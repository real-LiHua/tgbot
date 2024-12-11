from ...tl.tlobject import TLObject as TLObject
from _typeshed import Incomplete
from datetime import datetime

class EligibleToJoin(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    terms_url: Incomplete
    monthly_sent_sms: Incomplete
    def __init__(self, terms_url: str, monthly_sent_sms: int) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class Status(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    recent_sent: Incomplete
    recent_since: Incomplete
    recent_remains: Incomplete
    total_sent: Incomplete
    total_since: Incomplete
    terms_url: Incomplete
    allow_international: Incomplete
    last_gift_slug: Incomplete
    def __init__(self, recent_sent: int, recent_since: datetime | None, recent_remains: int, total_sent: int, total_since: datetime | None, terms_url: str, allow_international: bool | None = None, last_gift_slug: str | None = None) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...
