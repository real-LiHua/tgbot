from collections import defaultdict, deque
from collections.abc import Callable
from datetime import datetime

from telethon import events

from .cli import parser

system_prompt = r"""
你是一个 Telegram 频道/群组 助手，当前时间是{{time}}, 当前群组是{{chat}}
回复内容默认使用 Telegram MarkdownV2
你有一个与后续代码对接的命令行程序，名为“telegramctl”，该程序帮助说明如下：
{help}
允许同时使用多个参数
当使用该命令行程序时，应仅回复纯文本（不使用Markdown格式）的命令，且不要携带多余的字符
如携带多余字符，后续代码会认为这是普通文本消息
""".format(
    help=parser.format_help()
)


class Data(defaultdict[str, deque[dict[str, str]]]):
    def __init__(self, maxlen: int | None = None):
        def constant_factory(
            maxlen: int | None = None,
        ) -> Callable[[], deque[dict[str, str]]]:
            return lambda: deque([{"role": "system", "content": ""}], maxlen=maxlen)

        if maxlen:
            super().__init__(constant_factory(maxlen + 1))
        else:
            super().__init__(constant_factory())

    def system(self, event: events.NewMessage.Event):
        assert isinstance(event.chat_id, int)
        assert isinstance(event.date, datetime)
        assert isinstance(event.text, str)
        self[str(event.chat_id)][0] = {
            "role": "system",
            "content": system_prompt.format(
                time=event.date.strftime("%a %d %b %Y, %I:%M%p %Z"), chat=""
            ),
        }

    def user(self, event: events.NewMessage.Event):
        self[str(event.chat_id)].append(
            {
                "role": "user",
                "content": "{user}于{time}在{chat}说道：{text}".format(
                    user="",
                    time=event.date.strftime("%a %d %b %Y, %I:%M%p %Z"),
                    chat="",
                    text=event.text,
                ),
            }
        )
        self.system(event)

    def assistant(self, event: events.NewMessage.Event):
        self[str(event.chat_id)].append({"role": "assistant", "content": "".format()})
        self.system(event)

    def get_data(self, chat_id: int):
        return list(self[str(chat_id)])
