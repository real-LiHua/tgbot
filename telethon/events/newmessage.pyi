from .. import utils as utils
from ..tl import types as types
from .common import EventBuilder as EventBuilder, EventCommon as EventCommon, name_inner_event as name_inner_event
from _typeshed import Incomplete

class NewMessage(EventBuilder):
    incoming: Incomplete
    outgoing: Incomplete
    from_users: Incomplete
    forwards: Incomplete
    pattern: Incomplete
    def __init__(self, chats: Incomplete | None = None, *, blacklist_chats: bool = False, func: Incomplete | None = None, incoming: Incomplete | None = None, outgoing: Incomplete | None = None, from_users: Incomplete | None = None, forwards: Incomplete | None = None, pattern: Incomplete | None = None) -> None: ...
    @classmethod
    def build(cls, update, others: Incomplete | None = None, self_id: Incomplete | None = None): ...
    def filter(self, event): ...
    class Event(EventCommon):
        pattern_match: Incomplete
        message: Incomplete
        def __init__(self, message) -> None: ...
        def __getattr__(self, item): ...
        def __setattr__(self, name, value) -> None: ...
