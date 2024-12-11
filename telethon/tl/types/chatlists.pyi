from ...tl.tlobject import TLObject as TLObject
from ...tl.types import TypeChat as TypeChat, TypeDialogFilter as TypeDialogFilter, TypeExportedChatlistInvite as TypeExportedChatlistInvite, TypePeer as TypePeer, TypeUser as TypeUser
from _typeshed import Incomplete
from datetime import datetime as datetime

class ChatlistInvite(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    title: Incomplete
    peers: Incomplete
    chats: Incomplete
    users: Incomplete
    emoticon: Incomplete
    def __init__(self, title: str, peers: list['TypePeer'], chats: list['TypeChat'], users: list['TypeUser'], emoticon: str | None = None) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class ChatlistInviteAlready(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    filter_id: Incomplete
    missing_peers: Incomplete
    already_peers: Incomplete
    chats: Incomplete
    users: Incomplete
    def __init__(self, filter_id: int, missing_peers: list['TypePeer'], already_peers: list['TypePeer'], chats: list['TypeChat'], users: list['TypeUser']) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class ChatlistUpdates(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    missing_peers: Incomplete
    chats: Incomplete
    users: Incomplete
    def __init__(self, missing_peers: list['TypePeer'], chats: list['TypeChat'], users: list['TypeUser']) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class ExportedChatlistInvite(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    filter: Incomplete
    invite: Incomplete
    def __init__(self, filter: TypeDialogFilter, invite: TypeExportedChatlistInvite) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class ExportedInvites(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    invites: Incomplete
    chats: Incomplete
    users: Incomplete
    def __init__(self, invites: list['TypeExportedChatlistInvite'], chats: list['TypeChat'], users: list['TypeUser']) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...
