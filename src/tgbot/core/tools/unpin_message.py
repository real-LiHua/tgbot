from __future__ import annotations

from typing import Optional

from openai import pydantic_function_tool
from pydantic import BaseModel, Field

from . import Tool


@Tool
@pydantic_function_tool
class unpin_message(BaseModel):
    message: int = Field(
        ...,
        description="消息ID，可从Telegram消息链接获取, 例如：https://t.me/{chat_id}/{message_id}",
    )
