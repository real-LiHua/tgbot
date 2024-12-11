from ...tl.tlobject import TLObject as TLObject
from ...tl.types import TypeUser as TypeUser
from ...tl.types.auth import TypeAuthorization as TypeAuthorization, TypeCodeType as TypeCodeType, TypeSentCodeType as TypeSentCodeType
from ...tl.types.help import TypeTermsOfService as TypeTermsOfService
from _typeshed import Incomplete
from datetime import datetime

class Authorization(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    user: Incomplete
    setup_password_required: Incomplete
    otherwise_relogin_days: Incomplete
    tmp_sessions: Incomplete
    future_auth_token: Incomplete
    def __init__(self, user: TypeUser, setup_password_required: bool | None = None, otherwise_relogin_days: int | None = None, tmp_sessions: int | None = None, future_auth_token: bytes | None = None) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class AuthorizationSignUpRequired(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    terms_of_service: Incomplete
    def __init__(self, terms_of_service: TypeTermsOfService | None = None) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class CodeTypeCall(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class CodeTypeFlashCall(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class CodeTypeFragmentSms(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class CodeTypeMissedCall(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class CodeTypeSms(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class ExportedAuthorization(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    id: Incomplete
    bytes: Incomplete
    def __init__(self, id: int, bytes: bytes) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class LoggedOut(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    future_auth_token: Incomplete
    def __init__(self, future_auth_token: bytes | None = None) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class LoginToken(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    expires: Incomplete
    token: Incomplete
    def __init__(self, expires: datetime | None, token: bytes) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class LoginTokenMigrateTo(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    dc_id: Incomplete
    token: Incomplete
    def __init__(self, dc_id: int, token: bytes) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class LoginTokenSuccess(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    authorization: Incomplete
    def __init__(self, authorization: TypeAuthorization) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class PasswordRecovery(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    email_pattern: Incomplete
    def __init__(self, email_pattern: str) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class SentCode(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    type: Incomplete
    phone_code_hash: Incomplete
    next_type: Incomplete
    timeout: Incomplete
    def __init__(self, type: TypeSentCodeType, phone_code_hash: str, next_type: TypeCodeType | None = None, timeout: int | None = None) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class SentCodeSuccess(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    authorization: Incomplete
    def __init__(self, authorization: TypeAuthorization) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class SentCodeTypeApp(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    length: Incomplete
    def __init__(self, length: int) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class SentCodeTypeCall(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    length: Incomplete
    def __init__(self, length: int) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class SentCodeTypeEmailCode(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    email_pattern: Incomplete
    length: Incomplete
    apple_signin_allowed: Incomplete
    google_signin_allowed: Incomplete
    reset_available_period: Incomplete
    reset_pending_date: Incomplete
    def __init__(self, email_pattern: str, length: int, apple_signin_allowed: bool | None = None, google_signin_allowed: bool | None = None, reset_available_period: int | None = None, reset_pending_date: datetime | None = None) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class SentCodeTypeFirebaseSms(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    length: Incomplete
    nonce: Incomplete
    play_integrity_project_id: Incomplete
    play_integrity_nonce: Incomplete
    receipt: Incomplete
    push_timeout: Incomplete
    def __init__(self, length: int, nonce: bytes | None = None, play_integrity_project_id: int | None = None, play_integrity_nonce: bytes | None = None, receipt: str | None = None, push_timeout: int | None = None) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class SentCodeTypeFlashCall(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    pattern: Incomplete
    def __init__(self, pattern: str) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class SentCodeTypeFragmentSms(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    url: Incomplete
    length: Incomplete
    def __init__(self, url: str, length: int) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class SentCodeTypeMissedCall(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    prefix: Incomplete
    length: Incomplete
    def __init__(self, prefix: str, length: int) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class SentCodeTypeSetUpEmailRequired(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    apple_signin_allowed: Incomplete
    google_signin_allowed: Incomplete
    def __init__(self, apple_signin_allowed: bool | None = None, google_signin_allowed: bool | None = None) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class SentCodeTypeSms(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    length: Incomplete
    def __init__(self, length: int) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class SentCodeTypeSmsPhrase(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    beginning: Incomplete
    def __init__(self, beginning: str | None = None) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class SentCodeTypeSmsWord(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    beginning: Incomplete
    def __init__(self, beginning: str | None = None) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...
