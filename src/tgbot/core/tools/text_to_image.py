from typing import Optional

from pydantic import BaseModel, Field

from . import register_tool


@register_tool(name="images")
class Images(BaseModel):
    prompt: str = Field(..., description="A text description of the desired image(s)")
    size: Optional[str] = Field(
        ...,
        description="The size of the generated images.",
    )
