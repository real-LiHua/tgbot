from __future__ import annotations

from typing import Optional

from openai import pydantic_function_tool
from pydantic import BaseModel, Field

from . import Tool


@Tool
@pydantic_function_tool
class send_message(BaseModel):
    message: str = Field(
        ...,
        description="The message to be sent, or another message object to resend.The maximum length for a message is 35,000 bytes or 4,096 characters. Longer messages will not be sliced automatically, and you should slice them manually if the text to send is longer than said length.",
    )
    reply_to: Optional[int] = Field(
        None,
        description="消息ID，可从Telegram消息链接获取, 例如：https://t.me/{chat_id}/{message_id}",
    )
    link_preview: Optional[bool] = Field(
        None, description="Should the link preview be shown?"
    )
    silent: Optional[bool] = Field(
        None,
        description="Whether the message should notify people in a broadcast channel or not. Defaults to False, which means it will notify them. Set it to True to alter this behaviour.",
    )
    next_function: Optional[str] = Field(None, description="下一个要调用函数的名称")
