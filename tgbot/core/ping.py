import platform
import time

from telethon import TelegramClient, events

from .data import ChatData


async def init(bot: TelegramClient, data: ChatData):
    """
    Initialize the bot with a ping command handler.

    Args:
        bot (TelegramClient): The Telegram client instance.
    """

    @bot.on(events.NewMessage(pattern="/ping", forwards=False))
    async def handler(event: events.NewMessage.Event):
        """
        Handle the /ping command by replying with "Pong!" and measuring the response time.

        Args:
            event (events.NewMessage.Event): The new message event.
        """
        s = time.time()
        message = await event.reply("Pong!")
        d = time.time() - s
        os_info = platform.system()
        data.assistant(
            await message.edit(f"Pong! __(reply took {d:.2f}s)__ on {os_info}")
        )
