from telethon import TelegramClient

from . import ai, inline, ping, reset
from .data import ChatData


async def init(bot: TelegramClient, data: ChatData):
    """
    Initialize the bot with the provided modules.

    Args:
        bot (TelegramClient): The Telegram client instance.
        data (Data): The data instance containing necessary information.
    """
    await inline.init(bot, data)
    await ai.init(bot, data)
    await ping.init(bot, data)
    await reset.init(bot, data)
