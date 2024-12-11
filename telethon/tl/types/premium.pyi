from ...tl.tlobject import TLObject as TLObject
from ...tl.types import TypeBoost as TypeBoost, TypeChat as TypeChat, TypeMyBoost as TypeMyBoost, TypePrepaidGiveaway as TypePrepaidGiveaway, TypeStatsPercentValue as TypeStatsPercentValue, TypeUser as TypeUser
from _typeshed import Incomplete
from datetime import datetime as datetime

class BoostsList(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    count: Incomplete
    boosts: Incomplete
    users: Incomplete
    next_offset: Incomplete
    def __init__(self, count: int, boosts: list['TypeBoost'], users: list['TypeUser'], next_offset: str | None = None) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class BoostsStatus(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    level: Incomplete
    current_level_boosts: Incomplete
    boosts: Incomplete
    boost_url: Incomplete
    my_boost: Incomplete
    gift_boosts: Incomplete
    next_level_boosts: Incomplete
    premium_audience: Incomplete
    prepaid_giveaways: Incomplete
    my_boost_slots: Incomplete
    def __init__(self, level: int, current_level_boosts: int, boosts: int, boost_url: str, my_boost: bool | None = None, gift_boosts: int | None = None, next_level_boosts: int | None = None, premium_audience: TypeStatsPercentValue | None = None, prepaid_giveaways: list['TypePrepaidGiveaway'] | None = None, my_boost_slots: list[int] | None = None) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class MyBoosts(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    my_boosts: Incomplete
    chats: Incomplete
    users: Incomplete
    def __init__(self, my_boosts: list['TypeMyBoost'], chats: list['TypeChat'], users: list['TypeUser']) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...
