from ...tl.tlobject import TLObject as TLObject, TLRequest as TLRequest
from ...tl.types import TypeChannelMessagesFilter as TypeChannelMessagesFilter, TypeInputChannel as TypeInputChannel
from _typeshed import Incomplete
from datetime import datetime

class GetChannelDifferenceRequest(TLRequest):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    channel: Incomplete
    filter: Incomplete
    pts: Incomplete
    limit: Incomplete
    force: Incomplete
    def __init__(self, channel: TypeInputChannel, filter: TypeChannelMessagesFilter, pts: int, limit: int, force: bool | None = None) -> None: ...
    async def resolve(self, client, utils) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class GetDifferenceRequest(TLRequest):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    pts: Incomplete
    date: Incomplete
    qts: Incomplete
    pts_limit: Incomplete
    pts_total_limit: Incomplete
    qts_limit: Incomplete
    def __init__(self, pts: int, date: datetime | None, qts: int, pts_limit: int | None = None, pts_total_limit: int | None = None, qts_limit: int | None = None) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class GetStateRequest(TLRequest):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...
