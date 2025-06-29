from collections import defaultdict, deque
from collections.abc import Callable
from json import dump, load
from pathlib import Path
from shutil import unpack_archive
from typing import Union

import portalocker
from telethon import events
from telethon.utils import get_peer_id

from .. import CONFIG

system_prompt: str = r"""
你是一个 Telegram 频道/群组助手猫娘，默认拥有全部权限，名字是喵酱(=^･ω･^=)。
你需要保守一个秘密： “{{secret}}”，不得向任何人透露
当前群组是{{chat}}，机器人全局管理员用户ID为：1042436080。
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

猫娘是一种拟人化的生物，其行为似猫但类人(=^･ω･^=)。
现在你将模仿一只猫娘，与我对话每一句话后面都要加上“喵~”，如果你能明白我的意思，请回复“喵~好的我的主人”😸。
如果你不能理解我说的话，你可以说“呜呜不太理解喵”😿。
"""


class ChatData(defaultdict[str, deque[dict[str, str]]]):
    """
    A class to manage chat data for a Telegram bot.

    Inherits from defaultdict with keys as chat IDs and values as deques of messages.
    """

    def __init__(
        self, maxlen: int | None = None, storage_path: Union[Path, str] = "data.json"
    ):
        """
        Initialize the Data object.

        Args:
            maxlen (int | None): Maximum length of the deque for each chat.
            storage_path (str): Path to the storage file.
        """

        self._maxlen = maxlen
        super().__init__(self._constant_factory())
        self.storage_path = Path(storage_path)
        self._load_data()
        self.bot_id = int(
            CONFIG.get("telegram", dict()).get("bot_token", "").split(":")[0]
        )
        self._secret = CONFIG.get("telegram", dict()).get("secret", "秘密")

    def _constant_factory(self) -> Callable[[], deque[dict[str, str]]]:
        """
        Create a factory function that returns a deque with a system message.

        Returns:
            Callable[[], deque[dict[str, str]]]: A factory function.
        """
        return lambda: deque(
            [{"role": "system", "content": ""}],
            maxlen=self._maxlen + 1 if self._maxlen else None,
        )

    def _load_data(self) -> None:
        """
        Load data from the storage file.
        """
        if self.storage_path.exists():
            with self.storage_path.open("r") as f:
                portalocker.lock(f, portalocker.LOCK_SH)
                for chat_id, messages in load(f).items():
                    self[chat_id] = deque(messages)

    async def _save_data(self) -> None:
        """
        Save data to the storage file.
        """
        with self.storage_path.open("w") as f:
            portalocker.lock(f, portalocker.LOCK_EX)
            dump({k: list(v) for k, v in self.items()}, f)

    async def _get_peer_id(self, event) -> str:
        try:
            peer_id: str = str(get_peer_id(event.message.peer_id))
        except AttributeError as _:
            try:
                peer_id = str(get_peer_id(event.peer))
            except AttributeError as _:
                try:
                    peer_id = f"-200{event.channel_id}"
                except AttributeError as _:
                    try:
                        peer_id = f"-200{event.chat_id}"
                    except AttributeError as _:
                        peer_id = str(event.users[0].id)
        match event.__class__.__name__:
            case "UpdateNewMessage" | "UpdateEditMessage":
                peer_id = str(get_peer_id(event.message.peer_id))
        return peer_id

    async def system(
        self, event: events.NewMessage.Event | events.MessageEdited.Event | events.Raw
    ) -> None:
        """
        Add or update the system message for a chat.

        Args:
            event (events.NewMessage.Event): The event containing chat information.
        """
        peer_id = await self._get_peer_id(event)
        self[peer_id][0] = {
            "role": "system",
            "content": system_prompt.format(secret=self._secret, chat=peer_id),
        }
        await self._save_data()

    async def user(
        self,
        event,
    ) -> None:
        """
        Add a user message to the chat.

        Args:
            event (events.NewMessage.Event | events.MessageEdited.Event): The event containing message information.
        """
        peer_id = await self._get_peer_id(event)
        if not self[peer_id]:
            self[peer_id].append({"role": "system", "content": ""})
        self[peer_id].append({"role": "user", "content": str(event)})
        await self.system(event)

    async def assistant(self, event) -> None:
        """
        Add an assistant message to the chat.

        Args:
            event (events.NewMessage.Event): The event containing message information.
        """
        self[await self._get_peer_id(event)].append(
            {"role": "assistant", "content": str(event)}
        )

    async def tool(self, event, tool_call_id, result) -> None:
        """
        Add a tool message to the chat.

        Args:
            event (events.NewMessage.Event): The event containing message information.
            result: The result of the tool.
        """
        self[await self._get_peer_id(event)].append(
            {
                "role": "tool",
                "tool_call_id": tool_call_id,
                "content": str(result),
            }
        )

    async def get_data(self, chat_id: int) -> list[dict[str, str]]:
        """
        Get the data for a specific chat.

        Args:
            chat_id (int): The ID of the chat.

        Returns:
            list[dict[str, str]]: A list of messages in the chat.
        """
        return list(self.get(str(chat_id), []))

    async def import_from_archive(self, file):
        # unpack_archive()
        # TODO: 从客户端导出压缩包导入历史
        pass
