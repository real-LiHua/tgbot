import asyncio
import logging
from time import time_ns

from telethon import Button, TelegramClient, events

from .ai import invoke_model
from .data import ChatData


class Queue:
    def __init__(self):
        self._index = []
        self._status = dict()
        self._dict = dict()
        self._result = dict()

    async def set(self, uid, data):
        self._index.append(uid)
        self._dict[uid] = data

    async def get(self, uid):
        if self._result.get(uid):
            return self._result[uid]
        if self._status.get(uid):
            return ""
        self._status[uid] = True
        for _ in range(3):
            response = await invoke_model(
                "completions",
                messages=[
                    {"role": "system", "content": "使用中文回复"},
                    {"role": "user", "content": await self.query(uid)},
                ],
            )
            if not response:
                continue
            self._result[uid] = response.choices[0].message.content
            return self._result[uid]
        else:
            self._status[uid] = False

    async def query(self, uid):
        if self._dict.get(uid):
            return self._dict[uid].query
        return ""

    async def delete(self, uid):
        for key in map(int, self._dict.keys()):
            if key <= uid:
                del self._dict[key]
                del self._result[key]
                del self._status[key]


queue = Queue()


async def init(bot: TelegramClient, data: ChatData):
    @bot.on(events.CallbackQuery)
    async def callback(event: events.CallbackQuery.Event):
        logging.debug(event)
        uid = event.data.decode()
        data = await queue.get(uid)
        if not data:
            return
        try:
            user = await queue.query(uid)
            await event.edit(
                f"user:\n{user}\n\n-------------------------\n\nassistant:\n{data}"
            )
            await asyncio.sleep(10)
            await queue.delete(uid)
        except Exception as e:
            logging.error(e)

    @bot.on(events.InlineQuery)
    async def inline(event: events.InlineQuery.Event):
        builder = event.builder
        uid = str(time_ns())
        await event.answer(
            [
                builder.article(
                    "AI 助手",
                    text="AI 思考中...",
                    buttons=Button.inline("刷新助手回复", data=uid),
                ),
            ]
        )
        await queue.set(uid, event.query)
