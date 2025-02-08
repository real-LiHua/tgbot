from typing import Optional

from pydantic import BaseModel, Field

from . import register_tool


@register_tool(name="edit_message")
class EditMessage(BaseModel):
    message: int = Field(
        ...,
        description="Message ID, can be obtained from the Telegram message link, e.g., https://t.me/{chat_id}/{message_id}",
    )
    text: Optional[str] = Field(None, description="The new text of the message.")
    link_preview: Optional[bool] = Field(
        None, description="Should the link preview be shown?"
    )
