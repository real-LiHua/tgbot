import json
import logging

import httpx

from src.config import DOCKER_AGENT_URL

logger = logging.getLogger(__name__)

_sessions: dict[int, str] = {}
_agent_name = "agent"


async def _get_session(chat_id: int) -> str:
    if chat_id in _sessions:
        return _sessions[chat_id]
    async with httpx.AsyncClient() as c:
        resp = await c.post(f"{DOCKER_AGENT_URL}/api/sessions", json={})
        resp.raise_for_status()
        data = resp.json()
        _sessions[chat_id] = data["id"]
        return data["id"]


async def chat_stream(messages: list[dict], tools: list, chat_id: int):
    session_id = await _get_session(chat_id)
    body = [m for m in messages if m.get("role") != "system"]

    async with httpx.AsyncClient(timeout=600) as client:
        async with client.stream(
            "POST",
            f"{DOCKER_AGENT_URL}/api/sessions/{session_id}/agent/{_agent_name}",
            json=body,
        ) as resp:
            async for line in resp.aiter_lines():
                line = line.strip()
                if not line.startswith("data: "):
                    continue
                try:
                    event = json.loads(line[6:])
                except json.JSONDecodeError:
                    continue

                etype = event.get("type", "")

                if etype == "agent_choice":
                    yield {"type": "delta", "text": event.get("content", "")}
                elif etype == "tool_call_confirmation":
                    async with httpx.AsyncClient() as c:
                        await c.post(
                            f"{DOCKER_AGENT_URL}/api/sessions/{session_id}/resume",
                            json={"approve": True},
                        )
                elif etype == "stream_stopped":
                    yield {"type": "done"}
                    return
                elif etype == "error":
                    logger.error("docker agent error: %s", event.get("content", ""))
                    yield {"type": "done"}
                    return


async def list_models() -> list[str]:
    async with httpx.AsyncClient() as c:
        try:
            resp = await c.get(f"{DOCKER_AGENT_URL}/api/agents", timeout=30)
            resp.raise_for_status()
            return ["configured in agent.yaml"]
        except Exception:
            return []
