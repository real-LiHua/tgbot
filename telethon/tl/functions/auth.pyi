from ...tl.tlobject import TLObject as TLObject, TLRequest as TLRequest
from ...tl.types import TypeCodeSettings as TypeCodeSettings, TypeEmailVerification as TypeEmailVerification, TypeInputCheckPasswordSRP as TypeInputCheckPasswordSRP
from ...tl.types.account import TypePasswordInputSettings as TypePasswordInputSettings
from _typeshed import Incomplete
from datetime import datetime

class AcceptLoginTokenRequest(TLRequest):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    token: Incomplete
    def __init__(self, token: bytes) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class BindTempAuthKeyRequest(TLRequest):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    perm_auth_key_id: Incomplete
    nonce: Incomplete
    expires_at: Incomplete
    encrypted_message: Incomplete
    def __init__(self, perm_auth_key_id: int, nonce: int, expires_at: datetime | None, encrypted_message: bytes) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class CancelCodeRequest(TLRequest):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    phone_number: Incomplete
    phone_code_hash: Incomplete
    def __init__(self, phone_number: str, phone_code_hash: str) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class CheckPasswordRequest(TLRequest):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    password: Incomplete
    def __init__(self, password: TypeInputCheckPasswordSRP) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class CheckRecoveryPasswordRequest(TLRequest):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    code: Incomplete
    def __init__(self, code: str) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class DropTempAuthKeysRequest(TLRequest):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    except_auth_keys: Incomplete
    def __init__(self, except_auth_keys: list[int]) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class ExportAuthorizationRequest(TLRequest):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    dc_id: Incomplete
    def __init__(self, dc_id: int) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class ExportLoginTokenRequest(TLRequest):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    api_id: Incomplete
    api_hash: Incomplete
    except_ids: Incomplete
    def __init__(self, api_id: int, api_hash: str, except_ids: list[int]) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class ImportAuthorizationRequest(TLRequest):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    id: Incomplete
    bytes: Incomplete
    def __init__(self, id: int, bytes: bytes) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class ImportBotAuthorizationRequest(TLRequest):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    flags: Incomplete
    api_id: Incomplete
    api_hash: Incomplete
    bot_auth_token: Incomplete
    def __init__(self, flags: int, api_id: int, api_hash: str, bot_auth_token: str) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class ImportLoginTokenRequest(TLRequest):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    token: Incomplete
    def __init__(self, token: bytes) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class ImportWebTokenAuthorizationRequest(TLRequest):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    api_id: Incomplete
    api_hash: Incomplete
    web_auth_token: Incomplete
    def __init__(self, api_id: int, api_hash: str, web_auth_token: str) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class LogOutRequest(TLRequest):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class RecoverPasswordRequest(TLRequest):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    code: Incomplete
    new_settings: Incomplete
    def __init__(self, code: str, new_settings: TypePasswordInputSettings | None = None) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class ReportMissingCodeRequest(TLRequest):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    phone_number: Incomplete
    phone_code_hash: Incomplete
    mnc: Incomplete
    def __init__(self, phone_number: str, phone_code_hash: str, mnc: str) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class RequestFirebaseSmsRequest(TLRequest):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    phone_number: Incomplete
    phone_code_hash: Incomplete
    safety_net_token: Incomplete
    play_integrity_token: Incomplete
    ios_push_secret: Incomplete
    def __init__(self, phone_number: str, phone_code_hash: str, safety_net_token: str | None = None, play_integrity_token: str | None = None, ios_push_secret: str | None = None) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class RequestPasswordRecoveryRequest(TLRequest):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class ResendCodeRequest(TLRequest):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    phone_number: Incomplete
    phone_code_hash: Incomplete
    reason: Incomplete
    def __init__(self, phone_number: str, phone_code_hash: str, reason: str | None = None) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class ResetAuthorizationsRequest(TLRequest):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class ResetLoginEmailRequest(TLRequest):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    phone_number: Incomplete
    phone_code_hash: Incomplete
    def __init__(self, phone_number: str, phone_code_hash: str) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class SendCodeRequest(TLRequest):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    phone_number: Incomplete
    api_id: Incomplete
    api_hash: Incomplete
    settings: Incomplete
    def __init__(self, phone_number: str, api_id: int, api_hash: str, settings: TypeCodeSettings) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class SignInRequest(TLRequest):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    phone_number: Incomplete
    phone_code_hash: Incomplete
    phone_code: Incomplete
    email_verification: Incomplete
    def __init__(self, phone_number: str, phone_code_hash: str, phone_code: str | None = None, email_verification: TypeEmailVerification | None = None) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class SignUpRequest(TLRequest):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    phone_number: Incomplete
    phone_code_hash: Incomplete
    first_name: Incomplete
    last_name: Incomplete
    no_joined_notifications: Incomplete
    def __init__(self, phone_number: str, phone_code_hash: str, first_name: str, last_name: str, no_joined_notifications: bool | None = None) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...
