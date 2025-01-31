import asyncio
from uuid import uuid4

from telethon import Button, TelegramClient, events

from .ai import invoke_model
from .data import ChatData


class Queue:
    def __init__(self):
        self._index = []
        self._dict = dict()
        self._result = dict()

    async def set(self, uuid, data):
        self._index.append(uuid)
        self._dict[uuid] = data

    async def get(self, uuid):
        if self._result.get(uuid):
            return self._dict[uuid]
        self._result[uuid] = await invoke_model(
            "chat_completion", messages=self._dict[uuid]
        )

    async def delete(self, uuid):
        print(uuid)
        pass


queue = Queue()


async def init(bot: TelegramClient, data: ChatData):
    @bot.on(events.CallbackQuery)
    async def callback(event: events.CallbackQuery.Event):
        uuid = event.data.decode()
        data = await queue.get(uuid)
        if not data:
            return
        await event.edit(data)
        await asyncio.sleep(10)
        await queue.delete(uuid)

    @bot.on(events.InlineQuery)
    async def inline(event: events.InlineQuery.Event):
        builder = event.builder
        uuid = uuid4().hex
        await event.answer(
            [
                builder.article(
                    "AI 助手",
                    text="AI 思考中...",
                    buttons=Button.inline("刷新助手回复", data=uuid),
                ),
            ]
        )
        await queue.set(uuid, event.query)
