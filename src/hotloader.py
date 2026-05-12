import ast
import importlib.util
import json
import keyword
import logging
import re
import sys
from pathlib import Path
from typing import Any

import ai

logger = logging.getLogger(__name__)
from aiogram import Bot, Dispatcher, F, Router
from aiogram.filters import and_f

from src.sandbox_client import SandboxClient

_bot: Bot | None = None
_dp: Dispatcher | None = None
_dynamic_tools: dict[int, list[ai.Tool[..., Any]]] = {}
_dynamic_handlers: dict[int, dict[str, Any]] = {}
_sandboxes: dict[int, SandboxClient] = {}


def init(bot: Bot, dp: Dispatcher) -> None:
    global _bot, _dp
    _bot = bot
    _dp = dp


def get_dynamic_tools(chat_id: int) -> list[ai.Tool[..., Any]]:
    return list(_dynamic_tools.get(chat_id, []))


async def _ensure_sandbox(chat_id: int) -> SandboxClient:
    if chat_id not in _sandboxes:
        _sandboxes[chat_id] = await SandboxClient.create(timeout=300)
    return _sandboxes[chat_id]


def _is_valid_name(name: str) -> bool:
    return name.isidentifier() and not keyword.iskeyword(name)


def _parse_func_sig(code: str) -> tuple[str, str, dict[str, Any]]:
    tree = ast.parse(code)
    for node in ast.walk(tree):
        if not isinstance(node, ast.AsyncFunctionDef):
            continue
        name = node.name
        docstring = ast.get_docstring(node) or ""
        properties: dict[str, dict[str, str]] = {}
        required: list[str] = []
        all_args = list(node.args.posonlyargs) + list(node.args.args)
        for arg in all_args:
            if arg.arg in ("self", "cls"):
                continue
            properties[arg.arg] = {"type": "string"}
            required.append(arg.arg)
        defaults = node.args.defaults
        offset = len(all_args) - len(defaults)
        for i, _ in enumerate(defaults):
            idx = offset + i
            if 0 <= idx < len(all_args):
                a = all_args[idx].arg
                if a in required:
                    required.remove(a)
        param_schema = {"type": "object", "properties": properties, "required": required}
        return name, docstring, param_schema
    raise ValueError("no async function found in code")


async def register_tool(chat_id: int, code: str) -> str:
    tool_name, description, param_schema = _parse_func_sig(code)
    if not _is_valid_name(tool_name):
        raise ValueError(f"invalid tool name: {tool_name}")

    schema = ai.types.tools.ToolSchema(
        name=tool_name,
        description=description,
        param_schema=param_schema,
        return_type=str,
    )

    async def sandbox_handler(**kwargs: Any) -> str:
        return await _sandbox_run(chat_id, tool_name, code, kwargs)

    tool = ai.Tool(fn=sandbox_handler, schema=schema)
    _dynamic_tools.setdefault(chat_id, []).append(tool)
    return tool_name


async def _sandbox_run(chat_id: int, tool_name: str, code: str, kwargs: dict[str, Any]) -> str:
    client = await _ensure_sandbox(chat_id)
    await client.write_files([{"path": f"tools/{tool_name}.py", "content": code}])
    runner = (
        "import asyncio, json, importlib, os\n"
        "tn = os.environ['_TN']\n"
        "mod = importlib.import_module('tools.' + tn)\n"
        "fn = getattr(mod, tn)\n"
        "kw = json.loads(os.environ['_KW'])\n"
        "result = asyncio.run(fn(**kw))\n"
        "print(result)"
    )
    resp = await client.run_command(
        "python3", ["-c", runner],
        env={"_TN": tool_name, "_KW": json.dumps(kwargs, default=str)},
    )
    if resp["exit_code"] != 0:
        return f"sandbox error: {resp['stderr'].strip()}"
    return resp["stdout"].strip()


def _register_chat_router(router: Router, chat_id: int) -> Router:
    chat_router = Router(name=f"{router.name}_{chat_id}")
    for event_name, obs in router.observers.items():
        if not hasattr(obs, "handlers"):
            continue
        target_obs = chat_router.observers[event_name]
        for h in obs.handlers:
            target_obs.register(h.callback, and_f(F.chat.id == chat_id, *h.filters))
    if _dp is not None:
        _dp.include_router(chat_router)
    return chat_router


def register_handler(chat_id: int, code: str) -> str:
    match = re.search(r'router\s*=\s*Router\(name\s*=\s*["\'](\w+)["\']', code)
    name = match.group(1) if match else f"handler_{len(_dynamic_handlers)}"

    handler_dir = Path(f"dynamic/handlers/{chat_id}")
    handler_dir.mkdir(parents=True, exist_ok=True)
    path = handler_dir / f"{name}.py"
    path.write_text(code)

    mod_id = f"_dyn_{chat_id}_{name}"
    spec = importlib.util.spec_from_file_location(mod_id, str(path))
    if spec is None or spec.loader is None:
        raise ImportError(f"could not load {path}")
    mod = importlib.util.module_from_spec(spec)
    sys.modules[mod_id] = mod
    spec.loader.exec_module(mod)

    router = getattr(mod, "router", None)
    if router is None:
        raise ValueError("code must define a `router = Router(...)`")

    _register_chat_router(router, chat_id)
    _dynamic_handlers.setdefault(chat_id, {})[name] = mod
    return name


def auto_discover() -> None:
    base = Path("dynamic/handlers")
    if not base.is_dir():
        return
    for chat_dir in sorted(base.iterdir()):
        if not chat_dir.is_dir():
            continue
        try:
            chat_id = int(chat_dir.name)
        except ValueError:
            continue
        for path in sorted(chat_dir.glob("*.py")):
            name = path.stem
            if name in _dynamic_handlers.get(chat_id, {}):
                continue
            try:
                mod_id = f"_dyn_{chat_id}_{name}"
                spec = importlib.util.spec_from_file_location(mod_id, str(path))
                if spec is None or spec.loader is None:
                    continue
                mod = importlib.util.module_from_spec(spec)
                sys.modules[mod_id] = mod
                spec.loader.exec_module(mod)
                if hasattr(mod, "router"):
                    _register_chat_router(mod.router, chat_id)
                    _dynamic_handlers.setdefault(chat_id, {})[name] = mod
            except Exception as exc:
                logger.warning("auto_discover: failed to load %s/%s: %s", chat_dir.name, name, exc)
