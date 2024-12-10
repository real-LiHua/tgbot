import asyncio
import sys
from os import getenv,makedirs
from os.path import join

from dotenv import load_dotenv
from telethon import TelegramClient
import logging
logging.basicConfig(level=logging.WARNING)
logging.getLogger("asyncio").setLevel(logging.ERROR)
load_dotenv()
try:
    # Standalone script assistant.py with folder plugins/
    import core
    import plugins
except ImportError:
    try:
        # Running as a module with `python -m assistant` and structure:
        #
        #     assistant/
        #         __main__.py (this file)
        #         plugins/    (cloned)
        from . import core
        from . import plugins
    except ImportError:
        print(
            "could not load the plugins module, does the directory exist "
            "in the correct location?",
            file=sys.stderr,
        )

        exit(1)


async def main():
    #makedirs("env", exist_ok=True)
    bot = TelegramClient(611335, "d524b414d21f4d37f08684c1df41ac9c")
    await bot.start(bot_token=getenv("BOT_TOKEN"))
    try:
        await core.init(bot)
        await plugins.init(bot)
        await bot.run_until_disconnected()
    finally:
        await bot.disconnect()


asyncio.run(main())
