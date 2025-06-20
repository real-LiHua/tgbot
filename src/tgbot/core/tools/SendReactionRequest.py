from __future__ import annotations

from enum import Enum
from typing import Optional

from pydantic import BaseModel, Field

from . import register_tool


class Reaction(Enum):
    field_ = "👍"
    field__1 = "👎"
    field__2 = "❤"
    field__3 = "🔥"
    field__4 = "🥰"
    field__5 = "👏"
    field__6 = "😁"
    field__7 = "🤔"
    field__8 = "🤯"
    field__9 = "😱"
    field__10 = "🤬"
    field__11 = "😢"
    field__12 = "🎉"
    field__13 = "🤩"
    field__14 = "🤮"
    field__15 = "💩"
    field__16 = "🙏"
    field__17 = "👌"
    field__18 = "🕊"
    field__19 = "🤡"
    field__20 = "🥱"
    field__21 = "🥴"
    field__22 = "😍"
    field__23 = "🐳"
    field___ = "❤‍🔥"
    field__24 = "🌚"
    field__25 = "🌭"
    field__26 = "💯"
    field__27 = "🤣"
    field__28 = "⚡"
    field__29 = "🍌"
    field__30 = "🏆"
    field__31 = "💔"
    field__32 = "🤨"
    field__33 = "😐"
    field__34 = "🍓"
    field__35 = "🍾"
    field__36 = "💋"
    field__37 = "🖕"
    field__38 = "😈"
    field__39 = "😴"
    field__40 = "😭"
    field__41 = "🤓"
    field__42 = "👻"
    field____1 = "👨‍💻"
    field__43 = "👀"
    field__44 = "🎃"
    field__45 = "🙈"
    field__46 = "😇"
    field__47 = "😨"
    field__48 = "🤝"
    field__49 = "✍"
    field__50 = "🤗"
    field__51 = "🫡"
    field__52 = "🎅"
    field__53 = "🎄"
    field__54 = "☃"
    field__55 = "💅"
    field__56 = "🤪"
    field__57 = "🗿"
    field__58 = "🆒"
    field__59 = "💘"
    field__60 = "🙉"
    field__61 = "🦄"
    field__62 = "😘"
    field__63 = "💊"
    field__64 = "🙊"
    field__65 = "😎"
    field__66 = "👾"
    field____2 = "🤷‍♂"
    field__67 = "🤷"
    field____3 = "🤷‍♀"
    field__68 = "😡"


@register_tool
class SendReactionRequest(BaseModel):
    msg_id: int = Field(
        ...,
        description="Message ID, can be obtained from the Telegram message link, for example: https://t.me/{chat_id}/{message_id}",
    )
    reaction: Optional[Reaction] = Field(
        None,
        description="A JSON-serialized list of reaction types to set on the message. A custom emoji reaction can be used if it is either already present on the message or explicitly allowed by chat administrators.",
    )
