from ...tl.tlobject import TLObject as TLObject, TLRequest as TLRequest
from ...tl.types import TypeInputFileLocation as TypeInputFileLocation, TypeInputWebFileLocation as TypeInputWebFileLocation
from _typeshed import Incomplete
from datetime import datetime as datetime

class GetCdnFileRequest(TLRequest):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    file_token: Incomplete
    offset: Incomplete
    limit: Incomplete
    def __init__(self, file_token: bytes, offset: int, limit: int) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class GetCdnFileHashesRequest(TLRequest):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    file_token: Incomplete
    offset: Incomplete
    def __init__(self, file_token: bytes, offset: int) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class GetFileRequest(TLRequest):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    location: Incomplete
    offset: Incomplete
    limit: Incomplete
    precise: Incomplete
    cdn_supported: Incomplete
    def __init__(self, location: TypeInputFileLocation, offset: int, limit: int, precise: bool | None = None, cdn_supported: bool | None = None) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class GetFileHashesRequest(TLRequest):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    location: Incomplete
    offset: Incomplete
    def __init__(self, location: TypeInputFileLocation, offset: int) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class GetWebFileRequest(TLRequest):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    location: Incomplete
    offset: Incomplete
    limit: Incomplete
    def __init__(self, location: TypeInputWebFileLocation, offset: int, limit: int) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class ReuploadCdnFileRequest(TLRequest):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    file_token: Incomplete
    request_token: Incomplete
    def __init__(self, file_token: bytes, request_token: bytes) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class SaveBigFilePartRequest(TLRequest):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    file_id: Incomplete
    file_part: Incomplete
    file_total_parts: Incomplete
    bytes: Incomplete
    def __init__(self, file_id: int, file_part: int, file_total_parts: int, bytes: bytes) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class SaveFilePartRequest(TLRequest):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    file_id: Incomplete
    file_part: Incomplete
    bytes: Incomplete
    def __init__(self, file_id: int, file_part: int, bytes: bytes) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...
