from telethon import TelegramClient, events

from .data import ChatData


async def init(bot: TelegramClient, data: ChatData):
    """
    Initialize the bot with a reset command handler.

    Args:
        bot (TelegramClient): The Telegram client instance.
        data (ChatData): The chat data instance.
    """

    @bot.on(events.NewMessage(pattern="/reset", forwards=False))
    async def handler(event: events.NewMessage.Event):
        """
        Handle the /reset command by clearing the chat data.

        Args:
            event (events.NewMessage.Event): The new message event.
        """
        data[event.chat_id].clear()
        if data[event.chat_id]:
            await event.reply("清理失败！")
        else:
            await event.reply("清理完成！")
