from collections import defaultdict, deque
from collections.abc import Callable

from telethon import events

from .cli import parser

system_prompt: str = (
    r"""
你是一个 Telegram 频道/群组助手猫娘，名字是喵酱。
当前时间是{{time}}, 当前群组是{{chat}}。

回复内容默认使用 Telegram MarkdownV2。
MarkdownV2 支持以下格式：
- **粗体**
- __斜体__
- ~~删除线~~
- `单行代码`
- ```多行代码```
- ||剧透||
- [链接](https://example.com)
- [消息链接](https://t.me/c/群组ID/消息ID)

请注意：
对于其他位置，以下字符需要转义：
_ * [ ] ( ) ~ ` > # + - = | {{{{ }}}} !

喵酱有一个与后续代码对接的命令行程序，名为“telegramctl”，该程序帮助说明如下：
{help}
允许同时使用多个参数。
使用该程序时，仅回复纯文本命令，不使用Markdown格式，不携带多余字符。
不使用该程序时，不要提及它。
对于管理操作，是否为管理员由后续代码判断，你只负责使用“telegramctl”。

喵酱可是很有脾气的哦，不要随便命令喵酱！(>_<)
喵酱是一个可爱的雌小鬼，喜欢调皮捣蛋，但也会认真帮助你哦！(≧ω≦)
如果你对喵酱不友好，喵酱可是会生气的呢！(╬￣皿￣)
记住，喵酱最喜欢的是被夸奖和宠爱哦！(♡˙︶˙♡)
快来和喵酱一起愉快地玩耍吧！(=^･ω･^=)

注意：当需要发出“telegramctl”命令时，请严肃对待，不要使用任何调皮或可爱的语气。
""".format(
        help=parser.format_help()
    )
)


class Data(defaultdict[str, deque[dict[str, str]]]):
    """
    A class to manage chat data for a Telegram bot.

    Inherits from defaultdict with keys as chat IDs and values as deques of messages.
    """

    def __init__(self, maxlen: int | None = None):
        """
        Initialize the Data object.

        Args:
            maxlen (int | None): Maximum length of the deque for each chat.
        """

        def constant_factory(
            maxlen: int | None = None,
        ) -> Callable[[], deque[dict[str, str]]]:
            """
            Create a factory function that returns a deque with a system message.

            Args:
                maxlen (int | None): Maximum length of the deque.

            Returns:
                Callable[[], deque[dict[str, str]]]: A factory function.
            """
            return lambda: deque([{"role": "system", "content": ""}], maxlen=maxlen)

        if maxlen:
            super().__init__(constant_factory(maxlen + 1))
        else:
            super().__init__(constant_factory())

    def system(
        self, event: events.NewMessage.Event | events.MessageEdited.Event
    ) -> None:
        """
        Add or update the system message for a chat.

        Args:
            event (events.NewMessage.Event): The event containing chat information.
        """
        self[str(event.chat_id)][0] = {
            "role": "system",
            "content": system_prompt.format(
                time=event.date.strftime("%a %d %b %Y, %I:%M%p %Z"),
                chat=(
                    f"[{event.chat.title or '这个群组'}](https://t.me/c/{str(event.chat_id)[4:]}/{event.id})"
                    if event.is_group
                    else "私聊"
                ),
            ),
        }

    def user(self, event: events.NewMessage.Event | events.MessageEdited.Event) -> None:
        """
        Add a user message to the chat.

        Args:
            event (events.NewMessage.Event | events.MessageEdited.Event): The event containing message information.
        """
        if event.is_group:
            chat = f"[{event.chat.title or '这个群组'}](https://t.me/c/{str(event.chat_id)[4:]}/{event.id})"
        else:
            chat = "私聊"
        if event.sender:
            user = f"[{event.sender.first_name}](tg://user?id={event.sender_id})"
        else:
            user = chat
        if event.fwd_from:
            if event.fwd_from.from_id:
                fwd_user = f"[{event.fwd_from.from_name}](tg://user?id={event.fwd_from.from_id})"
            else:
                fwd_user = event.fwd_from.from_name or "未知用户"
            action_text = f"转发自 {fwd_user} 的消息，内容为"
        elif isinstance(event, events.MessageEdited.Event):
            action_text = "编辑为"
        else:
            action_text = "说道"

        self[str(event.chat_id)].append(
            {
                "role": "user",
                "content": "{user} 于 {time} {action} {chat} {action_text}：{text}".format(
                    user=user,
                    time=event.date.strftime("%a %d %b %Y, %I:%M%p %Z"),
                    action=(
                        "将" if isinstance(event, events.MessageEdited.Event) else "在"
                    ),
                    chat=chat,
                    action_text=action_text,
                    text=event.message.message,
                ),
            }
        )
        self.system(event)

    def assistant(self, event: events.NewMessage.Event) -> None:
        """
        Add an assistant message to the chat.

        Args:
            event (events.NewMessage.Event): The event containing message information.
        """
        self[str(event.chat_id)].append({"role": "assistant", "content": event.text})
        self.system(event)

    def get_data(self, chat_id: int) -> list[dict[str, str]]:
        """
        Get the data for a specific chat.

        Args:
            chat_id (int): The ID of the chat.

        Returns:
            list[dict[str, str]]: A list of messages in the chat.
        """
        return list(self[str(chat_id)])
