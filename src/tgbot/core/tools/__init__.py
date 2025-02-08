from openai import pydantic_function_tool

tools = []


def register_tool(func=None, name=None, description=None):
    """
    Singleton function to add a tool configuration to the tools list and apply pydantic_function_tool decorator.

    Args:
        func (callable, optional): The function to be registered as a tool. Defaults to None.
        name (str, optional): Name for the pydantic function tool. Defaults to None.
        description (str, optional): Description for the pydantic function tool. Defaults to None.

    Returns:
        callable: The original function if func is provided, otherwise the decorator.
    """

    if func is not None:
        tools.append(pydantic_function_tool(func))

    def decorator(func):
        tools.append(
            pydantic_function_tool(model=func, name=name, description=description)
        )

    return decorator


from . import SearXNG as _  # noqa
from . import SendReactionRequest as _  # noqa
from . import SetBotInfoRequest as _  # noqa
from . import UploadProfilePhotoRequest as _  # noqa
from . import delete_messages as _  # noqa
from . import edit_admin as _  # noqa
from . import edit_message as _  # noqa
from . import forward_messages as _  # noqa
from . import kick_participant as _  # noqa
from . import pin_message as _  # noqa
from . import send_file as _  # noqa
from . import send_message as _  # noqa
from . import text_to_image as _  # noqa
from . import unpin_message as _  # noqa
