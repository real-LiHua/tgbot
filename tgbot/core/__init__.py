from telethon import TelegramClient
from .data import Data
from . import message_log, ping, ai


async def init(bot: TelegramClient, data: Data):
    await message_log.init(bot, data)
    await ai.init(bot, data)
    await ping.init(bot)
