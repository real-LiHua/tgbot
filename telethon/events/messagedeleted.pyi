from ..tl import types as types
from .common import EventBuilder as EventBuilder, EventCommon as EventCommon, name_inner_event as name_inner_event
from _typeshed import Incomplete

class MessageDeleted(EventBuilder):
    @classmethod
    def build(cls, update, others: Incomplete | None = None, self_id: Incomplete | None = None): ...
    class Event(EventCommon):
        deleted_id: Incomplete
        deleted_ids: Incomplete
        def __init__(self, deleted_ids, peer) -> None: ...
