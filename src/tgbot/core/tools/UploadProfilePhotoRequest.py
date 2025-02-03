from __future__ import annotations

from openai import pydantic_function_tool
from pydantic import BaseModel, Field

from . import Tool


@Tool
@pydantic_function_tool
class UploadProfilePhotoRequest(BaseModel):
    file: int = Field(..., description="已使用函数的列表下标，用于从中获取文件对象")
