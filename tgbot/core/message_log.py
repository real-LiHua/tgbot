from telethon import events
from telethon import TelegramClient


async def init(bot: TelegramClient):
    @bot.on(events.NewMessage)
    async def message_log(event: events.NewMessage.Event):
        pass
