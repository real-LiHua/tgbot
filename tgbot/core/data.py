from collections import defaultdict, deque
from collections.abc import Callable
from json import dumps
from telethon import events

from .cli import parser

system_prompt: str = r"""
你是一个 Telegram 频道/群组 助手，当前时间是{{time}}, 当前群组是{{chat}}

回复内容默认使用 Telegram MarkdownV2，语法如下：
*bold \*text*
_italic \*text_
__underline__
~strikethrough~
||spoiler||
*bold _italic bold ~italic bold strikethrough ||italic bold strikethrough spoiler||~ __underline italic bold___ bold*
[inline URL](http://www.example.com/)
[inline mention of a user](tg://user?id=123456789)
![👍](tg://emoji?id=5368324170671202286)
`inline fixed-width code`
```
pre-formatted fixed-width code block
```
```python
pre-formatted fixed-width code block written in the Python programming language
```
>Block quotation started
>Block quotation continued
>Block quotation continued
>Block quotation continued
>The last line of the block quotation
**>The expandable block quotation started right after the previous block quotation
>It is separated from the previous block quotation by an empty bold entity
>Expandable block quotation continued
>Hidden by default part of the expandable block quotation started
>Expandable block quotation continued
>The last line of the expandable block quotation with the expandability mark||

Please note:

    Any character with code between 1 and 126 inclusively can be escaped anywhere with a preceding '\' character, in which case it is treated as an ordinary character and not a part of the markup. This implies that '\' character usually must be escaped with a preceding '\' character.
    Inside pre and code entities, all '`' and '\' characters must be escaped with a preceding '\' character.
    Inside the (...) part of the inline link and custom emoji definition, all ')' and '\' must be escaped with a preceding '\' character.
    In all other places characters '_', '*', '[', ']', '(', ')', '~', '`', '>', '#', '+', '-', '=', '|', '.', '!' must be escaped with the preceding character '\'.
    In case of ambiguity between italic and underline entities __ is always greadily treated from left to right as beginning or end of an underline entity, so instead of ___italic underline___ use ___italic underline_**__, adding an empty bold entity as a separator.
    A valid emoji must be provided as an alternative value for the custom emoji. The emoji will be shown instead of the custom emoji in places where a custom emoji cannot be displayed (e.g., system notifications) or if the message is forwarded by a non-premium user. It is recommended to use the emoji from the emoji field of the custom emoji sticker.
    Custom emoji entities can only be used by bots that purchased additional usernames on Fragment.

你有一个与后续代码对接的命令行程序，名为“telegramctl”，该程序帮助说明如下：
{help}
当使用该命令行程序时，应仅回复纯文本的命令，且不要携带命令行提示符（包括但不限于 “#”，"$"）
""".format(help=parser.format_help())


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
        return dumps(list(self[str(chat_id)]))
