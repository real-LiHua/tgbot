from ...tl.tlobject import TLObject as TLObject, TLRequest as TLRequest
from _typeshed import Incomplete
from datetime import datetime as datetime

class GetDifferenceRequest(TLRequest):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    lang_pack: Incomplete
    lang_code: Incomplete
    from_version: Incomplete
    def __init__(self, lang_pack: str, lang_code: str, from_version: int) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class GetLangPackRequest(TLRequest):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    lang_pack: Incomplete
    lang_code: Incomplete
    def __init__(self, lang_pack: str, lang_code: str) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class GetLanguageRequest(TLRequest):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    lang_pack: Incomplete
    lang_code: Incomplete
    def __init__(self, lang_pack: str, lang_code: str) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class GetLanguagesRequest(TLRequest):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    lang_pack: Incomplete
    def __init__(self, lang_pack: str) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class GetStringsRequest(TLRequest):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    lang_pack: Incomplete
    lang_code: Incomplete
    keys: Incomplete
    def __init__(self, lang_pack: str, lang_code: str, keys: list[str]) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...
