from telethon import events


async def init(bot):
    @bot.on(events.NewMessage)
    async def message_log(event):
        events.text
