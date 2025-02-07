from __future__ import annotations

from typing import Optional

from openai import pydantic_function_tool
from pydantic import BaseModel, Field

from . import Tool


@Tool
@pydantic_function_tool
class images(BaseModel):
    prompt: str = Field(..., description="A text description of the desired image(s)")
    size: Optional[str] = Field(
        ...,
        description="The size of the generated images.",
    )
