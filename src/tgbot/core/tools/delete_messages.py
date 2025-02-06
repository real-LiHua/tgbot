from __future__ import annotations

from typing import List, Optional

from openai import pydantic_function_tool
from pydantic import BaseModel, Field

from . import Tool


@Tool
@pydantic_function_tool
class delete_messages(BaseModel):
    message_ids: List = Field(..., description="The IDs to be deleted.")
    next_function: Optional[str] = Field(None, description="下一个要调用函数的名称")
