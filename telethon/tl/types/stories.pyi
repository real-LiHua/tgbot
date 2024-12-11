from ...tl.tlobject import TLObject as TLObject
from ...tl.types import TypeChat as TypeChat, TypeFoundStory as TypeFoundStory, TypePeerStories as TypePeerStories, TypeStoriesStealthMode as TypeStoriesStealthMode, TypeStoryItem as TypeStoryItem, TypeStoryReaction as TypeStoryReaction, TypeStoryView as TypeStoryView, TypeStoryViews as TypeStoryViews, TypeUser as TypeUser
from _typeshed import Incomplete
from datetime import datetime as datetime

class AllStories(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    count: Incomplete
    state: Incomplete
    peer_stories: Incomplete
    chats: Incomplete
    users: Incomplete
    stealth_mode: Incomplete
    has_more: Incomplete
    def __init__(self, count: int, state: str, peer_stories: list['TypePeerStories'], chats: list['TypeChat'], users: list['TypeUser'], stealth_mode: TypeStoriesStealthMode, has_more: bool | None = None) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class AllStoriesNotModified(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    state: Incomplete
    stealth_mode: Incomplete
    def __init__(self, state: str, stealth_mode: TypeStoriesStealthMode) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class FoundStories(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    count: Incomplete
    stories: Incomplete
    chats: Incomplete
    users: Incomplete
    next_offset: Incomplete
    def __init__(self, count: int, stories: list['TypeFoundStory'], chats: list['TypeChat'], users: list['TypeUser'], next_offset: str | None = None) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class PeerStories(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    stories: Incomplete
    chats: Incomplete
    users: Incomplete
    def __init__(self, stories: TypePeerStories, chats: list['TypeChat'], users: list['TypeUser']) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class Stories(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    count: Incomplete
    stories: Incomplete
    chats: Incomplete
    users: Incomplete
    pinned_to_top: Incomplete
    def __init__(self, count: int, stories: list['TypeStoryItem'], chats: list['TypeChat'], users: list['TypeUser'], pinned_to_top: list[int] | None = None) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class StoryReactionsList(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    count: Incomplete
    reactions: Incomplete
    chats: Incomplete
    users: Incomplete
    next_offset: Incomplete
    def __init__(self, count: int, reactions: list['TypeStoryReaction'], chats: list['TypeChat'], users: list['TypeUser'], next_offset: str | None = None) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class StoryViews(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    views: Incomplete
    users: Incomplete
    def __init__(self, views: list['TypeStoryViews'], users: list['TypeUser']) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class StoryViewsList(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    count: Incomplete
    views_count: Incomplete
    forwards_count: Incomplete
    reactions_count: Incomplete
    views: Incomplete
    chats: Incomplete
    users: Incomplete
    next_offset: Incomplete
    def __init__(self, count: int, views_count: int, forwards_count: int, reactions_count: int, views: list['TypeStoryView'], chats: list['TypeChat'], users: list['TypeUser'], next_offset: str | None = None) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...
