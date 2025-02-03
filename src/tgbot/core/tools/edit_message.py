from __future__ import annotations

from typing import Optional

from openai import pydantic_function_tool
from pydantic import BaseModel, Field

from . import Tool


@Tool
@pydantic_function_tool
class EditMessage(BaseModel):
    message: int = Field(
        ...,
        description="消息ID，可从Telegram消息链接获取, 例如：https://t.me/{chat_id}/{message_id}",
    )
    text: Optional[str] = Field(None, description="The new text of the message.")
    link_preview: Optional[bool] = Field(
        None, description="Should the link preview be shown?"
    )
