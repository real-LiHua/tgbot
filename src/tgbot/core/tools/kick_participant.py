from pydantic import BaseModel, Field

from . import register_tool


@register_tool(name="kick_participant")
class KickParticipant(BaseModel):
    user: int = Field(..., description="The user to kick.")
