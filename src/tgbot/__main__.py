import asyncio
import gc
import logging
import os

from telethon import TelegramClient

from . import CONFIG, core, plugins
from .core import history
from .core.data import ChatData

gc.set_debug(gc.get_debug() | gc.DEBUG_UNCOLLECTABLE)

logging.basicConfig(level=logging.INFO)
logging.getLogger("asyncio").setLevel(logging.DEBUG)


async def main():
    """
    Main function to initialize and run the Telegram bot.
    """
    xdg_data_home = os.getenv("XDG_DATA_HOME", os.path.expanduser("~/.local/share"))
    session_path = os.path.join(xdg_data_home, "tgbot", "bot")
    os.makedirs(os.path.dirname(session_path), exist_ok=True)
    data_path = os.path.join(xdg_data_home, "tgbot", "data.json")
    data = ChatData(4096, data_path)
    logging.info("Initializing bot...")
    bot: TelegramClient = TelegramClient(
        session_path,
        CONFIG.get("app_id", 611335),
        CONFIG.get("app_hash", "d524b414d21f4d37f08684c1df41ac9c"),
        catch_up=True,
    )
    try:
        await bot.start(bot_token=CONFIG.get("bot_token"))
        await history.init(bot, data)
        await core.init(bot, data)
        await plugins.init(bot)
        logging.info("Bot initialized successfully")
    except Exception as e:
        logging.error(f"Error Initializing bot: {e}")
    try:
        await bot.run_until_disconnected()
    finally:
        await bot.disconnect()


asyncio.run(main())
