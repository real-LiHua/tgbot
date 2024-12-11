from ...tl.tlobject import TLObject as TLObject, TLRequest as TLRequest
from _typeshed import Incomplete
from datetime import datetime as datetime

class FinishJobRequest(TLRequest):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    job_id: Incomplete
    error: Incomplete
    def __init__(self, job_id: str, error: str | None = None) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class GetSmsJobRequest(TLRequest):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    job_id: Incomplete
    def __init__(self, job_id: str) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class GetStatusRequest(TLRequest):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class IsEligibleToJoinRequest(TLRequest):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class JoinRequest(TLRequest):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class LeaveRequest(TLRequest):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class UpdateSettingsRequest(TLRequest):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    allow_international: Incomplete
    def __init__(self, allow_international: bool | None = None) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...
