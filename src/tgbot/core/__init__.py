from telethon import TelegramClient

from . import ai, message_log, ping, inline
from .data import ChatData
from ruamel.yaml import YAML
with open("config.yaml") as file:
    config=YAML().load(file)

async def init(bot: TelegramClient, data: ChatData):
    """
    Initialize the bot with the provided modules.

    Args:
        bot (TelegramClient): The Telegram client instance.
        data (Data): The data instance containing necessary information.
    """
    await message_log.init(bot, data)
    await ai.init(bot, data, config)
    await inline.init(bot,data)
    await ping.init(bot, data)
