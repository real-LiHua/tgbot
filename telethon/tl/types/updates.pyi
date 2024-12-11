from ...tl.tlobject import TLObject as TLObject
from ...tl.types import TypeChat as TypeChat, TypeDialog as TypeDialog, TypeEncryptedMessage as TypeEncryptedMessage, TypeMessage as TypeMessage, TypeUpdate as TypeUpdate, TypeUser as TypeUser
from ...tl.types.updates import TypeState as TypeState
from _typeshed import Incomplete
from datetime import datetime

class ChannelDifference(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    pts: Incomplete
    new_messages: Incomplete
    other_updates: Incomplete
    chats: Incomplete
    users: Incomplete
    final: Incomplete
    timeout: Incomplete
    def __init__(self, pts: int, new_messages: list['TypeMessage'], other_updates: list['TypeUpdate'], chats: list['TypeChat'], users: list['TypeUser'], final: bool | None = None, timeout: int | None = None) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class ChannelDifferenceEmpty(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    pts: Incomplete
    final: Incomplete
    timeout: Incomplete
    def __init__(self, pts: int, final: bool | None = None, timeout: int | None = None) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class ChannelDifferenceTooLong(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    dialog: Incomplete
    messages: Incomplete
    chats: Incomplete
    users: Incomplete
    final: Incomplete
    timeout: Incomplete
    def __init__(self, dialog: TypeDialog, messages: list['TypeMessage'], chats: list['TypeChat'], users: list['TypeUser'], final: bool | None = None, timeout: int | None = None) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class Difference(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    new_messages: Incomplete
    new_encrypted_messages: Incomplete
    other_updates: Incomplete
    chats: Incomplete
    users: Incomplete
    state: Incomplete
    def __init__(self, new_messages: list['TypeMessage'], new_encrypted_messages: list['TypeEncryptedMessage'], other_updates: list['TypeUpdate'], chats: list['TypeChat'], users: list['TypeUser'], state: TypeState) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class DifferenceEmpty(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    date: Incomplete
    seq: Incomplete
    def __init__(self, date: datetime | None, seq: int) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class DifferenceSlice(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    new_messages: Incomplete
    new_encrypted_messages: Incomplete
    other_updates: Incomplete
    chats: Incomplete
    users: Incomplete
    intermediate_state: Incomplete
    def __init__(self, new_messages: list['TypeMessage'], new_encrypted_messages: list['TypeEncryptedMessage'], other_updates: list['TypeUpdate'], chats: list['TypeChat'], users: list['TypeUser'], intermediate_state: TypeState) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class DifferenceTooLong(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    pts: Incomplete
    def __init__(self, pts: int) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class State(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    pts: Incomplete
    qts: Incomplete
    date: Incomplete
    seq: Incomplete
    unread_count: Incomplete
    def __init__(self, pts: int, qts: int, date: datetime | None, seq: int, unread_count: int) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...
