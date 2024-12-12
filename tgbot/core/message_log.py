from telethon import TelegramClient, events
from .data import Data


async def init(bot: TelegramClient, data: Data):
    @bot.on(events.NewMessage())
    async def message_log(event: events.NewMessage.Event):
        data.user(event)
