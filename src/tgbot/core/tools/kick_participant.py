from __future__ import annotations

from openai import pydantic_function_tool
from pydantic import BaseModel, Field

from . import Tool


@Tool
@pydantic_function_tool
class KickParticipant(BaseModel):
    user: int = Field(..., description="The user to kick.")
