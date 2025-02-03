from __future__ import annotations

from typing import List

from openai import pydantic_function_tool
from pydantic import BaseModel, Field

from . import Tool


@Tool
@pydantic_function_tool
class DeleteMessages(BaseModel):
    message_ids: List = Field(..., description="The IDs to be deleted.")
