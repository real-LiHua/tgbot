from .album import Album as Album
from .callbackquery import CallbackQuery as CallbackQuery
from .chataction import ChatAction as ChatAction
from .inlinequery import InlineQuery as InlineQuery
from .messagedeleted import MessageDeleted as MessageDeleted
from .messageedited import MessageEdited as MessageEdited
from .messageread import MessageRead as MessageRead
from .newmessage import NewMessage as NewMessage
from .raw import Raw as Raw
from .userupdate import UserUpdate as UserUpdate
from _typeshed import Incomplete

class StopPropagation(Exception): ...

def register(event: Incomplete | None = None): ...
def unregister(callback, event: Incomplete | None = None): ...
def is_handler(callback): ...
def list(callback): ...
