from pydantic import BaseModel, Field

from . import register_tool


@register_tool
class UploadProfilePhotoRequest(BaseModel):
    file: int = Field(
        ...,
        description="Index of the used function list, used to get the file object from it",
    )
