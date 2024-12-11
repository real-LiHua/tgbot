from ..tl import types as types
from .common import name_inner_event as name_inner_event
from .newmessage import NewMessage as NewMessage
from _typeshed import Incomplete

class MessageEdited(NewMessage):
    @classmethod
    def build(cls, update, others: Incomplete | None = None, self_id: Incomplete | None = None): ...
    class Event(NewMessage.Event): ...
