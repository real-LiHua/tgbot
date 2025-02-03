from singleton_decorator import singleton

tools = []


@singleton
def Tool(x: dict = dict()):
    """
    Singleton function to add a tool configuration to the tools list.

    Args:
        x (dict): Tool configuration dictionary. Defaults to an empty dictionary.
    """
    if x:
        tools.append(x)


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
