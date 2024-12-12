from huggingface_hub import AsyncInferenceClient
from telethon import TelegramClient, events
from .data import Data

client = AsyncInferenceClient()


async def init(bot: TelegramClient, data: Data):
    @bot.on(events.NewMessage(pattern="/ai", forwards=False))
    async def handler(event: events.NewMessage.Event):
        response = await client.chat_completion(
            data.get_data(event.chat_id),
            model="Qwen/Qwen2.5-7B-Instruct",
        )
        await event.reply(response.choices[0].message.content)
