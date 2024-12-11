from . import authenticator as authenticator
from .. import helpers as helpers, utils as utils
from ..crypto import AuthKey as AuthKey
from ..errors import AuthKeyNotFound as AuthKeyNotFound, BadMessageError as BadMessageError, InvalidBufferError as InvalidBufferError, SecurityError as SecurityError, TypeNotFoundError as TypeNotFoundError, rpc_message_to_error as rpc_message_to_error
from ..extensions import BinaryReader as BinaryReader
from ..extensions.messagepacker import MessagePacker as MessagePacker
from ..helpers import retry_range as retry_range
from ..tl.core import GzipPacked as GzipPacked, MessageContainer as MessageContainer, RpcResult as RpcResult
from ..tl.functions import DestroyAuthKeyRequest as DestroyAuthKeyRequest, DestroySessionRequest as DestroySessionRequest, PingRequest as PingRequest
from ..tl.functions.auth import LogOutRequest as LogOutRequest
from ..tl.tlobject import TLRequest as TLRequest
from ..tl.types import BadMsgNotification as BadMsgNotification, BadServerSalt as BadServerSalt, DestroyAuthKeyFail as DestroyAuthKeyFail, DestroyAuthKeyNone as DestroyAuthKeyNone, DestroyAuthKeyOk as DestroyAuthKeyOk, DestroySessionNone as DestroySessionNone, DestroySessionOk as DestroySessionOk, FutureSalts as FutureSalts, MsgDetailedInfo as MsgDetailedInfo, MsgNewDetailedInfo as MsgNewDetailedInfo, MsgResendReq as MsgResendReq, MsgsAck as MsgsAck, MsgsAllInfo as MsgsAllInfo, MsgsStateInfo as MsgsStateInfo, MsgsStateReq as MsgsStateReq, NewSessionCreated as NewSessionCreated, Pong as Pong, upload as upload
from .mtprotoplainsender import MTProtoPlainSender as MTProtoPlainSender
from .mtprotostate import MTProtoState as MTProtoState
from .requeststate import RequestState as RequestState
from _typeshed import Incomplete

class MTProtoSender:
    auth_key: Incomplete
    def __init__(self, auth_key, *, loggers, retries: int = 5, delay: int = 1, auto_reconnect: bool = True, connect_timeout: Incomplete | None = None, auth_key_callback: Incomplete | None = None, updates_queue: Incomplete | None = None, auto_reconnect_callback: Incomplete | None = None) -> None: ...
    async def connect(self, connection): ...
    def is_connected(self): ...
    async def disconnect(self) -> None: ...
    def send(self, request, ordered: bool = False): ...
    @property
    def disconnected(self): ...
