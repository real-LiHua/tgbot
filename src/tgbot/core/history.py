import logging
from shutil import unpack_archive
from tempfile import TemporaryFile

from telethon import TelegramClient, events

from .data import ChatData

no_events = (
    "UpdateMessageID",
    "UpdateNewChannelMessage",
    "UpdateUser",
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

    @bot.on(events.NewMessage(pattern="/import_history", forwards=False))
    async def history(event: events.NewMessage.Event):
        """
        Handle the /import_history command to import message history from a file.

        Args:
            event (events.NewMessage.Event): The event object containing the message.
        """
        if event.message.is_reply:
            reply_message = await event.message.get_reply_message()
            with TemporaryFile() as fp:
                await reply_message.download_media(fp)
                unpack_archive(fp.read(), str(event.chat_id))
        # await data.import_from_archive(event.message.reply_to.file)

    @bot.on(events.Raw)
    async def handler(update):
        """
        Handle raw events and process updates that are not in the no_events list.

        Args:
            update: The update object containing the event data.
        """
        if update.__class__.__name__ in no_events:
            return
        logging.debug(update)
        await data.user(update)
