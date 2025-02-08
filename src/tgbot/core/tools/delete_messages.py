from __future__ import annotations

from typing import List

from pydantic import BaseModel, Field

from . import register_tool


@register_tool(name="delete_messages")
class DeleteMessages(BaseModel):
    message_ids: List = Field(..., description="The IDs to be deleted.")
