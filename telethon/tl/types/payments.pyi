from ...tl.tlobject import TLObject as TLObject
from ...tl.types import TypeBankCardOpenUrl as TypeBankCardOpenUrl, TypeChat as TypeChat, TypeDataJSON as TypeDataJSON, TypeInvoice as TypeInvoice, TypePaymentFormMethod as TypePaymentFormMethod, TypePaymentRequestedInfo as TypePaymentRequestedInfo, TypePaymentSavedCredentials as TypePaymentSavedCredentials, TypePeer as TypePeer, TypeShippingOption as TypeShippingOption, TypeStarGift as TypeStarGift, TypeStarsRevenueStatus as TypeStarsRevenueStatus, TypeStarsSubscription as TypeStarsSubscription, TypeStarsTransaction as TypeStarsTransaction, TypeStatsGraph as TypeStatsGraph, TypeUpdates as TypeUpdates, TypeUser as TypeUser, TypeUserStarGift as TypeUserStarGift, TypeWebDocument as TypeWebDocument
from _typeshed import Incomplete
from datetime import datetime

class BankCardData(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    title: Incomplete
    open_urls: Incomplete
    def __init__(self, title: str, open_urls: list['TypeBankCardOpenUrl']) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class CheckedGiftCode(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    date: Incomplete
    months: Incomplete
    chats: Incomplete
    users: Incomplete
    via_giveaway: Incomplete
    from_id: Incomplete
    giveaway_msg_id: Incomplete
    to_id: Incomplete
    used_date: Incomplete
    def __init__(self, date: datetime | None, months: int, chats: list['TypeChat'], users: list['TypeUser'], via_giveaway: bool | None = None, from_id: TypePeer | None = None, giveaway_msg_id: int | None = None, to_id: int | None = None, used_date: datetime | None = None) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class ExportedInvoice(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    url: Incomplete
    def __init__(self, url: str) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class GiveawayInfo(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    start_date: Incomplete
    participating: Incomplete
    preparing_results: Incomplete
    joined_too_early_date: Incomplete
    admin_disallowed_chat_id: Incomplete
    disallowed_country: Incomplete
    def __init__(self, start_date: datetime | None, participating: bool | None = None, preparing_results: bool | None = None, joined_too_early_date: datetime | None = None, admin_disallowed_chat_id: int | None = None, disallowed_country: str | None = None) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class GiveawayInfoResults(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    start_date: Incomplete
    finish_date: Incomplete
    winners_count: Incomplete
    winner: Incomplete
    refunded: Incomplete
    gift_code_slug: Incomplete
    stars_prize: Incomplete
    activated_count: Incomplete
    def __init__(self, start_date: datetime | None, finish_date: datetime | None, winners_count: int, winner: bool | None = None, refunded: bool | None = None, gift_code_slug: str | None = None, stars_prize: int | None = None, activated_count: int | None = None) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class PaymentForm(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    form_id: Incomplete
    bot_id: Incomplete
    title: Incomplete
    description: Incomplete
    invoice: Incomplete
    provider_id: Incomplete
    url: Incomplete
    users: Incomplete
    can_save_credentials: Incomplete
    password_missing: Incomplete
    photo: Incomplete
    native_provider: Incomplete
    native_params: Incomplete
    additional_methods: Incomplete
    saved_info: Incomplete
    saved_credentials: Incomplete
    def __init__(self, form_id: int, bot_id: int, title: str, description: str, invoice: TypeInvoice, provider_id: int, url: str, users: list['TypeUser'], can_save_credentials: bool | None = None, password_missing: bool | None = None, photo: TypeWebDocument | None = None, native_provider: str | None = None, native_params: TypeDataJSON | None = None, additional_methods: list['TypePaymentFormMethod'] | None = None, saved_info: TypePaymentRequestedInfo | None = None, saved_credentials: list['TypePaymentSavedCredentials'] | None = None) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class PaymentFormStarGift(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    form_id: Incomplete
    invoice: Incomplete
    def __init__(self, form_id: int, invoice: TypeInvoice) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class PaymentFormStars(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    form_id: Incomplete
    bot_id: Incomplete
    title: Incomplete
    description: Incomplete
    invoice: Incomplete
    users: Incomplete
    photo: Incomplete
    def __init__(self, form_id: int, bot_id: int, title: str, description: str, invoice: TypeInvoice, users: list['TypeUser'], photo: TypeWebDocument | None = None) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class PaymentReceipt(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    date: Incomplete
    bot_id: Incomplete
    provider_id: Incomplete
    title: Incomplete
    description: Incomplete
    invoice: Incomplete
    currency: Incomplete
    total_amount: Incomplete
    credentials_title: Incomplete
    users: Incomplete
    photo: Incomplete
    info: Incomplete
    shipping: Incomplete
    tip_amount: Incomplete
    def __init__(self, date: datetime | None, bot_id: int, provider_id: int, title: str, description: str, invoice: TypeInvoice, currency: str, total_amount: int, credentials_title: str, users: list['TypeUser'], photo: TypeWebDocument | None = None, info: TypePaymentRequestedInfo | None = None, shipping: TypeShippingOption | None = None, tip_amount: int | None = None) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class PaymentReceiptStars(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    date: Incomplete
    bot_id: Incomplete
    title: Incomplete
    description: Incomplete
    invoice: Incomplete
    currency: Incomplete
    total_amount: Incomplete
    transaction_id: Incomplete
    users: Incomplete
    photo: Incomplete
    def __init__(self, date: datetime | None, bot_id: int, title: str, description: str, invoice: TypeInvoice, currency: str, total_amount: int, transaction_id: str, users: list['TypeUser'], photo: TypeWebDocument | None = None) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class PaymentResult(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    updates: Incomplete
    def __init__(self, updates: TypeUpdates) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class PaymentVerificationNeeded(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    url: Incomplete
    def __init__(self, url: str) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class SavedInfo(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    has_saved_credentials: Incomplete
    saved_info: Incomplete
    def __init__(self, has_saved_credentials: bool | None = None, saved_info: TypePaymentRequestedInfo | None = None) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class StarGifts(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    hash: Incomplete
    gifts: Incomplete
    def __init__(self, hash: int, gifts: list['TypeStarGift']) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class StarGiftsNotModified(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class StarsRevenueAdsAccountUrl(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    url: Incomplete
    def __init__(self, url: str) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class StarsRevenueStats(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    revenue_graph: Incomplete
    status: Incomplete
    usd_rate: Incomplete
    def __init__(self, revenue_graph: TypeStatsGraph, status: TypeStarsRevenueStatus, usd_rate: float) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class StarsRevenueWithdrawalUrl(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    url: Incomplete
    def __init__(self, url: str) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class StarsStatus(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    balance: Incomplete
    chats: Incomplete
    users: Incomplete
    subscriptions: Incomplete
    subscriptions_next_offset: Incomplete
    subscriptions_missing_balance: Incomplete
    history: Incomplete
    next_offset: Incomplete
    def __init__(self, balance: int, chats: list['TypeChat'], users: list['TypeUser'], subscriptions: list['TypeStarsSubscription'] | None = None, subscriptions_next_offset: str | None = None, subscriptions_missing_balance: int | None = None, history: list['TypeStarsTransaction'] | None = None, next_offset: str | None = None) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class UserStarGifts(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    count: Incomplete
    gifts: Incomplete
    users: Incomplete
    next_offset: Incomplete
    def __init__(self, count: int, gifts: list['TypeUserStarGift'], users: list['TypeUser'], next_offset: str | None = None) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class ValidatedRequestedInfo(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    id: Incomplete
    shipping_options: Incomplete
    def __init__(self, id: str | None = None, shipping_options: list['TypeShippingOption'] | None = None) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...
