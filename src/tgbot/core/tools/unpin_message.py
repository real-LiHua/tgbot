from pydantic import BaseModel, Field

from . import register_tool


@register_tool(name="unpin_message")
class UnpinMessage(BaseModel):
    message: int = Field(
        ...,
        description="Message ID, can be obtained from the Telegram message link, e.g., https://t.me/{chat_id}/{message_id}",
    )
