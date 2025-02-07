from __future__ import annotations

from typing import List, Optional

from openai import pydantic_function_tool
from pydantic import BaseModel, Field

from . import Tool


@Tool
@pydantic_function_tool
class delete_messages(BaseModel):
    message_ids: List = Field(..., description="The IDs to be deleted.")
