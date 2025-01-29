import asyncio
import gc
import logging
from os import getenv
from os.path import join
from pathlib import Path

from dotenv import load_dotenv
from telethon import TelegramClient

from . import core, plugins
from .core import message_log
from .core.data import ChatData

gc.set_debug(gc.get_debug() | gc.DEBUG_UNCOLLECTABLE)

logging.basicConfig(level=logging.DEBUG)
logging.getLogger("asyncio").setLevel(logging.ERROR)
load_dotenv()


async def main():
    """
    Main function to initialize and run the Telegram bot.
    """
    Path("site").mkdir(exist_ok=True)
    bot: TelegramClient = TelegramClient(
        join("site", "bot"), 611335, "d524b414d21f4d37f08684c1df41ac9c", catch_up=True
    )
    await bot.start(bot_token=getenv("BOT_TOKEN", ""))
    try:
        data = ChatData(4096, join("site", "data.json"))
        await message_log.init(bot, data)
        await core.init(bot, data)
        await plugins.init(bot)
        await bot.run_until_disconnected()
    finally:
        await bot.disconnect()


asyncio.run(main())
