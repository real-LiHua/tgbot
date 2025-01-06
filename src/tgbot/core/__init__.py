from ruamel.yaml import YAML
from telethon import TelegramClient

from . import ai, inline, message_log, ping
from .data import ChatData

with open("config.yaml") as file:
    config = YAML().load(file)


async def init(bot: TelegramClient, data: ChatData):
    """
    Initialize the bot with the provided modules.

    Args:
        bot (TelegramClient): The Telegram client instance.
        data (Data): The data instance containing necessary information.
    """
    await message_log.init(bot, data)
    await ai.init(bot, data, config)
    await inline.init(bot, data)
    await ping.init(bot, data)
