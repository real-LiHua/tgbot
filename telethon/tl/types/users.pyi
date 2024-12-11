from ...tl.tlobject import TLObject as TLObject
from ...tl.types import TypeChat as TypeChat, TypeUser as TypeUser, TypeUserFull as TypeUserFull
from _typeshed import Incomplete
from datetime import datetime as datetime

class UserFull(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    full_user: Incomplete
    chats: Incomplete
    users: Incomplete
    def __init__(self, full_user: TypeUserFull, chats: list['TypeChat'], users: list['TypeUser']) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...
