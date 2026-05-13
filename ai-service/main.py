import asyncio
import hmac
import json
import logging
import os
from collections.abc import AsyncGenerator
from typing import Any

import ai
from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import StreamingResponse
from pydantic import BaseModel, Field

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("ai-service")

AI_PROVIDER = os.environ.get("AI_PROVIDER", "openai")
AI_MODEL_ID = os.environ.get("AI_MODEL_ID") or None
API_KEY = os.environ.get("AI_SERVICE_API_KEY") or ""

app = FastAPI(title="AI Service")

_pending_tool_calls: dict[str, asyncio.Future[str]] = {}


def _verify_api_key(request: Request) -> None:
    if not API_KEY:
        return
    key = request.headers.get("X-Api-Key", "")
    if not hmac.compare_digest(key, API_KEY):
        raise HTTPException(403, "invalid api key")


def _get_model() -> ai.Model:
    provider = AI_PROVIDER.lower()
    if provider == "openai":
        return ai.openai(AI_MODEL_ID or "gpt-4o-mini")
    elif provider == "anthropic":
        return ai.anthropic(AI_MODEL_ID or "claude-sonnet-4")
    elif provider == "ai_gateway":
        return ai.ai_gateway(AI_MODEL_ID or "openai/gpt-4o-mini")
    else:
        raise ValueError(f"Unknown AI provider: {provider}")


def _build_stub_tools(
    tools_data: list[dict],
) -> list[ai.Tool]:
    result: list[ai.Tool] = []
    for td in tools_data:
        name = td.get("name", "unknown")
        schema = ai.types.tools.ToolSchema(
            name=name,
            description=td.get("description", ""),
            param_schema=td.get("param_schema", {"type": "object", "properties": {}}),
            return_type=str,
        )

        async def _stub(**kwargs: Any) -> str:
            return json.dumps(kwargs)

        result.append(ai.Tool(fn=_stub, schema=schema))
    return result


MAX_ITERATIONS = 10


async def _chat_stream(
    model: ai.Model,
    messages: list[ai.Message],
    tools: list[ai.Tool],
    remote_tool_names: set[str],
    call_ids_for_request: set[str],
) -> AsyncGenerator[str, None]:
    iterations = 0
    while True:
        iterations += 1
        if iterations > MAX_ITERATIONS:
            yield 'data: {"type":"done"}\n\n'
            return
        stream = await ai.stream(model, messages, tools=tools)
        async for msg in stream:
            if msg.text_delta:
                event = {"type": "delta", "text": msg.text_delta}
                yield f"data: {json.dumps(event, ensure_ascii=False)}\n\n"

        messages.append(stream.message)

        tool_calls = stream.tool_calls
        if not tool_calls:
            yield 'data: {"type":"done"}\n\n'
            return

        results: list[ai.ToolResultPart] = []
        for tc in tool_calls:
            if tc.name in remote_tool_names:
                call_id = os.urandom(8).hex()
                future: asyncio.Future[str] = asyncio.get_running_loop().create_future()
                _pending_tool_calls[call_id] = future
                call_ids_for_request.add(call_id)
                event = {
                    "type": "tool_call",
                    "call_id": call_id,
                    "name": tc.name,
                    "args": tc.args,
                    "tool_call_id": tc.id,
                }
                yield f"data: {json.dumps(event, ensure_ascii=False)}\n\n"
                try:
                    result = await asyncio.wait_for(future, timeout=300)
                except asyncio.TimeoutError:
                    result = f"ERROR: tool '{tc.name}' timed out"
                finally:
                    _pending_tool_calls.pop(call_id, None)
                    call_ids_for_request.discard(call_id)
                results.append(ai.tool_result(tc.id, result))
            else:
                results.append(ai.tool_result(tc.id, f"ERROR: unknown tool '{tc.name}'"))

        messages.append(ai.tool_message(*results))


def _deserialize_messages(msgs: list[dict]) -> list[ai.Message]:
    result: list[ai.Message] = []
    for m in msgs:
        role = m.get("role", "user")
        content = m.get("content", "")
        if role == "system":
            result.append(ai.system_message(content))
        elif role == "user":
            result.append(ai.user_message(content))
        elif role == "assistant":
            result.append(ai.assistant_message(content))
        elif role == "tool":
            tid = m.get("tool_call_id", "")
            result.append(ai.tool_message(ai.tool_result(tid, content)))
    return result


class ChatRequest(BaseModel):
    chat_id: int
    messages: list[dict[str, Any]] = Field(default_factory=list)
    tools: list[dict[str, Any]] = Field(default_factory=list)
    remote_tools: list[str] = Field(default_factory=list)


class ToolResultRequest(BaseModel):
    tool_call_id: str
    result: str = ""


@app.post("/api/chat")
async def chat(req: ChatRequest, request: Request):
    _verify_api_key(request)
    model = _get_model()
    messages = _deserialize_messages(req.messages)
    tools = _build_stub_tools(req.tools)
    remote_tool_names = set(req.remote_tools)

    call_ids_for_request: set[str] = set()

    async def event_stream():
        nonlocal call_ids_for_request
        try:
            async for event in _chat_stream(model, messages, tools, remote_tool_names, call_ids_for_request):
                yield event
        finally:
            for cid in call_ids_for_request:
                future = _pending_tool_calls.pop(cid, None)
                if future is not None and not future.done():
                    future.cancel()

    return StreamingResponse(
        event_stream(),
        media_type="text/event-stream",
        headers={
            "Cache-Control": "no-cache",
            "X-Accel-Buffering": "no",
        },
    )


@app.post("/api/chat/result")
async def chat_result(req: ToolResultRequest, request: Request):
    _verify_api_key(request)
    future = _pending_tool_calls.get(req.tool_call_id)
    if future is None:
        return {"ok": False, "error": "tool_call_id not found"}
    future.set_result(req.result)
    return {"ok": True}


@app.post("/api/models")
async def list_models(request: Request):
    _verify_api_key(request)
    try:
        model = _get_model()
        models = await model.provider.list()
    except Exception:
        return {"models": []}
    return {"models": models or []}


@app.get("/health")
async def health():
    return {"status": "ok"}
