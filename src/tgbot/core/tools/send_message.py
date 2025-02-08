from typing import Optional

from openai import pydantic_function_tool
from pydantic import BaseModel, Field

from . import register_tool


@register_tool(name="send_message")
class SendMessage(BaseModel):
    message: str = Field(
        ...,
        description="The message to be sent, or another message object to resend.The maximum length for a message is 35,000 bytes or 4,096 characters. Longer messages will not be sliced automatically, and you should slice them manually if the text to send is longer than said length.",
    )
    reply_to: Optional[int] = Field(
        None,
        description="Message ID, can be obtained from the Telegram message link, for example: https://t.me/{chat_id}/{message_id}",
    )
    link_preview: Optional[bool] = Field(
        None, description="Should the link preview be shown?"
    )
    silent: Optional[bool] = Field(
        None,
        description="Whether the message should notify people in a broadcast channel or not. Defaults to False, which means it will notify them. Set it to True to alter this behaviour.",
    )
