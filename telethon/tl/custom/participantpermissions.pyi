from .. import types as types
from _typeshed import Incomplete

class ParticipantPermissions:
    participant: Incomplete
    is_chat: Incomplete
    def __init__(self, participant, chat: bool) -> None: ...
    @property
    def is_admin(self): ...
    @property
    def is_creator(self): ...
    @property
    def has_default_permissions(self): ...
    @property
    def is_banned(self): ...
    @property
    def has_left(self): ...
    @property
    def add_admins(self): ...
    ban_users: Incomplete
    pin_messages: Incomplete
    invite_users: Incomplete
    delete_messages: Incomplete
    edit_messages: Incomplete
    post_messages: Incomplete
    change_info: Incomplete
    anonymous: Incomplete
    manage_call: Incomplete
