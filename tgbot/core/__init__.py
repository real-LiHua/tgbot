from huggingface_hub import AsyncInferenceClient
from telethon import TelegramClient
from .data import Data

bot_data = Data(3)
client: AsyncInferenceClient = AsyncInferenceClient()


async def init(bot: TelegramClient):
    pass
