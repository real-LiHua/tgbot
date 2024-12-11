from ...tl.tlobject import TLObject as TLObject
from ...tl.types import TypeChannelAdminLogEvent as TypeChannelAdminLogEvent, TypeChannelParticipant as TypeChannelParticipant, TypeChat as TypeChat, TypeSendAsPeer as TypeSendAsPeer, TypeSponsoredMessageReportOption as TypeSponsoredMessageReportOption, TypeUser as TypeUser
from _typeshed import Incomplete
from datetime import datetime as datetime

class AdminLogResults(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    events: Incomplete
    chats: Incomplete
    users: Incomplete
    def __init__(self, events: list['TypeChannelAdminLogEvent'], chats: list['TypeChat'], users: list['TypeUser']) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class ChannelParticipant(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    participant: Incomplete
    chats: Incomplete
    users: Incomplete
    def __init__(self, participant: TypeChannelParticipant, chats: list['TypeChat'], users: list['TypeUser']) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class ChannelParticipants(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    count: Incomplete
    participants: Incomplete
    chats: Incomplete
    users: Incomplete
    def __init__(self, count: int, participants: list['TypeChannelParticipant'], chats: list['TypeChat'], users: list['TypeUser']) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class ChannelParticipantsNotModified(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class SendAsPeers(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    peers: Incomplete
    chats: Incomplete
    users: Incomplete
    def __init__(self, peers: list['TypeSendAsPeer'], chats: list['TypeChat'], users: list['TypeUser']) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class SponsoredMessageReportResultAdsHidden(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class SponsoredMessageReportResultChooseOption(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    title: Incomplete
    options: Incomplete
    def __init__(self, title: str, options: list['TypeSponsoredMessageReportOption']) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class SponsoredMessageReportResultReported(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...
