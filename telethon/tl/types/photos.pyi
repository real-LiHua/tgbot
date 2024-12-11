from ...tl.tlobject import TLObject as TLObject
from ...tl.types import TypePhoto as TypePhoto, TypeUser as TypeUser
from _typeshed import Incomplete
from datetime import datetime as datetime

class Photo(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    photo: Incomplete
    users: Incomplete
    def __init__(self, photo: TypePhoto, users: list['TypeUser']) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class Photos(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    photos: Incomplete
    users: Incomplete
    def __init__(self, photos: list['TypePhoto'], users: list['TypeUser']) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class PhotosSlice(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    count: Incomplete
    photos: Incomplete
    users: Incomplete
    def __init__(self, count: int, photos: list['TypePhoto'], users: list['TypeUser']) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...
