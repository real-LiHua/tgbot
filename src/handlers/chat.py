import ai
from aiogram import Router, types

from src.ai.provider import get_model
from src.ai.tools import make_telegram_tools

router = Router(name="chat")


@router.message()
async def handle_message(message: types.Message) -> None:
    if message.text and message.text.startswith("/"):
        return

    text = message.text or message.caption or ""
    if not text.strip():
        return

    sent = await message.answer("...")
    model = get_model()
    bot = message.bot
    tools = make_telegram_tools(bot, chat_id=message.chat.id)
    agent = ai.agent(tools=tools)

    msgs = [
        ai.system_message(
            "你是一个 Telegram 群组 AI 助手。"
            "使用工具与群组交互：发送消息、管理成员、发送媒体等。"
            "请用中文回答，保持简洁有用。"
        ),
        ai.user_message(text),
    ]

    full = ""
    async for msg in agent.run(model, msgs):
        if msg.text_delta:
            full += msg.text_delta
            if len(full) < 4000:
                try:
                    await sent.edit_text(full)
                except Exception:
                    pass

    if full:
        parts = [full[i:i + 4000] for i in range(0, len(full), 4000)]
        try:
            await sent.edit_text(parts[0])
        except Exception:
            await message.answer(parts[0])
        for p in parts[1:]:
            await message.answer(p)
