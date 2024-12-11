from ...tl.tlobject import TLObject as TLObject
from ...tl.types import TypeAccessPointRule as TypeAccessPointRule, TypeChat as TypeChat, TypeDataJSON as TypeDataJSON, TypeDocument as TypeDocument, TypeJSONValue as TypeJSONValue, TypeMessageEntity as TypeMessageEntity, TypePeer as TypePeer, TypePremiumSubscriptionOption as TypePremiumSubscriptionOption, TypeRecentMeUrl as TypeRecentMeUrl, TypeTimezone as TypeTimezone, TypeUser as TypeUser
from ...tl.types.help import TypeCountry as TypeCountry, TypeCountryCode as TypeCountryCode, TypePeerColorOption as TypePeerColorOption, TypePeerColorSet as TypePeerColorSet, TypeTermsOfService as TypeTermsOfService
from _typeshed import Incomplete
from datetime import datetime

class AppConfig(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    hash: Incomplete
    config: Incomplete
    def __init__(self, hash: int, config: TypeJSONValue) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class AppConfigNotModified(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class AppUpdate(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    id: Incomplete
    version: Incomplete
    text: Incomplete
    entities: Incomplete
    can_not_skip: Incomplete
    document: Incomplete
    url: Incomplete
    sticker: Incomplete
    def __init__(self, id: int, version: str, text: str, entities: list['TypeMessageEntity'], can_not_skip: bool | None = None, document: TypeDocument | None = None, url: str | None = None, sticker: TypeDocument | None = None) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class ConfigSimple(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    date: Incomplete
    expires: Incomplete
    rules: Incomplete
    def __init__(self, date: datetime | None, expires: datetime | None, rules: list['TypeAccessPointRule']) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class CountriesList(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    countries: Incomplete
    hash: Incomplete
    def __init__(self, countries: list['TypeCountry'], hash: int) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class CountriesListNotModified(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class Country(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    iso2: Incomplete
    default_name: Incomplete
    country_codes: Incomplete
    hidden: Incomplete
    name: Incomplete
    def __init__(self, iso2: str, default_name: str, country_codes: list['TypeCountryCode'], hidden: bool | None = None, name: str | None = None) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class CountryCode(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    country_code: Incomplete
    prefixes: Incomplete
    patterns: Incomplete
    def __init__(self, country_code: str, prefixes: list[str] | None = None, patterns: list[str] | None = None) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class DeepLinkInfo(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    message: Incomplete
    update_app: Incomplete
    entities: Incomplete
    def __init__(self, message: str, update_app: bool | None = None, entities: list['TypeMessageEntity'] | None = None) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class DeepLinkInfoEmpty(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class InviteText(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    message: Incomplete
    def __init__(self, message: str) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class NoAppUpdate(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class PassportConfig(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    hash: Incomplete
    countries_langs: Incomplete
    def __init__(self, hash: int, countries_langs: TypeDataJSON) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class PassportConfigNotModified(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class PeerColorOption(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    color_id: Incomplete
    hidden: Incomplete
    colors: Incomplete
    dark_colors: Incomplete
    channel_min_level: Incomplete
    group_min_level: Incomplete
    def __init__(self, color_id: int, hidden: bool | None = None, colors: TypePeerColorSet | None = None, dark_colors: TypePeerColorSet | None = None, channel_min_level: int | None = None, group_min_level: int | None = None) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class PeerColorProfileSet(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    palette_colors: Incomplete
    bg_colors: Incomplete
    story_colors: Incomplete
    def __init__(self, palette_colors: list[int], bg_colors: list[int], story_colors: list[int]) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class PeerColorSet(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    colors: Incomplete
    def __init__(self, colors: list[int]) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class PeerColors(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    hash: Incomplete
    colors: Incomplete
    def __init__(self, hash: int, colors: list['TypePeerColorOption']) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class PeerColorsNotModified(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class PremiumPromo(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    status_text: Incomplete
    status_entities: Incomplete
    video_sections: Incomplete
    videos: Incomplete
    period_options: Incomplete
    users: Incomplete
    def __init__(self, status_text: str, status_entities: list['TypeMessageEntity'], video_sections: list[str], videos: list['TypeDocument'], period_options: list['TypePremiumSubscriptionOption'], users: list['TypeUser']) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class PromoData(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    expires: Incomplete
    peer: Incomplete
    chats: Incomplete
    users: Incomplete
    proxy: Incomplete
    psa_type: Incomplete
    psa_message: Incomplete
    def __init__(self, expires: datetime | None, peer: TypePeer, chats: list['TypeChat'], users: list['TypeUser'], proxy: bool | None = None, psa_type: str | None = None, psa_message: str | None = None) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class PromoDataEmpty(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    expires: Incomplete
    def __init__(self, expires: datetime | None) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class RecentMeUrls(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    urls: Incomplete
    chats: Incomplete
    users: Incomplete
    def __init__(self, urls: list['TypeRecentMeUrl'], chats: list['TypeChat'], users: list['TypeUser']) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class Support(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    phone_number: Incomplete
    user: Incomplete
    def __init__(self, phone_number: str, user: TypeUser) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class SupportName(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    name: Incomplete
    def __init__(self, name: str) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class TermsOfService(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    id: Incomplete
    text: Incomplete
    entities: Incomplete
    popup: Incomplete
    min_age_confirm: Incomplete
    def __init__(self, id: TypeDataJSON, text: str, entities: list['TypeMessageEntity'], popup: bool | None = None, min_age_confirm: int | None = None) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class TermsOfServiceUpdate(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    expires: Incomplete
    terms_of_service: Incomplete
    def __init__(self, expires: datetime | None, terms_of_service: TypeTermsOfService) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class TermsOfServiceUpdateEmpty(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    expires: Incomplete
    def __init__(self, expires: datetime | None) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class TimezonesList(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    timezones: Incomplete
    hash: Incomplete
    def __init__(self, timezones: list['TypeTimezone'], hash: int) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class TimezonesListNotModified(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class UserInfo(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    message: Incomplete
    entities: Incomplete
    author: Incomplete
    date: Incomplete
    def __init__(self, message: str, entities: list['TypeMessageEntity'], author: str, date: datetime | None) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class UserInfoEmpty(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...
