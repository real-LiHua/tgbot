from telethon import TelegramClient

from . import ai, message_log, ping
from .data import Data

async def init(bot: TelegramClient, data: Data):
    await message_log.init(bot, data)
    await ai.init(bot, data)
    await ping.init(bot)
