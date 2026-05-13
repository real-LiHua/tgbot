import hashlib
import os
from typing import Any

from aiogram import Router, types
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.formatting import Bold, Pre, Text, as_list

from src.hotloader import register_handler, register_tool

router = Router(name="callback")

MAX_PENDING = 50
_pending: dict[str, dict[str, Any]] = {}


def add_pending(fid: str, data: dict[str, Any]) -> None:
    if len(_pending) >= MAX_PENDING:
        oldest = next(iter(_pending))
        _pending.pop(oldest)
    _pending[fid] = data


def pop_pending(fid: str) -> dict[str, Any] | None:
    return _pending.pop(fid, None)


def make_fid(name: str) -> str:
    return hashlib.md5(os.urandom(16)).hexdigest()[:8]


def approve_kb(fid: str) -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(text="✅ 批准", callback_data=f"feature:approve:{fid}"),
            InlineKeyboardButton(text="❌ 拒绝", callback_data=f"feature:reject:{fid}"),
            InlineKeyboardButton(text="✏️ 修改建议", callback_data=f"feature:revise:{fid}"),
        ]
    ])


@router.callback_query(lambda c: c.data and c.data.startswith("feature:"))
async def handle_feature_callback(query: types.CallbackQuery) -> None:
    parts = query.data.split(":", 2)
    if len(parts) != 3:
        await query.answer("无效的回调", show_alert=True)
        return

    action, fid = parts[1], parts[2]
    feature = pop_pending(fid)
    if not feature:
        await query.answer("该功能请求已过期", show_alert=True)
        return

    name = feature.get("name", "未知")
    code = feature.get("code", "")
    chat_id = feature.get("chat_id")

    match action:
        case "approve":
            try:
                if chat_id is None:
                    raise ValueError("缺少 chat_id")
                if "@ai.tool" in code:
                    tool_name = await register_tool(chat_id, code)
                    content = Text("✅ 功能「", Bold(name), "」已热加载 (工具: ", Bold(tool_name), ")")
                elif "router = Router(" in code:
                    handler_name = register_handler(chat_id, code)
                    content = Text("✅ 功能「", Bold(name), "」已热加载 (处理器: ", Bold(handler_name), ")")
                else:
                    content = as_list(
                        Text("✅ 功能「", Bold(name), "」已批准！"),
                        Pre(code, language="python"),
                        "无法自动识别类型，请手动应用后重启 bot。",
                        sep="\n\n",
                    )
                await query.message.edit_text(**content.as_kwargs())
            except Exception as e:
                await query.message.edit_text(
                    f"❌ 热加载失败: {e}\n\n```python\n{code}\n```\n请手动应用后重启 bot。"
                )
            await query.answer("已批准")

        case "reject":
            await query.message.edit_text(**Text("❌ 功能「", Bold(name), "」已拒绝").as_kwargs())
            await query.answer("已拒绝")

        case "revise":
            await query.message.edit_text(**as_list(
                Text("📝 请描述对「", Bold(name), "」的修改建议："),
                Pre(code[:1500], language="python"),
                sep="\n\n",
            ).as_kwargs())
            await query.answer()
