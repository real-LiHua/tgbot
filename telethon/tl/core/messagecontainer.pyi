from ..tlobject import TLObject as TLObject
from .tlmessage import TLMessage as TLMessage
from _typeshed import Incomplete

class MessageContainer(TLObject):
    CONSTRUCTOR_ID: int
    MAXIMUM_SIZE: Incomplete
    MAXIMUM_LENGTH: int
    messages: Incomplete
    def __init__(self, messages) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...
