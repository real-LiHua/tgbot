from ...tl.tlobject import TLObject as TLObject
from _typeshed import Incomplete
from datetime import datetime

class CollectibleInfo(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    purchase_date: Incomplete
    currency: Incomplete
    amount: Incomplete
    crypto_currency: Incomplete
    crypto_amount: Incomplete
    url: Incomplete
    def __init__(self, purchase_date: datetime | None, currency: str, amount: int, crypto_currency: str, crypto_amount: int, url: str) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...
