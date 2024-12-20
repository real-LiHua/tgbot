import asyncio
import logging
import os
from importlib import import_module
from time import time
from types import ModuleType

from telethon import TelegramClient


async def init(bot: TelegramClient):
    """
    Initialize all plugins for the bot.

    This function loads and initializes all Python modules in the current directory
    that have a filename starting with an alphabet character and ending with '.py',
    excluding '__init__.py'.

    Args:
        bot (TelegramClient): The Telegram client instance.
    """
    await asyncio.gather(
        *(
            _init_plugin(import_module(f"{__name__}.{file[:-3]}"), bot)
            for file in os.listdir(os.path.dirname(__file__))
            if file[0].isalpha() and file.endswith(".py") and file != "__init__.py"
        )
    )


async def _init_plugin(plugin: ModuleType, bot: TelegramClient):
    """
    Initialize a single plugin.

    This function attempts to initialize a given plugin module by calling its 'init'
    function if it exists. It logs the loading process and handles any exceptions
    that occur during initialization.

    Args:
        plugin (ModuleType): The plugin module to initialize.
        bot (TelegramClient): The Telegram client instance.
    """
    try:
        logging.warning(f"Loading plugin {plugin.__name__}…")
        start = time()
        ret = await plugin.init(bot) if hasattr(plugin, "init") else None
        logging.warning(f"Loaded plugin {plugin.__name__} (took {time() - start:.2f}s)")
    except Exception:
        logging.exception(f"Failed to load plugin {plugin}")
    else:
        if asyncio.iscoroutine(ret) or isinstance(ret, asyncio.Future):
            await ret
