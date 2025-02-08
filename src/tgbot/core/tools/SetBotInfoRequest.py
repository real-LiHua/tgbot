from typing import Optional

from pydantic import BaseModel, Field

from . import register_tool


@register_tool
class SetBotInfoRequest(BaseModel):
    lang_code: str = Field(..., description="lang code")
    name: Optional[str] = Field(
        None,
        description="Your name. This argument defaults to `None` and can be omitted.",
    )
    about: Optional[str] = Field(
        None,
        description="Information about you. This argument defaults to `None` and can be omitted.",
    )
    description: Optional[str] = Field(
        None,
        description="A description of you. This argument defaults to `None` and can be omitted.",
    )
