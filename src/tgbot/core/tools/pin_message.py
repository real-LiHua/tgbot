from typing import Optional

from pydantic import BaseModel, Field

from . import register_tool


@register_tool(name="pin_message")
class PinMessage(BaseModel):
    message: int = Field(
        ..., description="Message ID, can be obtained from the Telegram message link"
    )
    notify: Optional[bool] = Field(
        None, description="Whether the pin should notify people or not."
    )
