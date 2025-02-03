class Tool(list):
    __obj = None

    def __new__(cls, flag=None):
        if not cls.__obj:
            cls.__obj = super().__new__(cls)
        return cls.__obj

    def __init__(self, c: dict = None):
        if c:
            self.append(c)


from . import SearXNG as _  # noqa
from . import SendReactionRequest as _
from . import SetBotInfoRequest as _
from . import UploadProfilePhotoRequest as _
from . import delete_messages as _
from . import edit_admin as _
from . import edit_message as _
from . import forward_messages as _
from . import kick_participant as _
from . import pin_message as _
from . import send_file as _
from . import send_message as _
from . import text_to_image as _
from . import unpin_message as _

tools = Tool()
