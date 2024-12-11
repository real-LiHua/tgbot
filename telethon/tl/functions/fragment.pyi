from ...tl.tlobject import TLObject as TLObject, TLRequest as TLRequest
from ...tl.types import TypeInputCollectible as TypeInputCollectible
from _typeshed import Incomplete
from datetime import datetime as datetime

class GetCollectibleInfoRequest(TLRequest):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    collectible: Incomplete
    def __init__(self, collectible: TypeInputCollectible) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...
