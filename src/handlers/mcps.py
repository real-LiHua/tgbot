import argparse
import shlex

import ai
from aiogram import Router, types
from aiogram.filters import Command
from aiogram.utils.formatting import Bold, Code, as_list

router = Router(name="mcps")

_parser = argparse.ArgumentParser(prog="/mcps", description="MCP 服务器工具管理")
_sub = _parser.add_subparsers(dest="cmd")

p = _sub.add_parser("http", help="连接 HTTP MCP 服务器并列出工具")
p.add_argument("url", help="服务器 URL")

p = _sub.add_parser("stdio", help="启动 stdio MCP 服务器并列出工具")
p.add_argument("command", help="命令")
p.add_argument("args", nargs=argparse.REMAINDER, help="命令参数")


@router.message(Command("mcps"))
async def handle_mcps(message: types.Message) -> None:
    raw = message.text.removeprefix("/mcps").strip()
    argv = raw.split() if raw else ["--help"]

    if argv[0] == "stdio":
        rest = raw.removeprefix("stdio").strip()
        argv = ["stdio", *shlex.split(rest)] if rest else ["stdio"]

    try:
        ns = _parser.parse_args(argv)
    except (SystemExit, argparse.Error):
        await message.answer(_parser.format_help())
        return

    match ns.cmd:
        case "http":
            await _http(message, ns.url)
        case "stdio":
            await _stdio(message, ns.command, ns.args)
        case _:
            await message.answer(_parser.format_help())


async def _http(message: types.Message, url: str) -> None:
    sent = await message.answer(f"正在连接 MCP 服务器: {url}")
    try:
        tools = await ai.mcp.get_http_tools(url)
    except Exception as e:
        await sent.edit_text(f"连接失败: {e}")
        return
    if not tools:
        await sent.edit_text("该服务器未提供任何工具。")
        return
    lines = [Bold(f"🔧 MCP 工具列表 ({len(tools)} 个):\n")]
    for t in tools:
        s = t.schema
        params = " ".join(f"<{k}>" for k in (s.param_schema or {}).get("properties", {}))
        lines.append(f"  {Code(s.name)} {params}".rstrip())
        if s.description:
            lines.append(f"    {s.description[:100]}")
    await sent.edit_text(**as_list(*lines).as_kwargs())


async def _stdio(message: types.Message, cmd: str, args: list[str]) -> None:
    sent = await message.answer(f"正在启动: {cmd} {' '.join(args)}")
    try:
        tools = await ai.mcp.get_stdio_tools(cmd, *args)
    except Exception as e:
        await sent.edit_text(f"启动失败: {e}")
        return
    if not tools:
        await sent.edit_text("该服务器未提供任何工具。")
        return
    lines = [Bold(f"🔧 MCP 工具列表 ({len(tools)} 个):\n")]
    for t in tools:
        s = t.schema
        params = " ".join(f"<{k}>" for k in (s.param_schema or {}).get("properties", {}))
        lines.append(f"  {Code(s.name)} {params}".rstrip())
        if s.description:
            lines.append(f"    {s.description[:100]}")
    await sent.edit_text(**as_list(*lines).as_kwargs())
