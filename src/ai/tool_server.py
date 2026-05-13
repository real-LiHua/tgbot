import hmac
from collections.abc import Sequence
from typing import Any

import ai
from aiohttp import web
from aiogram import Bot

from src.ai.tools import make_telegram_tools
from src.config import BOT_TOOL_API_KEY


def _param_type_to_openapi(pt: str) -> str:
    return {"string": "string", "number": "number", "integer": "integer", "boolean": "boolean", "object": "object", "array": "array"}.get(pt, "string")


def _build_openapi_spec(tools: Sequence[ai.Tool]) -> dict:
    paths = {}
    for tool in tools:
        if not tool.schema:
            continue
        name = tool.schema.name
        description = (tool.schema.description or "")[:200]
        param_schema = tool.schema.param_schema or {"type": "object", "properties": {}}

        properties = {}
        required = param_schema.get("required", [])

        for pname, pschema in param_schema.get("properties", {}).items():
            ptype = _param_type_to_openapi(pschema.get("type", "string"))
            prop: dict[str, Any] = {"type": ptype}
            if pschema.get("description"):
                prop["description"] = pschema["description"]
            properties[pname] = prop

        paths[f"/api/tools/{name}"] = {
            "post": {
                "operationId": name,
                "description": description,
                "requestBody": {
                    "required": True,
                    "content": {
                        "application/json": {
                            "schema": {
                                "type": "object",
                                "properties": properties,
                                "required": required or None,
                            }
                        }
                    },
                },
                "responses": {
                    "200": {
                        "description": "Execution result",
                        "content": {
                            "application/json": {
                                "schema": {
                                    "type": "object",
                                    "properties": {"result": {"type": "string"}},
                                }
                            }
                        },
                    }
                },
            }
        }

    return {
        "openapi": "3.0.0",
        "info": {"title": "Telegram Bot Tools", "version": "1.0.0"},
        "servers": [{"url": "http://bot:8080"}],
        "paths": paths,
    }


def _check_auth(request: web.Request) -> web.Response | None:
    if not BOT_TOOL_API_KEY:
        return None
    key = request.headers.get("X-Api-Key", "")
    if not hmac.compare_digest(key, BOT_TOOL_API_KEY):
        return web.json_response({"error": "unauthorized"}, status=403)
    return None


def create_tool_routes(bot: Bot) -> list[web.RouteDef]:
    tools = make_telegram_tools(bot)
    tool_map: dict[str, ai.Tool] = {t.schema.name: t for t in tools if t.schema}
    spec = _build_openapi_spec(tools)

    async def openapi_handler(request: web.Request) -> web.Response:
        err = _check_auth(request)
        if err:
            return err
        return web.json_response(spec)

    async def tool_executor(request: web.Request) -> web.Response:
        err = _check_auth(request)
        if err:
            return err
        name = request.match_info.get("name", "")
        if name not in tool_map:
            return web.json_response({"error": f"unknown tool: {name}"}, status=404)
        try:
            body = await request.json()
        except Exception:
            body = {}
        try:
            result = await tool_map[name].fn(**body)
            return web.json_response({"result": str(result)})
        except Exception as e:
            return web.json_response({"error": str(e)}, status=500)

    return [
        web.get("/api/openapi.json", openapi_handler),
        web.post("/api/tools/{name}", tool_executor),
    ]
