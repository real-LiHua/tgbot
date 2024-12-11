from ...tl.tlobject import TLObject as TLObject
from ...tl.types import TypeFileHash as TypeFileHash
from ...tl.types.storage import TypeFileType as TypeFileType
from _typeshed import Incomplete
from datetime import datetime as datetime

class CdnFile(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    bytes: Incomplete
    def __init__(self, bytes: bytes) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class CdnFileReuploadNeeded(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    request_token: Incomplete
    def __init__(self, request_token: bytes) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class File(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    type: Incomplete
    mtime: Incomplete
    bytes: Incomplete
    def __init__(self, type: TypeFileType, mtime: int, bytes: bytes) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class FileCdnRedirect(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    dc_id: Incomplete
    file_token: Incomplete
    encryption_key: Incomplete
    encryption_iv: Incomplete
    file_hashes: Incomplete
    def __init__(self, dc_id: int, file_token: bytes, encryption_key: bytes, encryption_iv: bytes, file_hashes: list['TypeFileHash']) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class WebFile(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    size: Incomplete
    mime_type: Incomplete
    file_type: Incomplete
    mtime: Incomplete
    bytes: Incomplete
    def __init__(self, size: int, mime_type: str, file_type: TypeFileType, mtime: int, bytes: bytes) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...
