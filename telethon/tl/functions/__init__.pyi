from . import account as account, auth as auth, bots as bots, channels as channels, chatlists as chatlists, contacts as contacts, folders as folders, fragment as fragment, help as help, langpack as langpack, messages as messages, payments as payments, phone as phone, photos as photos, premium as premium, smsjobs as smsjobs, stats as stats, stickers as stickers, stories as stories, updates as updates, upload as upload, users as users
from ...tl.tlobject import TLRequest
from ...tl.types import TypeInputClientProxy as TypeInputClientProxy, TypeJSONValue as TypeJSONValue, TypeMessageRange as TypeMessageRange, TypeType as TypeType, TypeX as TypeX
from _typeshed import Incomplete
from datetime import datetime as datetime

class DestroyAuthKeyRequest(TLRequest):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class DestroySessionRequest(TLRequest):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    session_id: Incomplete
    def __init__(self, session_id: int) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class GetFutureSaltsRequest(TLRequest):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    num: Incomplete
    def __init__(self, num: int) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class InitConnectionRequest(TLRequest):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    api_id: Incomplete
    device_model: Incomplete
    system_version: Incomplete
    app_version: Incomplete
    system_lang_code: Incomplete
    lang_pack: Incomplete
    lang_code: Incomplete
    query: Incomplete
    proxy: Incomplete
    params: Incomplete
    def __init__(self, api_id: int, device_model: str, system_version: str, app_version: str, system_lang_code: str, lang_pack: str, lang_code: str, query: TypeX, proxy: TypeInputClientProxy | None = None, params: TypeJSONValue | None = None) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class InvokeAfterMsgRequest(TLRequest):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    msg_id: Incomplete
    query: Incomplete
    def __init__(self, msg_id: int, query: TypeX) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class InvokeAfterMsgsRequest(TLRequest):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    msg_ids: Incomplete
    query: Incomplete
    def __init__(self, msg_ids: list[int], query: TypeX) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class InvokeWithApnsSecretRequest(TLRequest):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    nonce: Incomplete
    secret: Incomplete
    query: Incomplete
    def __init__(self, nonce: str, secret: str, query: TypeX) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class InvokeWithBusinessConnectionRequest(TLRequest):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    connection_id: Incomplete
    query: Incomplete
    def __init__(self, connection_id: str, query: TypeX) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class InvokeWithGooglePlayIntegrityRequest(TLRequest):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    nonce: Incomplete
    token: Incomplete
    query: Incomplete
    def __init__(self, nonce: str, token: str, query: TypeX) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class InvokeWithLayerRequest(TLRequest):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    layer: Incomplete
    query: Incomplete
    def __init__(self, layer: int, query: TypeX) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class InvokeWithMessagesRangeRequest(TLRequest):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    range: Incomplete
    query: Incomplete
    def __init__(self, range: TypeMessageRange, query: TypeX) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class InvokeWithTakeoutRequest(TLRequest):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    takeout_id: Incomplete
    query: Incomplete
    def __init__(self, takeout_id: int, query: TypeX) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class InvokeWithoutUpdatesRequest(TLRequest):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    query: Incomplete
    def __init__(self, query: TypeX) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class PingRequest(TLRequest):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    ping_id: Incomplete
    def __init__(self, ping_id: int) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class PingDelayDisconnectRequest(TLRequest):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    ping_id: Incomplete
    disconnect_delay: Incomplete
    def __init__(self, ping_id: int, disconnect_delay: int) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class ReqDHParamsRequest(TLRequest):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    nonce: Incomplete
    server_nonce: Incomplete
    p: Incomplete
    q: Incomplete
    public_key_fingerprint: Incomplete
    encrypted_data: Incomplete
    def __init__(self, nonce: int, server_nonce: int, p: bytes, q: bytes, public_key_fingerprint: int, encrypted_data: bytes) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class ReqPqRequest(TLRequest):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    nonce: Incomplete
    def __init__(self, nonce: int) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class ReqPqMultiRequest(TLRequest):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    nonce: Incomplete
    def __init__(self, nonce: int) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class RpcDropAnswerRequest(TLRequest):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    req_msg_id: Incomplete
    def __init__(self, req_msg_id: int) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class SetClientDHParamsRequest(TLRequest):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    nonce: Incomplete
    server_nonce: Incomplete
    encrypted_data: Incomplete
    def __init__(self, nonce: int, server_nonce: int, encrypted_data: bytes) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...
