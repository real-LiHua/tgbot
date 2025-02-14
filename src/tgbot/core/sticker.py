from telethon import TelegramClient, events, functions, types


async def init(bot: TelegramClient):
    @bot.on(events.NewMessage(pattern="/test", forwards=False))
    async def handler(event: events.NewMessage.Event):
        res = await bot(
            functions.messages.GetStickerSetRequest(
                types.InputStickerSetShortName("g0g8tary_1002023814798_by_mairen_quote_bot"),
                hash=0,
            ),
        )
        print(res)
