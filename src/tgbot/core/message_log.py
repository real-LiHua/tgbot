from telethon import TelegramClient, events

from .data import ChatData

no_events = (
    "UpdateNewChannelMessage",
    "UpdateMessageID",
    "UpdateReadChannelInbox",
    "UpdateReadChannelOutbox",
)


async def init(bot: TelegramClient, data: ChatData):
    """
    Initialize the bot with a message logging event handler.

    Args:
        bot (TelegramClient): The Telegram client instance.
        data (Data): The data handler instance.
    """

    @bot.on(events.Raw)
    async def handler(update):
        if update.__class__.__name__ in no_events:
            return
        print(update)
        data.user(update)
