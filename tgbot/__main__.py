import asyncio
from os import getenv
from dotenv import load_dotenv
from telethon import TelegramClient
import logging
from telethon.sessions import MemorySession
from . import core
from . import plugins

logging.basicConfig(level=logging.WARNING)
logging.getLogger("asyncio").setLevel(logging.ERROR)
_ = load_dotenv()


async def main():
    bot:TelegramClient = TelegramClient(
        MemorySession(), 611335, "d524b414d21f4d37f08684c1df41ac9c"
    ).start(bot_token=getenv("BOT_TOKEN", ""))
    try:
        await core.init(bot)
        await plugins.init(bot)
        bot.run_until_disconnected()
    finally:
        bot.disconnect()


asyncio.run(main())
