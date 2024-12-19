import asyncio
import logging
from os import getenv

from dotenv import load_dotenv

from telethon import TelegramClient
from telethon.sessions import MemorySession

from . import core, plugins
from .core.data import Data

logging.basicConfig(level=logging.WARNING)
logging.getLogger("asyncio").setLevel(logging.ERROR)
load_dotenv()


async def main():
    bot: TelegramClient = TelegramClient(
        "site/bot", 611335, "d524b414d21f4d37f08684c1df41ac9c"
    )
    await bot.start(bot_token=getenv("BOT_TOKEN", ""))
    try:
        data = Data(3)
        await core.init(bot, data)
        # await plugins.init(bot)
        await bot.run_until_disconnected()
    finally:
        await bot.disconnect()


asyncio.run(main())
