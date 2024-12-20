from telethon import TelegramClient, events

from .data import Data


async def init(bot: TelegramClient, data: Data):
    """
    Initialize the bot with a message logging event handler.

    Args:
        bot (TelegramClient): The Telegram client instance.
        data (Data): The data handler instance.
    """

    @bot.on(events.NewMessage())
    async def log_new_message(event: events.NewMessage.Event):
        """
        Log new messages received by the bot.

        Args:
            event (events.NewMessage.Event): The event object containing message details.
        """
        data.user(event)

    @bot.on(events.MessageEdited())
    async def log_edited_message(event: events.MessageEdited.Event):
        """
        Log edited messages received by the bot.

        Args:
            event (events.MessageEdited.Event): The event object containing message details.
        """
        data.user(event)
