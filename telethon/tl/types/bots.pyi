from ...tl.tlobject import TLObject as TLObject
from ...tl.types import TypeBotPreviewMedia as TypeBotPreviewMedia, TypeUser as TypeUser
from _typeshed import Incomplete
from datetime import datetime as datetime

class BotInfo(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    name: Incomplete
    about: Incomplete
    description: Incomplete
    def __init__(self, name: str, about: str, description: str) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class PopularAppBots(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    users: Incomplete
    next_offset: Incomplete
    def __init__(self, users: list['TypeUser'], next_offset: str | None = None) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class PreviewInfo(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    media: Incomplete
    lang_codes: Incomplete
    def __init__(self, media: list['TypeBotPreviewMedia'], lang_codes: list[str]) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...
