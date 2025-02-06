from __future__ import annotations

from typing import Optional

from openai import pydantic_function_tool
from pydantic import BaseModel, Field

from . import Tool


@Tool
@pydantic_function_tool
class KickParticipant(BaseModel):
    user: int = Field(..., description="The user to kick.")
    next_function: Optional[str] = Field(None, description="下一个要调用函数的名称")
