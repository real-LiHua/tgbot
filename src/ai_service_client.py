import json
import logging
import os

import httpx

from src.config import AI_SERVICE_URL

logger = logging.getLogger(__name__)

_API_KEY = os.environ.get("AI_SERVICE_API_KEY", "")


def _headers() -> dict[str, str]:
    if _API_KEY:
        return {"X-Api-Key": _API_KEY}
    return {}


def tool_to_schema(tool: object) -> dict:
    s = tool.schema
    return {
        "name": s.name,
        "description": s.description,
        "param_schema": s.param_schema,
    }


def tool_names(tools: list) -> list[str]:
    return [t.schema.name for t in tools]


async def chat_stream(messages: list[dict], tools: list, chat_id: int):
    tool_dicts = [tool_to_schema(t) for t in tools]
    remote_names = tool_names(tools)

    body = {
        "chat_id": chat_id,
        "messages": messages,
        "tools": tool_dicts,
        "remote_tools": remote_names,
    }

    async with httpx.AsyncClient(timeout=600) as sse_client:
        async with sse_client.stream(
            "POST",
            f"{AI_SERVICE_URL}/api/chat",
            json=body,
            headers=_headers(),
        ) as resp:
            async for line in resp.aiter_lines():
                line = line.strip()
                if not line.startswith("data: "):
                    continue
                try:
                    event = json.loads(line[6:])
                except json.JSONDecodeError:
                    continue

                if event["type"] == "tool_call":
                    result = await _execute_tool(event, tools)
                    async with httpx.AsyncClient(timeout=120) as _:
                        resp2 = await _.post(
                            f"{AI_SERVICE_URL}/api/chat/result",
                            json={"tool_call_id": event["call_id"], "result": result},
                            headers=_headers(),
                        )
                        resp2.raise_for_status()
                    yield {"type": "tool_result", "name": event["name"]}
                elif event["type"] == "delta":
                    yield event
                elif event["type"] == "done":
                    yield event
                    return


async def _execute_tool(event: dict, tools: list) -> str:
    name = event["name"]
    args = event["args"]
    for t in tools:
        if t.schema.name == name:
            try:
                result = await t.fn(**args)
                return str(result)
            except Exception:
                logger.exception("tool %s failed", name)
                return f"ERROR: tool '{name}' execution failed"
    return f"ERROR: tool '{name}' not found"


async def list_models() -> list[str]:
    async with httpx.AsyncClient() as c:
        resp = await c.post(f"{AI_SERVICE_URL}/api/models", json={}, timeout=30, headers=_headers())
        resp.raise_for_status()
        data = resp.json()
        return data.get("models", [])
