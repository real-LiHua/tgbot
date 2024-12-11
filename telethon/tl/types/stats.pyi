from ...tl.tlobject import TLObject as TLObject
from ...tl.types import TypeBroadcastRevenueBalances as TypeBroadcastRevenueBalances, TypeBroadcastRevenueTransaction as TypeBroadcastRevenueTransaction, TypeChat as TypeChat, TypePostInteractionCounters as TypePostInteractionCounters, TypePublicForward as TypePublicForward, TypeStatsAbsValueAndPrev as TypeStatsAbsValueAndPrev, TypeStatsDateRangeDays as TypeStatsDateRangeDays, TypeStatsGraph as TypeStatsGraph, TypeStatsGroupTopAdmin as TypeStatsGroupTopAdmin, TypeStatsGroupTopInviter as TypeStatsGroupTopInviter, TypeStatsGroupTopPoster as TypeStatsGroupTopPoster, TypeStatsPercentValue as TypeStatsPercentValue, TypeUser as TypeUser
from _typeshed import Incomplete
from datetime import datetime as datetime

class BroadcastRevenueStats(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    top_hours_graph: Incomplete
    revenue_graph: Incomplete
    balances: Incomplete
    usd_rate: Incomplete
    def __init__(self, top_hours_graph: TypeStatsGraph, revenue_graph: TypeStatsGraph, balances: TypeBroadcastRevenueBalances, usd_rate: float) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class BroadcastRevenueTransactions(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    count: Incomplete
    transactions: Incomplete
    def __init__(self, count: int, transactions: list['TypeBroadcastRevenueTransaction']) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class BroadcastRevenueWithdrawalUrl(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    url: Incomplete
    def __init__(self, url: str) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class BroadcastStats(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    period: Incomplete
    followers: Incomplete
    views_per_post: Incomplete
    shares_per_post: Incomplete
    reactions_per_post: Incomplete
    views_per_story: Incomplete
    shares_per_story: Incomplete
    reactions_per_story: Incomplete
    enabled_notifications: Incomplete
    growth_graph: Incomplete
    followers_graph: Incomplete
    mute_graph: Incomplete
    top_hours_graph: Incomplete
    interactions_graph: Incomplete
    iv_interactions_graph: Incomplete
    views_by_source_graph: Incomplete
    new_followers_by_source_graph: Incomplete
    languages_graph: Incomplete
    reactions_by_emotion_graph: Incomplete
    story_interactions_graph: Incomplete
    story_reactions_by_emotion_graph: Incomplete
    recent_posts_interactions: Incomplete
    def __init__(self, period: TypeStatsDateRangeDays, followers: TypeStatsAbsValueAndPrev, views_per_post: TypeStatsAbsValueAndPrev, shares_per_post: TypeStatsAbsValueAndPrev, reactions_per_post: TypeStatsAbsValueAndPrev, views_per_story: TypeStatsAbsValueAndPrev, shares_per_story: TypeStatsAbsValueAndPrev, reactions_per_story: TypeStatsAbsValueAndPrev, enabled_notifications: TypeStatsPercentValue, growth_graph: TypeStatsGraph, followers_graph: TypeStatsGraph, mute_graph: TypeStatsGraph, top_hours_graph: TypeStatsGraph, interactions_graph: TypeStatsGraph, iv_interactions_graph: TypeStatsGraph, views_by_source_graph: TypeStatsGraph, new_followers_by_source_graph: TypeStatsGraph, languages_graph: TypeStatsGraph, reactions_by_emotion_graph: TypeStatsGraph, story_interactions_graph: TypeStatsGraph, story_reactions_by_emotion_graph: TypeStatsGraph, recent_posts_interactions: list['TypePostInteractionCounters']) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class MegagroupStats(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    period: Incomplete
    members: Incomplete
    messages: Incomplete
    viewers: Incomplete
    posters: Incomplete
    growth_graph: Incomplete
    members_graph: Incomplete
    new_members_by_source_graph: Incomplete
    languages_graph: Incomplete
    messages_graph: Incomplete
    actions_graph: Incomplete
    top_hours_graph: Incomplete
    weekdays_graph: Incomplete
    top_posters: Incomplete
    top_admins: Incomplete
    top_inviters: Incomplete
    users: Incomplete
    def __init__(self, period: TypeStatsDateRangeDays, members: TypeStatsAbsValueAndPrev, messages: TypeStatsAbsValueAndPrev, viewers: TypeStatsAbsValueAndPrev, posters: TypeStatsAbsValueAndPrev, growth_graph: TypeStatsGraph, members_graph: TypeStatsGraph, new_members_by_source_graph: TypeStatsGraph, languages_graph: TypeStatsGraph, messages_graph: TypeStatsGraph, actions_graph: TypeStatsGraph, top_hours_graph: TypeStatsGraph, weekdays_graph: TypeStatsGraph, top_posters: list['TypeStatsGroupTopPoster'], top_admins: list['TypeStatsGroupTopAdmin'], top_inviters: list['TypeStatsGroupTopInviter'], users: list['TypeUser']) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class MessageStats(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    views_graph: Incomplete
    reactions_by_emotion_graph: Incomplete
    def __init__(self, views_graph: TypeStatsGraph, reactions_by_emotion_graph: TypeStatsGraph) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class PublicForwards(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    count: Incomplete
    forwards: Incomplete
    chats: Incomplete
    users: Incomplete
    next_offset: Incomplete
    def __init__(self, count: int, forwards: list['TypePublicForward'], chats: list['TypeChat'], users: list['TypeUser'], next_offset: str | None = None) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class StoryStats(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    views_graph: Incomplete
    reactions_by_emotion_graph: Incomplete
    def __init__(self, views_graph: TypeStatsGraph, reactions_by_emotion_graph: TypeStatsGraph) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...
