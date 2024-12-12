from huggingface_hub import AsyncInferenceClient
from telethon import TelegramClient, events
from .data import Data

client = AsyncInferenceClient()


async def init(bot: TelegramClient, data: Data):
    @bot.on(events.NewMessage(pattern="/ai", forwards=False))
    async def handler(event: events.NewMessage.Event):
        response = await client.chat.completions.create(
            model="meta-llama/Meta-Llama-3-8B-Instruct", messages=data.get_data(event.chat_id)
        )
        await event.reply(response.choices[0].message.content)
