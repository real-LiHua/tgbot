from argparse import ArgumentError

from dotenv import load_dotenv

from huggingface_hub import AsyncInferenceClient
from telethon import TelegramClient, events

from .cli import callback
from .data import Data

load_dotenv()

client = AsyncInferenceClient()


async def init(bot: TelegramClient, data: Data):
    @bot.on(events.NewMessage(pattern="/ai", forwards=False))
    async def handler(event: events.NewMessage.Event):
        response = await client.chat_completion(
            data.get_data(event.chat_id),
            model="Qwen/Qwen2.5-72B-Instruct",
            max_tokens=1000,
        )
        assistant = response.choices[0].message.content or ""
        try:
            await callback(assistant, event)
        except ArgumentError:
            reply = await event.reply(assistant)
        return assistant
