from aiogram import Router, types

from src.ai_service_client import chat_stream

router = Router(name="chat")


@router.message()
async def handle_message(message: types.Message) -> None:
    if message.text and message.text.startswith("/"):
        return

    text = message.text or message.caption or ""
    if not text.strip():
        return

    sent = await message.answer("...")

    messages = [{"role": "user", "content": text}]

    full = ""
    async for event in chat_stream(messages, [], chat_id=message.chat.id):
        if event["type"] == "delta":
            full += event["text"]
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
