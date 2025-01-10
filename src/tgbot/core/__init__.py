from ruamel.yaml import YAML
from telethon import TelegramClient

from . import ai, ping, reset
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
    await ai.init(bot, data, config)
    await ping.init(bot, data)
    await reset.init(bot, data)
