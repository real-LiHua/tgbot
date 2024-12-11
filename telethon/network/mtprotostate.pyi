from ..crypto import AES as AES
from ..errors import InvalidBufferError as InvalidBufferError, SecurityError as SecurityError
from ..extensions import BinaryReader as BinaryReader
from ..tl.core import TLMessage as TLMessage
from ..tl.core.gzippacked import GzipPacked as GzipPacked
from ..tl.functions import InvokeAfterMsgRequest as InvokeAfterMsgRequest
from ..tl.tlobject import TLRequest as TLRequest
from ..tl.types import BadMsgNotification as BadMsgNotification, BadServerSalt as BadServerSalt
from _typeshed import Incomplete

MAX_RECENT_MSG_IDS: int
MSG_TOO_NEW_DELTA: int
MSG_TOO_OLD_DELTA: int
MAX_CONSECUTIVE_IGNORED: int

class _OpaqueRequest(TLRequest):
    data: Incomplete
    def __init__(self, data: bytes) -> None: ...

class MTProtoState:
    auth_key: Incomplete
    time_offset: int
    salt: int
    id: Incomplete
    def __init__(self, auth_key, loggers) -> None: ...
    def reset(self) -> None: ...
    def update_message_id(self, message) -> None: ...
    def write_data_as_message(self, buffer, data, content_related, *, after_id: Incomplete | None = None): ...
    def encrypt_message_data(self, data): ...
    def decrypt_message_data(self, body): ...
    def update_time_offset(self, correct_msg_id): ...
