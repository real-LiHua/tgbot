from __future__ import annotations

from typing import Optional

from openai import pydantic_function_tool
from pydantic import BaseModel, Field

from . import Tool


@Tool
@pydantic_function_tool
class edit_admin(BaseModel):
    user: int = Field(..., description="用户ID")
    change_info: Optional[bool] = Field(
        None, description="Whether the user will be able to change info."
    )
    post_messages: Optional[bool] = Field(
        None,
        description="Whether the user will be able to post in the channel. This will only work in broadcast channels.",
    )
    edit_messages: Optional[bool] = Field(
        None,
        description="Whether the user will be able to edit messages in the channel. This will only work in broadcast channels.",
    )
    delete_messages: Optional[bool] = Field(
        None, description="Whether the user will be able to delete messages."
    )
    ban_users: Optional[bool] = Field(
        None, description="Whether the user will be able to ban users."
    )
    invite_users: Optional[bool] = Field(
        None, description="Whether the user will be able to invite users."
    )
    pin_messages: Optional[bool] = Field(
        None, description="Whether the user will be able to pin messages."
    )
    add_admins: Optional[bool] = Field(
        None, description="Whether the user will be able to add admins."
    )
    anonymous: Optional[bool] = Field(
        None,
        description="Whether the user will remain anonymous when sending messages. The sender of the anonymous messages becomes the group itself. Note: Users may be able to identify the anonymous admin by its custom title, so additional care is needed when using both anonymous and custom titles. For example, if multiple anonymous admins share the same title, users won’t be able to distinguish them.",
    )
    title: Optional[str] = Field(
        None,
        description="The custom title (also known as “rank”) to show for this admin. This text will be shown instead of the “admin” badge. This will only work in channels and megagroups. When left unspecified or empty, the default localized “admin” badge will be shown.",
    )
    next_function: Optional[str] = Field(None, description="下一个要调用函数的名称")
