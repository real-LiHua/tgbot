from ...tl.tlobject import TLObject as TLObject
from ...tl.types import TypeChat as TypeChat, TypeGroupCall as TypeGroupCall, TypeGroupCallParticipant as TypeGroupCallParticipant, TypeGroupCallStreamChannel as TypeGroupCallStreamChannel, TypePeer as TypePeer, TypePhoneCall as TypePhoneCall, TypeUser as TypeUser
from _typeshed import Incomplete
from datetime import datetime as datetime

class ExportedGroupCallInvite(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    link: Incomplete
    def __init__(self, link: str) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class GroupCall(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    call: Incomplete
    participants: Incomplete
    participants_next_offset: Incomplete
    chats: Incomplete
    users: Incomplete
    def __init__(self, call: TypeGroupCall, participants: list['TypeGroupCallParticipant'], participants_next_offset: str, chats: list['TypeChat'], users: list['TypeUser']) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class GroupCallStreamChannels(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    channels: Incomplete
    def __init__(self, channels: list['TypeGroupCallStreamChannel']) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class GroupCallStreamRtmpUrl(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    url: Incomplete
    key: Incomplete
    def __init__(self, url: str, key: str) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class GroupParticipants(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    count: Incomplete
    participants: Incomplete
    next_offset: Incomplete
    chats: Incomplete
    users: Incomplete
    version: Incomplete
    def __init__(self, count: int, participants: list['TypeGroupCallParticipant'], next_offset: str, chats: list['TypeChat'], users: list['TypeUser'], version: int) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class JoinAsPeers(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    peers: Incomplete
    chats: Incomplete
    users: Incomplete
    def __init__(self, peers: list['TypePeer'], chats: list['TypeChat'], users: list['TypeUser']) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class PhoneCall(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    phone_call: Incomplete
    users: Incomplete
    def __init__(self, phone_call: TypePhoneCall, users: list['TypeUser']) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...
