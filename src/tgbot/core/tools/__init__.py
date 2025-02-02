from typing import Type

from openai import pydantic_function_tool
from pydantic import BaseModel


class Tool(list):
    __obj = None

    def __new__(cls, flag=None):
        if not cls.__obj:
            cls.__obj = super().__new__(cls)
        return cls.__obj

    def __init__(self, c: Type[BaseModel] = None):
        if c:
            self.append(pydantic_function_tool(c))


from . import (
    SearXNG,
    SendReactionRequest,
    SetBotInfoRequest,
    UploadProfilePhotoRequest,
    delete_messages,
    edit_admin,
    edit_message,
    forward_messages,
    kick_participant,
    pin_message,
    send_file,
    send_message,
    text_to_image,
    unpin_message,
)

tools = Tool()
