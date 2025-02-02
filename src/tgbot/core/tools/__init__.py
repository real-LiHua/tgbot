from openai import pydantic_function_tool

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

tools = [
    pydantic_function_tool(SearXNG.SearXNG),
    pydantic_function_tool(SetBotInfoRequest.SetBotInfoRequest),
    pydantic_function_tool(delete_messages.DeleteMessages),
    pydantic_function_tool(edit_message.EditMessage),
    pydantic_function_tool(kick_participant.KickParticipant),
    pydantic_function_tool(send_file.SendFile),
    pydantic_function_tool(text_to_image.images),
    pydantic_function_tool(SendReactionRequest.SendReactionRequest),
    pydantic_function_tool(UploadProfilePhotoRequest.UploadProfilePhotoRequest),
    pydantic_function_tool(edit_admin.EditAdmin),
    pydantic_function_tool(forward_messages.ForwardMessages),
    pydantic_function_tool(pin_message.PinMessage),
    pydantic_function_tool(send_message.SendMessage),
    pydantic_function_tool(unpin_message.UnpinMessage),
]
