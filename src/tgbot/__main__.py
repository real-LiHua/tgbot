import asyncio
import gc
import logging
import os

from opentele.api import API, CreateNewSession
from opentele.td import TDesktop
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
    if os.name == "nt":
        base_dir = os.getenv("APPDATA", os.path.expanduser(r"~\AppData\Roaming"))
    else:
        base_dir = os.getenv("XDG_DATA_HOME", os.path.expanduser("~/.local/share"))
    session_path = os.path.join(base_dir, "tgbot", "bot")
    os.makedirs(os.path.dirname(session_path), exist_ok=True)
    config = CONFIG.get("telegram", dict())
    api_id = config.get("api_id", 611335)
    api_hash = config.get("api_hash", "d524b414d21f4d37f08684c1df41ac9c")
    if not os.path.exists(f"{session_path}.session"):
        tdataFolder = config.get("tdata")
        if tdataFolder:
            tdesk = TDesktop(tdataFolder)
            api = API.TelegramDesktop(api_id, api_hash)
            await tdesk.ToTelethon(
                "bot.session", CreateNewSession, api, config.get("password")
            )
    data_path = os.path.join(base_dir, "tgbot", "data.json")
    data = ChatData(4096, data_path)
    logging.info("Initializing bot...")
    bot: TelegramClient = TelegramClient(
        session_path,
        api_id,
        api_hash,
        catch_up=True,
    )
    try:
        await bot.start(bot_token=config.get("bot_token"))
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
