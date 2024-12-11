from ...tl.tlobject import TLObject as TLObject
from ...tl.types import TypeAuthorization as TypeAuthorization, TypeAutoDownloadSettings as TypeAutoDownloadSettings, TypeAutoSaveException as TypeAutoSaveException, TypeAutoSaveSettings as TypeAutoSaveSettings, TypeBusinessChatLink as TypeBusinessChatLink, TypeChat as TypeChat, TypeConnectedBot as TypeConnectedBot, TypeDocument as TypeDocument, TypeEmojiStatus as TypeEmojiStatus, TypeMessageEntity as TypeMessageEntity, TypePasswordKdfAlgo as TypePasswordKdfAlgo, TypePeer as TypePeer, TypePrivacyRule as TypePrivacyRule, TypeSecurePasswordKdfAlgo as TypeSecurePasswordKdfAlgo, TypeSecureRequiredType as TypeSecureRequiredType, TypeSecureSecretSettings as TypeSecureSecretSettings, TypeSecureValue as TypeSecureValue, TypeSecureValueError as TypeSecureValueError, TypeTheme as TypeTheme, TypeUser as TypeUser, TypeWallPaper as TypeWallPaper, TypeWebAuthorization as TypeWebAuthorization
from ...tl.types.auth import TypeSentCode as TypeSentCode
from _typeshed import Incomplete
from datetime import datetime

class AuthorizationForm(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    required_types: Incomplete
    values: Incomplete
    errors: Incomplete
    users: Incomplete
    privacy_policy_url: Incomplete
    def __init__(self, required_types: list['TypeSecureRequiredType'], values: list['TypeSecureValue'], errors: list['TypeSecureValueError'], users: list['TypeUser'], privacy_policy_url: str | None = None) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class Authorizations(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    authorization_ttl_days: Incomplete
    authorizations: Incomplete
    def __init__(self, authorization_ttl_days: int, authorizations: list['TypeAuthorization']) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class AutoDownloadSettings(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    low: Incomplete
    medium: Incomplete
    high: Incomplete
    def __init__(self, low: TypeAutoDownloadSettings, medium: TypeAutoDownloadSettings, high: TypeAutoDownloadSettings) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class AutoSaveSettings(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    users_settings: Incomplete
    chats_settings: Incomplete
    broadcasts_settings: Incomplete
    exceptions: Incomplete
    chats: Incomplete
    users: Incomplete
    def __init__(self, users_settings: TypeAutoSaveSettings, chats_settings: TypeAutoSaveSettings, broadcasts_settings: TypeAutoSaveSettings, exceptions: list['TypeAutoSaveException'], chats: list['TypeChat'], users: list['TypeUser']) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class BusinessChatLinks(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    links: Incomplete
    chats: Incomplete
    users: Incomplete
    def __init__(self, links: list['TypeBusinessChatLink'], chats: list['TypeChat'], users: list['TypeUser']) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class ConnectedBots(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    connected_bots: Incomplete
    users: Incomplete
    def __init__(self, connected_bots: list['TypeConnectedBot'], users: list['TypeUser']) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class ContentSettings(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    sensitive_enabled: Incomplete
    sensitive_can_change: Incomplete
    def __init__(self, sensitive_enabled: bool | None = None, sensitive_can_change: bool | None = None) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class EmailVerified(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    email: Incomplete
    def __init__(self, email: str) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class EmailVerifiedLogin(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    email: Incomplete
    sent_code: Incomplete
    def __init__(self, email: str, sent_code: TypeSentCode) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class EmojiStatuses(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    hash: Incomplete
    statuses: Incomplete
    def __init__(self, hash: int, statuses: list['TypeEmojiStatus']) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class EmojiStatusesNotModified(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class Password(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    new_algo: Incomplete
    new_secure_algo: Incomplete
    secure_random: Incomplete
    has_recovery: Incomplete
    has_secure_values: Incomplete
    has_password: Incomplete
    current_algo: Incomplete
    srp_B: Incomplete
    srp_id: Incomplete
    hint: Incomplete
    email_unconfirmed_pattern: Incomplete
    pending_reset_date: Incomplete
    login_email_pattern: Incomplete
    def __init__(self, new_algo: TypePasswordKdfAlgo, new_secure_algo: TypeSecurePasswordKdfAlgo, secure_random: bytes, has_recovery: bool | None = None, has_secure_values: bool | None = None, has_password: bool | None = None, current_algo: TypePasswordKdfAlgo | None = None, srp_B: bytes | None = None, srp_id: int | None = None, hint: str | None = None, email_unconfirmed_pattern: str | None = None, pending_reset_date: datetime | None = None, login_email_pattern: str | None = None) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class PasswordInputSettings(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    new_algo: Incomplete
    new_password_hash: Incomplete
    hint: Incomplete
    email: Incomplete
    new_secure_settings: Incomplete
    def __init__(self, new_algo: TypePasswordKdfAlgo | None = None, new_password_hash: bytes | None = None, hint: str | None = None, email: str | None = None, new_secure_settings: TypeSecureSecretSettings | None = None) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class PasswordSettings(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    email: Incomplete
    secure_settings: Incomplete
    def __init__(self, email: str | None = None, secure_settings: TypeSecureSecretSettings | None = None) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class PrivacyRules(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    rules: Incomplete
    chats: Incomplete
    users: Incomplete
    def __init__(self, rules: list['TypePrivacyRule'], chats: list['TypeChat'], users: list['TypeUser']) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class ResetPasswordFailedWait(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    retry_date: Incomplete
    def __init__(self, retry_date: datetime | None) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class ResetPasswordOk(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class ResetPasswordRequestedWait(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    until_date: Incomplete
    def __init__(self, until_date: datetime | None) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class ResolvedBusinessChatLinks(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    peer: Incomplete
    message: Incomplete
    chats: Incomplete
    users: Incomplete
    entities: Incomplete
    def __init__(self, peer: TypePeer, message: str, chats: list['TypeChat'], users: list['TypeUser'], entities: list['TypeMessageEntity'] | None = None) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class SavedRingtone(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class SavedRingtoneConverted(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    document: Incomplete
    def __init__(self, document: TypeDocument) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class SavedRingtones(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    hash: Incomplete
    ringtones: Incomplete
    def __init__(self, hash: int, ringtones: list['TypeDocument']) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class SavedRingtonesNotModified(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class SentEmailCode(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    email_pattern: Incomplete
    length: Incomplete
    def __init__(self, email_pattern: str, length: int) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class Takeout(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    id: Incomplete
    def __init__(self, id: int) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class Themes(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    hash: Incomplete
    themes: Incomplete
    def __init__(self, hash: int, themes: list['TypeTheme']) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class ThemesNotModified(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class TmpPassword(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    tmp_password: Incomplete
    valid_until: Incomplete
    def __init__(self, tmp_password: bytes, valid_until: datetime | None) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class WallPapers(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    hash: Incomplete
    wallpapers: Incomplete
    def __init__(self, hash: int, wallpapers: list['TypeWallPaper']) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class WallPapersNotModified(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class WebAuthorizations(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    authorizations: Incomplete
    users: Incomplete
    def __init__(self, authorizations: list['TypeWebAuthorization'], users: list['TypeUser']) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...
