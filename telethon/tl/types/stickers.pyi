from ...tl.tlobject import TLObject as TLObject
from _typeshed import Incomplete
from datetime import datetime as datetime

class SuggestedShortName(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    short_name: Incomplete
    def __init__(self, short_name: str) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...
