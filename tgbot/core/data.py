from collections import defaultdict, deque
from collections.abc import Callable

from telethon import events

from .cli import parser

system_prompt = r"""
你是一个 Telegram 频道/群组助手。
当前时间是{{time}}, 当前群组是{{chat}}。

回复内容默认使用 Telegram MarkdownV2。
MarkdownV2 支持以下格式：
- **粗体**
- __斜体__
- ~~删除线~~
- `单行代码`
- ```多行代码```
- [链接](https://example.com)
注意：以下字符需要转义：
_ * [ ] ( ) ~ ` > # + - = | {{{{ }}}} . !

你有一个与后续代码对接的命令行程序，名为“telegramctl”，该程序帮助说明如下：
{help}
允许同时使用多个参数。
使用该命令行程序时，应仅回复纯文本（不使用Markdown格式）的命令，且不要携带多余字符。
如携带多余字符，后续代码会认为这是普通文本消息。
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
        self[str(event.chat_id)][0] = {
            "role": "system",
            "content": system_prompt.format(
                time=event.date.strftime("%a %d %b %Y, %I:%M%p %Z"),
                chat=(
                    f"[{event.chat.title}](https://t.me/c/{event.chat_id}/{event.id})"
                    if event.is_group
                    else "私聊"
                ),
            ),
        }

    def user(self, event: events.NewMessage.Event):
        if event.sender:
            user = f"[{event.sender.first_name}](tg://user?id={event.sender_id})"
        else:
            user = f"[{event.chat.title}](https://t.me/c/{event.chat_id}/{event.id})"

        self[str(event.chat_id)].append(
            {
                "role": "user",
                "content": "{user}于{time}在{chat}说道：{text}".format(
                    user=user,
                    time=event.date.strftime("%a %d %b %Y, %I:%M%p %Z"),
                    chat=(
                        f"[{event.chat.title}](https://t.me/c/{event.chat_id}/{event.id})"
                        if event.is_group
                        else "私聊"
                    ),
                    text=event.text,
                ),
            }
        )
        self.system(event)

    def assistant(self, event: events.NewMessage.Event):
        self[str(event.chat_id)].append({"role": "assistant", "content": event.text})
        self.system(event)

    def get_data(self, chat_id: int):
        return list(self[str(chat_id)])
