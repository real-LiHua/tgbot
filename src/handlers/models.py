from aiogram import Router, types
from aiogram.filters import Command

from src.ai.provider import get_model

router = Router(name="models")


@router.message(Command("models"))
async def handle_models(message: types.Message) -> None:
    sent = await message.answer("正在获取可用模型列表...")
    try:
        model = get_model()
        models = await model.provider.list()
    except Exception:
        await sent.edit_text(
            "获取模型列表失败，请检查 API 密钥和网络连接是否正常。"
        )
        return

    if not models:
        await sent.edit_text("暂无可用模型。")
        return

    lines = [f"📋 可用模型 ({len(models)} 个):\n"]
    for m in models:
        lines.append(f"  • `{m}`")

    await sent.edit_text("\n".join(lines))
