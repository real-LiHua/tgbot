from __future__ import annotations

from typing import Optional

from openai import pydantic_function_tool
from pydantic import BaseModel, Field

from . import Tool


@Tool
@pydantic_function_tool
class pin_message(BaseModel):
    message: int = Field(..., description="消息ID，可从Telegram消息链接获取")
    notify: Optional[bool] = Field(
        None, description="Whether the pin should notify people or not."
    )
