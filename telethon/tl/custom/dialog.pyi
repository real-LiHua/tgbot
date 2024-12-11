from . import Draft as Draft
from .. import TLObject as TLObject, functions as functions, types as types
from ... import utils as utils
from _typeshed import Incomplete

class Dialog:
    dialog: Incomplete
    pinned: Incomplete
    folder_id: Incomplete
    archived: Incomplete
    message: Incomplete
    date: Incomplete
    entity: Incomplete
    input_entity: Incomplete
    id: Incomplete
    name: Incomplete
    unread_count: Incomplete
    unread_mentions_count: Incomplete
    draft: Incomplete
    is_user: Incomplete
    is_group: Incomplete
    is_channel: Incomplete
    def __init__(self, client, dialog, entities, message) -> None: ...
    async def send_message(self, *args, **kwargs): ...
    async def delete(self, revoke: bool = False) -> None: ...
    async def archive(self, folder: int = 1): ...
    def to_dict(self): ...
    def stringify(self): ...
