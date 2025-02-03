from __future__ import annotations

from typing import List, Optional

from openai import pydantic_function_tool
from pydantic import BaseModel, Field

from . import Tool


@Tool
@pydantic_function_tool
class ForwardMessages(BaseModel):
    entity: int = Field(
        ..., description="To which entity the message(s) will be forwarded."
    )
    messages: List = Field(..., description="The messages integer IDs.")
    from_peer: int = Field(
        ...,
        description="If the given messages are integer IDs and not instances of the Message class, this must be specified in order for the forward to work. This parameter indicates the entity from which the messages should be forwarded.",
    )
    silent: Optional[bool] = Field(
        None,
        description="Whether the message should notify people in a broadcast channel or not. Defaults to False, which means it will notify them. Set it to True to alter this behaviour.",
    )
