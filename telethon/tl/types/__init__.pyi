from . import account as account, auth as auth, bots as bots, channels as channels, chatlists as chatlists, contacts as contacts, fragment as fragment, help as help, messages as messages, payments as payments, phone as phone, photos as photos, premium as premium, smsjobs as smsjobs, stats as stats, stickers as stickers, storage as storage, stories as stories, updates as updates, upload as upload, users as users
from ...tl.tlobject import TLObject
from ...tl.types import Typefuture_salt as Typefuture_salt
from _typeshed import Incomplete
from datetime import datetime

class AccessPointRule(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    phone_prefix_rules: Incomplete
    dc_id: Incomplete
    ips: Incomplete
    def __init__(self, phone_prefix_rules: str, dc_id: int, ips: list['TypeIpPort']) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class AccountDaysTTL(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    days: Incomplete
    def __init__(self, days: int) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class AttachMenuBot(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    bot_id: Incomplete
    short_name: Incomplete
    icons: Incomplete
    inactive: Incomplete
    has_settings: Incomplete
    request_write_access: Incomplete
    show_in_attach_menu: Incomplete
    show_in_side_menu: Incomplete
    side_menu_disclaimer_needed: Incomplete
    peer_types: Incomplete
    def __init__(self, bot_id: int, short_name: str, icons: list['TypeAttachMenuBotIcon'], inactive: bool | None = None, has_settings: bool | None = None, request_write_access: bool | None = None, show_in_attach_menu: bool | None = None, show_in_side_menu: bool | None = None, side_menu_disclaimer_needed: bool | None = None, peer_types: list['TypeAttachMenuPeerType'] | None = None) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class AttachMenuBotIcon(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    name: Incomplete
    icon: Incomplete
    colors: Incomplete
    def __init__(self, name: str, icon: TypeDocument, colors: list['TypeAttachMenuBotIconColor'] | None = None) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class AttachMenuBotIconColor(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    name: Incomplete
    color: Incomplete
    def __init__(self, name: str, color: int) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class AttachMenuBots(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    hash: Incomplete
    bots: Incomplete
    users: Incomplete
    def __init__(self, hash: int, bots: list['TypeAttachMenuBot'], users: list['TypeUser']) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class AttachMenuBotsBot(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    bot: Incomplete
    users: Incomplete
    def __init__(self, bot: TypeAttachMenuBot, users: list['TypeUser']) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class AttachMenuBotsNotModified(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class AttachMenuPeerTypeBotPM(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class AttachMenuPeerTypeBroadcast(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class AttachMenuPeerTypeChat(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class AttachMenuPeerTypePM(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class AttachMenuPeerTypeSameBotPM(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class Authorization(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    hash: Incomplete
    device_model: Incomplete
    platform: Incomplete
    system_version: Incomplete
    api_id: Incomplete
    app_name: Incomplete
    app_version: Incomplete
    date_created: Incomplete
    date_active: Incomplete
    ip: Incomplete
    country: Incomplete
    region: Incomplete
    current: Incomplete
    official_app: Incomplete
    password_pending: Incomplete
    encrypted_requests_disabled: Incomplete
    call_requests_disabled: Incomplete
    unconfirmed: Incomplete
    def __init__(self, hash: int, device_model: str, platform: str, system_version: str, api_id: int, app_name: str, app_version: str, date_created: datetime | None, date_active: datetime | None, ip: str, country: str, region: str, current: bool | None = None, official_app: bool | None = None, password_pending: bool | None = None, encrypted_requests_disabled: bool | None = None, call_requests_disabled: bool | None = None, unconfirmed: bool | None = None) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class AutoDownloadSettings(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    photo_size_max: Incomplete
    video_size_max: Incomplete
    file_size_max: Incomplete
    video_upload_maxbitrate: Incomplete
    small_queue_active_operations_max: Incomplete
    large_queue_active_operations_max: Incomplete
    disabled: Incomplete
    video_preload_large: Incomplete
    audio_preload_next: Incomplete
    phonecalls_less_data: Incomplete
    stories_preload: Incomplete
    def __init__(self, photo_size_max: int, video_size_max: int, file_size_max: int, video_upload_maxbitrate: int, small_queue_active_operations_max: int, large_queue_active_operations_max: int, disabled: bool | None = None, video_preload_large: bool | None = None, audio_preload_next: bool | None = None, phonecalls_less_data: bool | None = None, stories_preload: bool | None = None) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class AutoSaveException(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    peer: Incomplete
    settings: Incomplete
    def __init__(self, peer: TypePeer, settings: TypeAutoSaveSettings) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class AutoSaveSettings(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    photos: Incomplete
    videos: Incomplete
    video_max_size: Incomplete
    def __init__(self, photos: bool | None = None, videos: bool | None = None, video_max_size: int | None = None) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class AvailableEffect(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    id: Incomplete
    emoticon: Incomplete
    effect_sticker_id: Incomplete
    premium_required: Incomplete
    static_icon_id: Incomplete
    effect_animation_id: Incomplete
    def __init__(self, id: int, emoticon: str, effect_sticker_id: int, premium_required: bool | None = None, static_icon_id: int | None = None, effect_animation_id: int | None = None) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class AvailableReaction(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    reaction: Incomplete
    title: Incomplete
    static_icon: Incomplete
    appear_animation: Incomplete
    select_animation: Incomplete
    activate_animation: Incomplete
    effect_animation: Incomplete
    inactive: Incomplete
    premium: Incomplete
    around_animation: Incomplete
    center_icon: Incomplete
    def __init__(self, reaction: str, title: str, static_icon: TypeDocument, appear_animation: TypeDocument, select_animation: TypeDocument, activate_animation: TypeDocument, effect_animation: TypeDocument, inactive: bool | None = None, premium: bool | None = None, around_animation: TypeDocument | None = None, center_icon: TypeDocument | None = None) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class BadMsgNotification(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    bad_msg_id: Incomplete
    bad_msg_seqno: Incomplete
    error_code: Incomplete
    def __init__(self, bad_msg_id: int, bad_msg_seqno: int, error_code: int) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class BadServerSalt(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    bad_msg_id: Incomplete
    bad_msg_seqno: Incomplete
    error_code: Incomplete
    new_server_salt: Incomplete
    def __init__(self, bad_msg_id: int, bad_msg_seqno: int, error_code: int, new_server_salt: int) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class BankCardOpenUrl(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    url: Incomplete
    name: Incomplete
    def __init__(self, url: str, name: str) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class BaseThemeArctic(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class BaseThemeClassic(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class BaseThemeDay(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class BaseThemeNight(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class BaseThemeTinted(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class BindAuthKeyInner(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    nonce: Incomplete
    temp_auth_key_id: Incomplete
    perm_auth_key_id: Incomplete
    temp_session_id: Incomplete
    expires_at: Incomplete
    def __init__(self, nonce: int, temp_auth_key_id: int, perm_auth_key_id: int, temp_session_id: int, expires_at: datetime | None) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class Birthday(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    day: Incomplete
    month: Incomplete
    year: Incomplete
    def __init__(self, day: int, month: int, year: int | None = None) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class Boost(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    id: Incomplete
    date: Incomplete
    expires: Incomplete
    gift: Incomplete
    giveaway: Incomplete
    unclaimed: Incomplete
    user_id: Incomplete
    giveaway_msg_id: Incomplete
    used_gift_slug: Incomplete
    multiplier: Incomplete
    stars: Incomplete
    def __init__(self, id: str, date: datetime | None, expires: datetime | None, gift: bool | None = None, giveaway: bool | None = None, unclaimed: bool | None = None, user_id: int | None = None, giveaway_msg_id: int | None = None, used_gift_slug: str | None = None, multiplier: int | None = None, stars: int | None = None) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class BotApp(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    id: Incomplete
    access_hash: Incomplete
    short_name: Incomplete
    title: Incomplete
    description: Incomplete
    photo: Incomplete
    hash: Incomplete
    document: Incomplete
    def __init__(self, id: int, access_hash: int, short_name: str, title: str, description: str, photo: TypePhoto, hash: int, document: TypeDocument | None = None) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class BotAppNotModified(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class BotAppSettings(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    placeholder_path: Incomplete
    background_color: Incomplete
    background_dark_color: Incomplete
    header_color: Incomplete
    header_dark_color: Incomplete
    def __init__(self, placeholder_path: bytes | None = None, background_color: int | None = None, background_dark_color: int | None = None, header_color: int | None = None, header_dark_color: int | None = None) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class BotBusinessConnection(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    connection_id: Incomplete
    user_id: Incomplete
    dc_id: Incomplete
    date: Incomplete
    can_reply: Incomplete
    disabled: Incomplete
    def __init__(self, connection_id: str, user_id: int, dc_id: int, date: datetime | None, can_reply: bool | None = None, disabled: bool | None = None) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class BotCommand(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    command: Incomplete
    description: Incomplete
    def __init__(self, command: str, description: str) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class BotCommandScopeChatAdmins(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class BotCommandScopeChats(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class BotCommandScopeDefault(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class BotCommandScopePeer(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    peer: Incomplete
    def __init__(self, peer: TypeInputPeer) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class BotCommandScopePeerAdmins(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    peer: Incomplete
    def __init__(self, peer: TypeInputPeer) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class BotCommandScopePeerUser(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    peer: Incomplete
    user_id: Incomplete
    def __init__(self, peer: TypeInputPeer, user_id: TypeInputUser) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class BotCommandScopeUsers(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class BotInfo(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    has_preview_medias: Incomplete
    user_id: Incomplete
    description: Incomplete
    description_photo: Incomplete
    description_document: Incomplete
    commands: Incomplete
    menu_button: Incomplete
    privacy_policy_url: Incomplete
    app_settings: Incomplete
    def __init__(self, has_preview_medias: bool | None = None, user_id: int | None = None, description: str | None = None, description_photo: TypePhoto | None = None, description_document: TypeDocument | None = None, commands: list['TypeBotCommand'] | None = None, menu_button: TypeBotMenuButton | None = None, privacy_policy_url: str | None = None, app_settings: TypeBotAppSettings | None = None) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class BotInlineMediaResult(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    id: Incomplete
    type: Incomplete
    send_message: Incomplete
    photo: Incomplete
    document: Incomplete
    title: Incomplete
    description: Incomplete
    def __init__(self, id: str, type: str, send_message: TypeBotInlineMessage, photo: TypePhoto | None = None, document: TypeDocument | None = None, title: str | None = None, description: str | None = None) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class BotInlineMessageMediaAuto(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    message: Incomplete
    invert_media: Incomplete
    entities: Incomplete
    reply_markup: Incomplete
    def __init__(self, message: str, invert_media: bool | None = None, entities: list['TypeMessageEntity'] | None = None, reply_markup: TypeReplyMarkup | None = None) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class BotInlineMessageMediaContact(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    phone_number: Incomplete
    first_name: Incomplete
    last_name: Incomplete
    vcard: Incomplete
    reply_markup: Incomplete
    def __init__(self, phone_number: str, first_name: str, last_name: str, vcard: str, reply_markup: TypeReplyMarkup | None = None) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class BotInlineMessageMediaGeo(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    geo: Incomplete
    heading: Incomplete
    period: Incomplete
    proximity_notification_radius: Incomplete
    reply_markup: Incomplete
    def __init__(self, geo: TypeGeoPoint, heading: int | None = None, period: int | None = None, proximity_notification_radius: int | None = None, reply_markup: TypeReplyMarkup | None = None) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class BotInlineMessageMediaInvoice(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    title: Incomplete
    description: Incomplete
    currency: Incomplete
    total_amount: Incomplete
    shipping_address_requested: Incomplete
    test: Incomplete
    photo: Incomplete
    reply_markup: Incomplete
    def __init__(self, title: str, description: str, currency: str, total_amount: int, shipping_address_requested: bool | None = None, test: bool | None = None, photo: TypeWebDocument | None = None, reply_markup: TypeReplyMarkup | None = None) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class BotInlineMessageMediaVenue(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    geo: Incomplete
    title: Incomplete
    address: Incomplete
    provider: Incomplete
    venue_id: Incomplete
    venue_type: Incomplete
    reply_markup: Incomplete
    def __init__(self, geo: TypeGeoPoint, title: str, address: str, provider: str, venue_id: str, venue_type: str, reply_markup: TypeReplyMarkup | None = None) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class BotInlineMessageMediaWebPage(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    message: Incomplete
    url: Incomplete
    invert_media: Incomplete
    force_large_media: Incomplete
    force_small_media: Incomplete
    manual: Incomplete
    safe: Incomplete
    entities: Incomplete
    reply_markup: Incomplete
    def __init__(self, message: str, url: str, invert_media: bool | None = None, force_large_media: bool | None = None, force_small_media: bool | None = None, manual: bool | None = None, safe: bool | None = None, entities: list['TypeMessageEntity'] | None = None, reply_markup: TypeReplyMarkup | None = None) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class BotInlineMessageText(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    message: Incomplete
    no_webpage: Incomplete
    invert_media: Incomplete
    entities: Incomplete
    reply_markup: Incomplete
    def __init__(self, message: str, no_webpage: bool | None = None, invert_media: bool | None = None, entities: list['TypeMessageEntity'] | None = None, reply_markup: TypeReplyMarkup | None = None) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class BotInlineResult(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    id: Incomplete
    type: Incomplete
    send_message: Incomplete
    title: Incomplete
    description: Incomplete
    url: Incomplete
    thumb: Incomplete
    content: Incomplete
    def __init__(self, id: str, type: str, send_message: TypeBotInlineMessage, title: str | None = None, description: str | None = None, url: str | None = None, thumb: TypeWebDocument | None = None, content: TypeWebDocument | None = None) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class BotMenuButton(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    text: Incomplete
    url: Incomplete
    def __init__(self, text: str, url: str) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class BotMenuButtonCommands(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class BotMenuButtonDefault(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class BotPreviewMedia(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    date: Incomplete
    media: Incomplete
    def __init__(self, date: datetime | None, media: TypeMessageMedia) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class BroadcastRevenueBalances(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    current_balance: Incomplete
    available_balance: Incomplete
    overall_revenue: Incomplete
    withdrawal_enabled: Incomplete
    def __init__(self, current_balance: int, available_balance: int, overall_revenue: int, withdrawal_enabled: bool | None = None) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class BroadcastRevenueTransactionProceeds(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    amount: Incomplete
    from_date: Incomplete
    to_date: Incomplete
    def __init__(self, amount: int, from_date: datetime | None, to_date: datetime | None) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class BroadcastRevenueTransactionRefund(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    amount: Incomplete
    date: Incomplete
    provider: Incomplete
    def __init__(self, amount: int, date: datetime | None, provider: str) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class BroadcastRevenueTransactionWithdrawal(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    amount: Incomplete
    date: Incomplete
    provider: Incomplete
    pending: Incomplete
    failed: Incomplete
    transaction_date: Incomplete
    transaction_url: Incomplete
    def __init__(self, amount: int, date: datetime | None, provider: str, pending: bool | None = None, failed: bool | None = None, transaction_date: datetime | None = None, transaction_url: str | None = None) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class BusinessAwayMessage(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    shortcut_id: Incomplete
    schedule: Incomplete
    recipients: Incomplete
    offline_only: Incomplete
    def __init__(self, shortcut_id: int, schedule: TypeBusinessAwayMessageSchedule, recipients: TypeBusinessRecipients, offline_only: bool | None = None) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class BusinessAwayMessageScheduleAlways(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class BusinessAwayMessageScheduleCustom(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    start_date: Incomplete
    end_date: Incomplete
    def __init__(self, start_date: datetime | None, end_date: datetime | None) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class BusinessAwayMessageScheduleOutsideWorkHours(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class BusinessBotRecipients(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    existing_chats: Incomplete
    new_chats: Incomplete
    contacts: Incomplete
    non_contacts: Incomplete
    exclude_selected: Incomplete
    users: Incomplete
    exclude_users: Incomplete
    def __init__(self, existing_chats: bool | None = None, new_chats: bool | None = None, contacts: bool | None = None, non_contacts: bool | None = None, exclude_selected: bool | None = None, users: list[int] | None = None, exclude_users: list[int] | None = None) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class BusinessChatLink(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    link: Incomplete
    message: Incomplete
    views: Incomplete
    entities: Incomplete
    title: Incomplete
    def __init__(self, link: str, message: str, views: int, entities: list['TypeMessageEntity'] | None = None, title: str | None = None) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class BusinessGreetingMessage(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    shortcut_id: Incomplete
    recipients: Incomplete
    no_activity_days: Incomplete
    def __init__(self, shortcut_id: int, recipients: TypeBusinessRecipients, no_activity_days: int) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class BusinessIntro(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    title: Incomplete
    description: Incomplete
    sticker: Incomplete
    def __init__(self, title: str, description: str, sticker: TypeDocument | None = None) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class BusinessLocation(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    address: Incomplete
    geo_point: Incomplete
    def __init__(self, address: str, geo_point: TypeGeoPoint | None = None) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class BusinessRecipients(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    existing_chats: Incomplete
    new_chats: Incomplete
    contacts: Incomplete
    non_contacts: Incomplete
    exclude_selected: Incomplete
    users: Incomplete
    def __init__(self, existing_chats: bool | None = None, new_chats: bool | None = None, contacts: bool | None = None, non_contacts: bool | None = None, exclude_selected: bool | None = None, users: list[int] | None = None) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class BusinessWeeklyOpen(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    start_minute: Incomplete
    end_minute: Incomplete
    def __init__(self, start_minute: int, end_minute: int) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class BusinessWorkHours(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    timezone_id: Incomplete
    weekly_open: Incomplete
    open_now: Incomplete
    def __init__(self, timezone_id: str, weekly_open: list['TypeBusinessWeeklyOpen'], open_now: bool | None = None) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class CdnConfig(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    public_keys: Incomplete
    def __init__(self, public_keys: list['TypeCdnPublicKey']) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class CdnPublicKey(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    dc_id: Incomplete
    public_key: Incomplete
    def __init__(self, dc_id: int, public_key: str) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class Channel(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    id: Incomplete
    title: Incomplete
    photo: Incomplete
    date: Incomplete
    creator: Incomplete
    left: Incomplete
    broadcast: Incomplete
    verified: Incomplete
    megagroup: Incomplete
    restricted: Incomplete
    signatures: Incomplete
    min: Incomplete
    scam: Incomplete
    has_link: Incomplete
    has_geo: Incomplete
    slowmode_enabled: Incomplete
    call_active: Incomplete
    call_not_empty: Incomplete
    fake: Incomplete
    gigagroup: Incomplete
    noforwards: Incomplete
    join_to_send: Incomplete
    join_request: Incomplete
    forum: Incomplete
    stories_hidden: Incomplete
    stories_hidden_min: Incomplete
    stories_unavailable: Incomplete
    signature_profiles: Incomplete
    access_hash: Incomplete
    username: Incomplete
    restriction_reason: Incomplete
    admin_rights: Incomplete
    banned_rights: Incomplete
    default_banned_rights: Incomplete
    participants_count: Incomplete
    usernames: Incomplete
    stories_max_id: Incomplete
    color: Incomplete
    profile_color: Incomplete
    emoji_status: Incomplete
    level: Incomplete
    subscription_until_date: Incomplete
    def __init__(self, id: int, title: str, photo: TypeChatPhoto, date: datetime | None, creator: bool | None = None, left: bool | None = None, broadcast: bool | None = None, verified: bool | None = None, megagroup: bool | None = None, restricted: bool | None = None, signatures: bool | None = None, min: bool | None = None, scam: bool | None = None, has_link: bool | None = None, has_geo: bool | None = None, slowmode_enabled: bool | None = None, call_active: bool | None = None, call_not_empty: bool | None = None, fake: bool | None = None, gigagroup: bool | None = None, noforwards: bool | None = None, join_to_send: bool | None = None, join_request: bool | None = None, forum: bool | None = None, stories_hidden: bool | None = None, stories_hidden_min: bool | None = None, stories_unavailable: bool | None = None, signature_profiles: bool | None = None, access_hash: int | None = None, username: str | None = None, restriction_reason: list['TypeRestrictionReason'] | None = None, admin_rights: TypeChatAdminRights | None = None, banned_rights: TypeChatBannedRights | None = None, default_banned_rights: TypeChatBannedRights | None = None, participants_count: int | None = None, usernames: list['TypeUsername'] | None = None, stories_max_id: int | None = None, color: TypePeerColor | None = None, profile_color: TypePeerColor | None = None, emoji_status: TypeEmojiStatus | None = None, level: int | None = None, subscription_until_date: datetime | None = None) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class ChannelAdminLogEvent(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    id: Incomplete
    date: Incomplete
    user_id: Incomplete
    action: Incomplete
    def __init__(self, id: int, date: datetime | None, user_id: int, action: TypeChannelAdminLogEventAction) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class ChannelAdminLogEventActionChangeAbout(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    prev_value: Incomplete
    new_value: Incomplete
    def __init__(self, prev_value: str, new_value: str) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class ChannelAdminLogEventActionChangeAvailableReactions(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    prev_value: Incomplete
    new_value: Incomplete
    def __init__(self, prev_value: TypeChatReactions, new_value: TypeChatReactions) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class ChannelAdminLogEventActionChangeEmojiStatus(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    prev_value: Incomplete
    new_value: Incomplete
    def __init__(self, prev_value: TypeEmojiStatus, new_value: TypeEmojiStatus) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class ChannelAdminLogEventActionChangeEmojiStickerSet(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    prev_stickerset: Incomplete
    new_stickerset: Incomplete
    def __init__(self, prev_stickerset: TypeInputStickerSet, new_stickerset: TypeInputStickerSet) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class ChannelAdminLogEventActionChangeHistoryTTL(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    prev_value: Incomplete
    new_value: Incomplete
    def __init__(self, prev_value: int, new_value: int) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class ChannelAdminLogEventActionChangeLinkedChat(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    prev_value: Incomplete
    new_value: Incomplete
    def __init__(self, prev_value: int, new_value: int) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class ChannelAdminLogEventActionChangeLocation(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    prev_value: Incomplete
    new_value: Incomplete
    def __init__(self, prev_value: TypeChannelLocation, new_value: TypeChannelLocation) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class ChannelAdminLogEventActionChangePeerColor(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    prev_value: Incomplete
    new_value: Incomplete
    def __init__(self, prev_value: TypePeerColor, new_value: TypePeerColor) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class ChannelAdminLogEventActionChangePhoto(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    prev_photo: Incomplete
    new_photo: Incomplete
    def __init__(self, prev_photo: TypePhoto, new_photo: TypePhoto) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class ChannelAdminLogEventActionChangeProfilePeerColor(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    prev_value: Incomplete
    new_value: Incomplete
    def __init__(self, prev_value: TypePeerColor, new_value: TypePeerColor) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class ChannelAdminLogEventActionChangeStickerSet(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    prev_stickerset: Incomplete
    new_stickerset: Incomplete
    def __init__(self, prev_stickerset: TypeInputStickerSet, new_stickerset: TypeInputStickerSet) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class ChannelAdminLogEventActionChangeTitle(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    prev_value: Incomplete
    new_value: Incomplete
    def __init__(self, prev_value: str, new_value: str) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class ChannelAdminLogEventActionChangeUsername(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    prev_value: Incomplete
    new_value: Incomplete
    def __init__(self, prev_value: str, new_value: str) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class ChannelAdminLogEventActionChangeUsernames(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    prev_value: Incomplete
    new_value: Incomplete
    def __init__(self, prev_value: list[str], new_value: list[str]) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class ChannelAdminLogEventActionChangeWallpaper(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    prev_value: Incomplete
    new_value: Incomplete
    def __init__(self, prev_value: TypeWallPaper, new_value: TypeWallPaper) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class ChannelAdminLogEventActionCreateTopic(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    topic: Incomplete
    def __init__(self, topic: TypeForumTopic) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class ChannelAdminLogEventActionDefaultBannedRights(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    prev_banned_rights: Incomplete
    new_banned_rights: Incomplete
    def __init__(self, prev_banned_rights: TypeChatBannedRights, new_banned_rights: TypeChatBannedRights) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class ChannelAdminLogEventActionDeleteMessage(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    message: Incomplete
    def __init__(self, message: TypeMessage) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class ChannelAdminLogEventActionDeleteTopic(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    topic: Incomplete
    def __init__(self, topic: TypeForumTopic) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class ChannelAdminLogEventActionDiscardGroupCall(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    call: Incomplete
    def __init__(self, call: TypeInputGroupCall) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class ChannelAdminLogEventActionEditMessage(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    prev_message: Incomplete
    new_message: Incomplete
    def __init__(self, prev_message: TypeMessage, new_message: TypeMessage) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class ChannelAdminLogEventActionEditTopic(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    prev_topic: Incomplete
    new_topic: Incomplete
    def __init__(self, prev_topic: TypeForumTopic, new_topic: TypeForumTopic) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class ChannelAdminLogEventActionExportedInviteDelete(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    invite: Incomplete
    def __init__(self, invite: TypeExportedChatInvite) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class ChannelAdminLogEventActionExportedInviteEdit(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    prev_invite: Incomplete
    new_invite: Incomplete
    def __init__(self, prev_invite: TypeExportedChatInvite, new_invite: TypeExportedChatInvite) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class ChannelAdminLogEventActionExportedInviteRevoke(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    invite: Incomplete
    def __init__(self, invite: TypeExportedChatInvite) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class ChannelAdminLogEventActionParticipantInvite(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    participant: Incomplete
    def __init__(self, participant: TypeChannelParticipant) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class ChannelAdminLogEventActionParticipantJoin(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class ChannelAdminLogEventActionParticipantJoinByInvite(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    invite: Incomplete
    via_chatlist: Incomplete
    def __init__(self, invite: TypeExportedChatInvite, via_chatlist: bool | None = None) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class ChannelAdminLogEventActionParticipantJoinByRequest(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    invite: Incomplete
    approved_by: Incomplete
    def __init__(self, invite: TypeExportedChatInvite, approved_by: int) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class ChannelAdminLogEventActionParticipantLeave(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class ChannelAdminLogEventActionParticipantMute(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    participant: Incomplete
    def __init__(self, participant: TypeGroupCallParticipant) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class ChannelAdminLogEventActionParticipantSubExtend(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    prev_participant: Incomplete
    new_participant: Incomplete
    def __init__(self, prev_participant: TypeChannelParticipant, new_participant: TypeChannelParticipant) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class ChannelAdminLogEventActionParticipantToggleAdmin(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    prev_participant: Incomplete
    new_participant: Incomplete
    def __init__(self, prev_participant: TypeChannelParticipant, new_participant: TypeChannelParticipant) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class ChannelAdminLogEventActionParticipantToggleBan(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    prev_participant: Incomplete
    new_participant: Incomplete
    def __init__(self, prev_participant: TypeChannelParticipant, new_participant: TypeChannelParticipant) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class ChannelAdminLogEventActionParticipantUnmute(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    participant: Incomplete
    def __init__(self, participant: TypeGroupCallParticipant) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class ChannelAdminLogEventActionParticipantVolume(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    participant: Incomplete
    def __init__(self, participant: TypeGroupCallParticipant) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class ChannelAdminLogEventActionPinTopic(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    prev_topic: Incomplete
    new_topic: Incomplete
    def __init__(self, prev_topic: TypeForumTopic | None = None, new_topic: TypeForumTopic | None = None) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class ChannelAdminLogEventActionSendMessage(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    message: Incomplete
    def __init__(self, message: TypeMessage) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class ChannelAdminLogEventActionStartGroupCall(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    call: Incomplete
    def __init__(self, call: TypeInputGroupCall) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class ChannelAdminLogEventActionStopPoll(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    message: Incomplete
    def __init__(self, message: TypeMessage) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class ChannelAdminLogEventActionToggleAntiSpam(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    new_value: Incomplete
    def __init__(self, new_value: bool) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class ChannelAdminLogEventActionToggleForum(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    new_value: Incomplete
    def __init__(self, new_value: bool) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class ChannelAdminLogEventActionToggleGroupCallSetting(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    join_muted: Incomplete
    def __init__(self, join_muted: bool) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class ChannelAdminLogEventActionToggleInvites(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    new_value: Incomplete
    def __init__(self, new_value: bool) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class ChannelAdminLogEventActionToggleNoForwards(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    new_value: Incomplete
    def __init__(self, new_value: bool) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class ChannelAdminLogEventActionTogglePreHistoryHidden(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    new_value: Incomplete
    def __init__(self, new_value: bool) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class ChannelAdminLogEventActionToggleSignatureProfiles(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    new_value: Incomplete
    def __init__(self, new_value: bool) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class ChannelAdminLogEventActionToggleSignatures(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    new_value: Incomplete
    def __init__(self, new_value: bool) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class ChannelAdminLogEventActionToggleSlowMode(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    prev_value: Incomplete
    new_value: Incomplete
    def __init__(self, prev_value: int, new_value: int) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class ChannelAdminLogEventActionUpdatePinned(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    message: Incomplete
    def __init__(self, message: TypeMessage) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class ChannelAdminLogEventsFilter(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    join: Incomplete
    leave: Incomplete
    invite: Incomplete
    ban: Incomplete
    unban: Incomplete
    kick: Incomplete
    unkick: Incomplete
    promote: Incomplete
    demote: Incomplete
    info: Incomplete
    settings: Incomplete
    pinned: Incomplete
    edit: Incomplete
    delete: Incomplete
    group_call: Incomplete
    invites: Incomplete
    send: Incomplete
    forums: Incomplete
    sub_extend: Incomplete
    def __init__(self, join: bool | None = None, leave: bool | None = None, invite: bool | None = None, ban: bool | None = None, unban: bool | None = None, kick: bool | None = None, unkick: bool | None = None, promote: bool | None = None, demote: bool | None = None, info: bool | None = None, settings: bool | None = None, pinned: bool | None = None, edit: bool | None = None, delete: bool | None = None, group_call: bool | None = None, invites: bool | None = None, send: bool | None = None, forums: bool | None = None, sub_extend: bool | None = None) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class ChannelForbidden(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    id: Incomplete
    access_hash: Incomplete
    title: Incomplete
    broadcast: Incomplete
    megagroup: Incomplete
    until_date: Incomplete
    def __init__(self, id: int, access_hash: int, title: str, broadcast: bool | None = None, megagroup: bool | None = None, until_date: datetime | None = None) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class ChannelFull(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    id: Incomplete
    about: Incomplete
    read_inbox_max_id: Incomplete
    read_outbox_max_id: Incomplete
    unread_count: Incomplete
    chat_photo: Incomplete
    notify_settings: Incomplete
    bot_info: Incomplete
    pts: Incomplete
    can_view_participants: Incomplete
    can_set_username: Incomplete
    can_set_stickers: Incomplete
    hidden_prehistory: Incomplete
    can_set_location: Incomplete
    has_scheduled: Incomplete
    can_view_stats: Incomplete
    blocked: Incomplete
    can_delete_channel: Incomplete
    antispam: Incomplete
    participants_hidden: Incomplete
    translations_disabled: Incomplete
    stories_pinned_available: Incomplete
    view_forum_as_messages: Incomplete
    restricted_sponsored: Incomplete
    can_view_revenue: Incomplete
    paid_media_allowed: Incomplete
    can_view_stars_revenue: Incomplete
    paid_reactions_available: Incomplete
    participants_count: Incomplete
    admins_count: Incomplete
    kicked_count: Incomplete
    banned_count: Incomplete
    online_count: Incomplete
    exported_invite: Incomplete
    migrated_from_chat_id: Incomplete
    migrated_from_max_id: Incomplete
    pinned_msg_id: Incomplete
    stickerset: Incomplete
    available_min_id: Incomplete
    folder_id: Incomplete
    linked_chat_id: Incomplete
    location: Incomplete
    slowmode_seconds: Incomplete
    slowmode_next_send_date: Incomplete
    stats_dc: Incomplete
    call: Incomplete
    ttl_period: Incomplete
    pending_suggestions: Incomplete
    groupcall_default_join_as: Incomplete
    theme_emoticon: Incomplete
    requests_pending: Incomplete
    recent_requesters: Incomplete
    default_send_as: Incomplete
    available_reactions: Incomplete
    reactions_limit: Incomplete
    stories: Incomplete
    wallpaper: Incomplete
    boosts_applied: Incomplete
    boosts_unrestrict: Incomplete
    emojiset: Incomplete
    def __init__(self, id: int, about: str, read_inbox_max_id: int, read_outbox_max_id: int, unread_count: int, chat_photo: TypePhoto, notify_settings: TypePeerNotifySettings, bot_info: list['TypeBotInfo'], pts: int, can_view_participants: bool | None = None, can_set_username: bool | None = None, can_set_stickers: bool | None = None, hidden_prehistory: bool | None = None, can_set_location: bool | None = None, has_scheduled: bool | None = None, can_view_stats: bool | None = None, blocked: bool | None = None, can_delete_channel: bool | None = None, antispam: bool | None = None, participants_hidden: bool | None = None, translations_disabled: bool | None = None, stories_pinned_available: bool | None = None, view_forum_as_messages: bool | None = None, restricted_sponsored: bool | None = None, can_view_revenue: bool | None = None, paid_media_allowed: bool | None = None, can_view_stars_revenue: bool | None = None, paid_reactions_available: bool | None = None, participants_count: int | None = None, admins_count: int | None = None, kicked_count: int | None = None, banned_count: int | None = None, online_count: int | None = None, exported_invite: TypeExportedChatInvite | None = None, migrated_from_chat_id: int | None = None, migrated_from_max_id: int | None = None, pinned_msg_id: int | None = None, stickerset: TypeStickerSet | None = None, available_min_id: int | None = None, folder_id: int | None = None, linked_chat_id: int | None = None, location: TypeChannelLocation | None = None, slowmode_seconds: int | None = None, slowmode_next_send_date: datetime | None = None, stats_dc: int | None = None, call: TypeInputGroupCall | None = None, ttl_period: int | None = None, pending_suggestions: list[str] | None = None, groupcall_default_join_as: TypePeer | None = None, theme_emoticon: str | None = None, requests_pending: int | None = None, recent_requesters: list[int] | None = None, default_send_as: TypePeer | None = None, available_reactions: TypeChatReactions | None = None, reactions_limit: int | None = None, stories: TypePeerStories | None = None, wallpaper: TypeWallPaper | None = None, boosts_applied: int | None = None, boosts_unrestrict: int | None = None, emojiset: TypeStickerSet | None = None) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class ChannelLocation(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    geo_point: Incomplete
    address: Incomplete
    def __init__(self, geo_point: TypeGeoPoint, address: str) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class ChannelLocationEmpty(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class ChannelMessagesFilter(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    ranges: Incomplete
    exclude_new_messages: Incomplete
    def __init__(self, ranges: list['TypeMessageRange'], exclude_new_messages: bool | None = None) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class ChannelMessagesFilterEmpty(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class ChannelParticipant(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    user_id: Incomplete
    date: Incomplete
    subscription_until_date: Incomplete
    def __init__(self, user_id: int, date: datetime | None, subscription_until_date: datetime | None = None) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class ChannelParticipantAdmin(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    user_id: Incomplete
    promoted_by: Incomplete
    date: Incomplete
    admin_rights: Incomplete
    can_edit: Incomplete
    is_self: Incomplete
    inviter_id: Incomplete
    rank: Incomplete
    def __init__(self, user_id: int, promoted_by: int, date: datetime | None, admin_rights: TypeChatAdminRights, can_edit: bool | None = None, is_self: bool | None = None, inviter_id: int | None = None, rank: str | None = None) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class ChannelParticipantBanned(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    peer: Incomplete
    kicked_by: Incomplete
    date: Incomplete
    banned_rights: Incomplete
    left: Incomplete
    def __init__(self, peer: TypePeer, kicked_by: int, date: datetime | None, banned_rights: TypeChatBannedRights, left: bool | None = None) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class ChannelParticipantCreator(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    user_id: Incomplete
    admin_rights: Incomplete
    rank: Incomplete
    def __init__(self, user_id: int, admin_rights: TypeChatAdminRights, rank: str | None = None) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class ChannelParticipantLeft(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    peer: Incomplete
    def __init__(self, peer: TypePeer) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class ChannelParticipantSelf(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    user_id: Incomplete
    inviter_id: Incomplete
    date: Incomplete
    via_request: Incomplete
    subscription_until_date: Incomplete
    def __init__(self, user_id: int, inviter_id: int, date: datetime | None, via_request: bool | None = None, subscription_until_date: datetime | None = None) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class ChannelParticipantsAdmins(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class ChannelParticipantsBanned(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    q: Incomplete
    def __init__(self, q: str) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class ChannelParticipantsBots(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class ChannelParticipantsContacts(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    q: Incomplete
    def __init__(self, q: str) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class ChannelParticipantsKicked(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    q: Incomplete
    def __init__(self, q: str) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class ChannelParticipantsMentions(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    q: Incomplete
    top_msg_id: Incomplete
    def __init__(self, q: str | None = None, top_msg_id: int | None = None) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class ChannelParticipantsRecent(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class ChannelParticipantsSearch(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    q: Incomplete
    def __init__(self, q: str) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class Chat(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    id: Incomplete
    title: Incomplete
    photo: Incomplete
    participants_count: Incomplete
    date: Incomplete
    version: Incomplete
    creator: Incomplete
    left: Incomplete
    deactivated: Incomplete
    call_active: Incomplete
    call_not_empty: Incomplete
    noforwards: Incomplete
    migrated_to: Incomplete
    admin_rights: Incomplete
    default_banned_rights: Incomplete
    def __init__(self, id: int, title: str, photo: TypeChatPhoto, participants_count: int, date: datetime | None, version: int, creator: bool | None = None, left: bool | None = None, deactivated: bool | None = None, call_active: bool | None = None, call_not_empty: bool | None = None, noforwards: bool | None = None, migrated_to: TypeInputChannel | None = None, admin_rights: TypeChatAdminRights | None = None, default_banned_rights: TypeChatBannedRights | None = None) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class ChatAdminRights(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    change_info: Incomplete
    post_messages: Incomplete
    edit_messages: Incomplete
    delete_messages: Incomplete
    ban_users: Incomplete
    invite_users: Incomplete
    pin_messages: Incomplete
    add_admins: Incomplete
    anonymous: Incomplete
    manage_call: Incomplete
    other: Incomplete
    manage_topics: Incomplete
    post_stories: Incomplete
    edit_stories: Incomplete
    delete_stories: Incomplete
    def __init__(self, change_info: bool | None = None, post_messages: bool | None = None, edit_messages: bool | None = None, delete_messages: bool | None = None, ban_users: bool | None = None, invite_users: bool | None = None, pin_messages: bool | None = None, add_admins: bool | None = None, anonymous: bool | None = None, manage_call: bool | None = None, other: bool | None = None, manage_topics: bool | None = None, post_stories: bool | None = None, edit_stories: bool | None = None, delete_stories: bool | None = None) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class ChatAdminWithInvites(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    admin_id: Incomplete
    invites_count: Incomplete
    revoked_invites_count: Incomplete
    def __init__(self, admin_id: int, invites_count: int, revoked_invites_count: int) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class ChatBannedRights(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    until_date: Incomplete
    view_messages: Incomplete
    send_messages: Incomplete
    send_media: Incomplete
    send_stickers: Incomplete
    send_gifs: Incomplete
    send_games: Incomplete
    send_inline: Incomplete
    embed_links: Incomplete
    send_polls: Incomplete
    change_info: Incomplete
    invite_users: Incomplete
    pin_messages: Incomplete
    manage_topics: Incomplete
    send_photos: Incomplete
    send_videos: Incomplete
    send_roundvideos: Incomplete
    send_audios: Incomplete
    send_voices: Incomplete
    send_docs: Incomplete
    send_plain: Incomplete
    def __init__(self, until_date: datetime | None, view_messages: bool | None = None, send_messages: bool | None = None, send_media: bool | None = None, send_stickers: bool | None = None, send_gifs: bool | None = None, send_games: bool | None = None, send_inline: bool | None = None, embed_links: bool | None = None, send_polls: bool | None = None, change_info: bool | None = None, invite_users: bool | None = None, pin_messages: bool | None = None, manage_topics: bool | None = None, send_photos: bool | None = None, send_videos: bool | None = None, send_roundvideos: bool | None = None, send_audios: bool | None = None, send_voices: bool | None = None, send_docs: bool | None = None, send_plain: bool | None = None) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class ChatEmpty(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    id: Incomplete
    def __init__(self, id: int) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class ChatForbidden(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    id: Incomplete
    title: Incomplete
    def __init__(self, id: int, title: str) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class ChatFull(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    id: Incomplete
    about: Incomplete
    participants: Incomplete
    notify_settings: Incomplete
    can_set_username: Incomplete
    has_scheduled: Incomplete
    translations_disabled: Incomplete
    chat_photo: Incomplete
    exported_invite: Incomplete
    bot_info: Incomplete
    pinned_msg_id: Incomplete
    folder_id: Incomplete
    call: Incomplete
    ttl_period: Incomplete
    groupcall_default_join_as: Incomplete
    theme_emoticon: Incomplete
    requests_pending: Incomplete
    recent_requesters: Incomplete
    available_reactions: Incomplete
    reactions_limit: Incomplete
    def __init__(self, id: int, about: str, participants: TypeChatParticipants, notify_settings: TypePeerNotifySettings, can_set_username: bool | None = None, has_scheduled: bool | None = None, translations_disabled: bool | None = None, chat_photo: TypePhoto | None = None, exported_invite: TypeExportedChatInvite | None = None, bot_info: list['TypeBotInfo'] | None = None, pinned_msg_id: int | None = None, folder_id: int | None = None, call: TypeInputGroupCall | None = None, ttl_period: int | None = None, groupcall_default_join_as: TypePeer | None = None, theme_emoticon: str | None = None, requests_pending: int | None = None, recent_requesters: list[int] | None = None, available_reactions: TypeChatReactions | None = None, reactions_limit: int | None = None) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class ChatInvite(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    title: Incomplete
    photo: Incomplete
    participants_count: Incomplete
    color: Incomplete
    channel: Incomplete
    broadcast: Incomplete
    public: Incomplete
    megagroup: Incomplete
    request_needed: Incomplete
    verified: Incomplete
    scam: Incomplete
    fake: Incomplete
    can_refulfill_subscription: Incomplete
    about: Incomplete
    participants: Incomplete
    subscription_pricing: Incomplete
    subscription_form_id: Incomplete
    def __init__(self, title: str, photo: TypePhoto, participants_count: int, color: int, channel: bool | None = None, broadcast: bool | None = None, public: bool | None = None, megagroup: bool | None = None, request_needed: bool | None = None, verified: bool | None = None, scam: bool | None = None, fake: bool | None = None, can_refulfill_subscription: bool | None = None, about: str | None = None, participants: list['TypeUser'] | None = None, subscription_pricing: TypeStarsSubscriptionPricing | None = None, subscription_form_id: int | None = None) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class ChatInviteAlready(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    chat: Incomplete
    def __init__(self, chat: TypeChat) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class ChatInviteExported(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    link: Incomplete
    admin_id: Incomplete
    date: Incomplete
    revoked: Incomplete
    permanent: Incomplete
    request_needed: Incomplete
    start_date: Incomplete
    expire_date: Incomplete
    usage_limit: Incomplete
    usage: Incomplete
    requested: Incomplete
    subscription_expired: Incomplete
    title: Incomplete
    subscription_pricing: Incomplete
    def __init__(self, link: str, admin_id: int, date: datetime | None, revoked: bool | None = None, permanent: bool | None = None, request_needed: bool | None = None, start_date: datetime | None = None, expire_date: datetime | None = None, usage_limit: int | None = None, usage: int | None = None, requested: int | None = None, subscription_expired: int | None = None, title: str | None = None, subscription_pricing: TypeStarsSubscriptionPricing | None = None) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class ChatInviteImporter(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    user_id: Incomplete
    date: Incomplete
    requested: Incomplete
    via_chatlist: Incomplete
    about: Incomplete
    approved_by: Incomplete
    def __init__(self, user_id: int, date: datetime | None, requested: bool | None = None, via_chatlist: bool | None = None, about: str | None = None, approved_by: int | None = None) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class ChatInvitePeek(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    chat: Incomplete
    expires: Incomplete
    def __init__(self, chat: TypeChat, expires: datetime | None) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class ChatInvitePublicJoinRequests(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class ChatOnlines(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    onlines: Incomplete
    def __init__(self, onlines: int) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class ChatParticipant(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    user_id: Incomplete
    inviter_id: Incomplete
    date: Incomplete
    def __init__(self, user_id: int, inviter_id: int, date: datetime | None) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class ChatParticipantAdmin(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    user_id: Incomplete
    inviter_id: Incomplete
    date: Incomplete
    def __init__(self, user_id: int, inviter_id: int, date: datetime | None) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class ChatParticipantCreator(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    user_id: Incomplete
    def __init__(self, user_id: int) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class ChatParticipants(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    chat_id: Incomplete
    participants: Incomplete
    version: Incomplete
    def __init__(self, chat_id: int, participants: list['TypeChatParticipant'], version: int) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class ChatParticipantsForbidden(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    chat_id: Incomplete
    self_participant: Incomplete
    def __init__(self, chat_id: int, self_participant: TypeChatParticipant | None = None) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class ChatPhoto(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    photo_id: Incomplete
    dc_id: Incomplete
    has_video: Incomplete
    stripped_thumb: Incomplete
    def __init__(self, photo_id: int, dc_id: int, has_video: bool | None = None, stripped_thumb: bytes | None = None) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class ChatPhotoEmpty(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class ChatReactionsAll(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    allow_custom: Incomplete
    def __init__(self, allow_custom: bool | None = None) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class ChatReactionsNone(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class ChatReactionsSome(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    reactions: Incomplete
    def __init__(self, reactions: list['TypeReaction']) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class ClientDHInnerData(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    nonce: Incomplete
    server_nonce: Incomplete
    retry_id: Incomplete
    g_b: Incomplete
    def __init__(self, nonce: int, server_nonce: int, retry_id: int, g_b: bytes) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class CodeSettings(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    allow_flashcall: Incomplete
    current_number: Incomplete
    allow_app_hash: Incomplete
    allow_missed_call: Incomplete
    allow_firebase: Incomplete
    unknown_number: Incomplete
    logout_tokens: Incomplete
    token: Incomplete
    app_sandbox: Incomplete
    def __init__(self, allow_flashcall: bool | None = None, current_number: bool | None = None, allow_app_hash: bool | None = None, allow_missed_call: bool | None = None, allow_firebase: bool | None = None, unknown_number: bool | None = None, logout_tokens: list[bytes] | None = None, token: str | None = None, app_sandbox: bool | None = None) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class Config(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    date: Incomplete
    expires: Incomplete
    test_mode: Incomplete
    this_dc: Incomplete
    dc_options: Incomplete
    dc_txt_domain_name: Incomplete
    chat_size_max: Incomplete
    megagroup_size_max: Incomplete
    forwarded_count_max: Incomplete
    online_update_period_ms: Incomplete
    offline_blur_timeout_ms: Incomplete
    offline_idle_timeout_ms: Incomplete
    online_cloud_timeout_ms: Incomplete
    notify_cloud_delay_ms: Incomplete
    notify_default_delay_ms: Incomplete
    push_chat_period_ms: Incomplete
    push_chat_limit: Incomplete
    edit_time_limit: Incomplete
    revoke_time_limit: Incomplete
    revoke_pm_time_limit: Incomplete
    rating_e_decay: Incomplete
    stickers_recent_limit: Incomplete
    channels_read_media_period: Incomplete
    call_receive_timeout_ms: Incomplete
    call_ring_timeout_ms: Incomplete
    call_connect_timeout_ms: Incomplete
    call_packet_timeout_ms: Incomplete
    me_url_prefix: Incomplete
    caption_length_max: Incomplete
    message_length_max: Incomplete
    webfile_dc_id: Incomplete
    default_p2p_contacts: Incomplete
    preload_featured_stickers: Incomplete
    revoke_pm_inbox: Incomplete
    blocked_mode: Incomplete
    force_try_ipv6: Incomplete
    tmp_sessions: Incomplete
    autoupdate_url_prefix: Incomplete
    gif_search_username: Incomplete
    venue_search_username: Incomplete
    img_search_username: Incomplete
    static_maps_provider: Incomplete
    suggested_lang_code: Incomplete
    lang_pack_version: Incomplete
    base_lang_pack_version: Incomplete
    reactions_default: Incomplete
    autologin_token: Incomplete
    def __init__(self, date: datetime | None, expires: datetime | None, test_mode: bool, this_dc: int, dc_options: list['TypeDcOption'], dc_txt_domain_name: str, chat_size_max: int, megagroup_size_max: int, forwarded_count_max: int, online_update_period_ms: int, offline_blur_timeout_ms: int, offline_idle_timeout_ms: int, online_cloud_timeout_ms: int, notify_cloud_delay_ms: int, notify_default_delay_ms: int, push_chat_period_ms: int, push_chat_limit: int, edit_time_limit: int, revoke_time_limit: int, revoke_pm_time_limit: int, rating_e_decay: int, stickers_recent_limit: int, channels_read_media_period: int, call_receive_timeout_ms: int, call_ring_timeout_ms: int, call_connect_timeout_ms: int, call_packet_timeout_ms: int, me_url_prefix: str, caption_length_max: int, message_length_max: int, webfile_dc_id: int, default_p2p_contacts: bool | None = None, preload_featured_stickers: bool | None = None, revoke_pm_inbox: bool | None = None, blocked_mode: bool | None = None, force_try_ipv6: bool | None = None, tmp_sessions: int | None = None, autoupdate_url_prefix: str | None = None, gif_search_username: str | None = None, venue_search_username: str | None = None, img_search_username: str | None = None, static_maps_provider: str | None = None, suggested_lang_code: str | None = None, lang_pack_version: int | None = None, base_lang_pack_version: int | None = None, reactions_default: TypeReaction | None = None, autologin_token: str | None = None) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class ConnectedBot(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    bot_id: Incomplete
    recipients: Incomplete
    can_reply: Incomplete
    def __init__(self, bot_id: int, recipients: TypeBusinessBotRecipients, can_reply: bool | None = None) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class Contact(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    user_id: Incomplete
    mutual: Incomplete
    def __init__(self, user_id: int, mutual: bool) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class ContactBirthday(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    contact_id: Incomplete
    birthday: Incomplete
    def __init__(self, contact_id: int, birthday: TypeBirthday) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class ContactStatus(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    user_id: Incomplete
    status: Incomplete
    def __init__(self, user_id: int, status: TypeUserStatus) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class DataJSON(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    data: Incomplete
    def __init__(self, data: str) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class DcOption(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    id: Incomplete
    ip_address: Incomplete
    port: Incomplete
    ipv6: Incomplete
    media_only: Incomplete
    tcpo_only: Incomplete
    cdn: Incomplete
    static: Incomplete
    this_port_only: Incomplete
    secret: Incomplete
    def __init__(self, id: int, ip_address: str, port: int, ipv6: bool | None = None, media_only: bool | None = None, tcpo_only: bool | None = None, cdn: bool | None = None, static: bool | None = None, this_port_only: bool | None = None, secret: bytes | None = None) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class DefaultHistoryTTL(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    period: Incomplete
    def __init__(self, period: int) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class DestroyAuthKeyFail(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class DestroyAuthKeyNone(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class DestroyAuthKeyOk(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class DestroySessionNone(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    session_id: Incomplete
    def __init__(self, session_id: int) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class DestroySessionOk(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    session_id: Incomplete
    def __init__(self, session_id: int) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class DhGenFail(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    nonce: Incomplete
    server_nonce: Incomplete
    new_nonce_hash3: Incomplete
    def __init__(self, nonce: int, server_nonce: int, new_nonce_hash3: int) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class DhGenOk(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    nonce: Incomplete
    server_nonce: Incomplete
    new_nonce_hash1: Incomplete
    def __init__(self, nonce: int, server_nonce: int, new_nonce_hash1: int) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class DhGenRetry(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    nonce: Incomplete
    server_nonce: Incomplete
    new_nonce_hash2: Incomplete
    def __init__(self, nonce: int, server_nonce: int, new_nonce_hash2: int) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class Dialog(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    peer: Incomplete
    top_message: Incomplete
    read_inbox_max_id: Incomplete
    read_outbox_max_id: Incomplete
    unread_count: Incomplete
    unread_mentions_count: Incomplete
    unread_reactions_count: Incomplete
    notify_settings: Incomplete
    pinned: Incomplete
    unread_mark: Incomplete
    view_forum_as_messages: Incomplete
    pts: Incomplete
    draft: Incomplete
    folder_id: Incomplete
    ttl_period: Incomplete
    def __init__(self, peer: TypePeer, top_message: int, read_inbox_max_id: int, read_outbox_max_id: int, unread_count: int, unread_mentions_count: int, unread_reactions_count: int, notify_settings: TypePeerNotifySettings, pinned: bool | None = None, unread_mark: bool | None = None, view_forum_as_messages: bool | None = None, pts: int | None = None, draft: TypeDraftMessage | None = None, folder_id: int | None = None, ttl_period: int | None = None) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class DialogFilter(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    id: Incomplete
    title: Incomplete
    pinned_peers: Incomplete
    include_peers: Incomplete
    exclude_peers: Incomplete
    contacts: Incomplete
    non_contacts: Incomplete
    groups: Incomplete
    broadcasts: Incomplete
    bots: Incomplete
    exclude_muted: Incomplete
    exclude_read: Incomplete
    exclude_archived: Incomplete
    emoticon: Incomplete
    color: Incomplete
    def __init__(self, id: int, title: str, pinned_peers: list['TypeInputPeer'], include_peers: list['TypeInputPeer'], exclude_peers: list['TypeInputPeer'], contacts: bool | None = None, non_contacts: bool | None = None, groups: bool | None = None, broadcasts: bool | None = None, bots: bool | None = None, exclude_muted: bool | None = None, exclude_read: bool | None = None, exclude_archived: bool | None = None, emoticon: str | None = None, color: int | None = None) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class DialogFilterChatlist(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    id: Incomplete
    title: Incomplete
    pinned_peers: Incomplete
    include_peers: Incomplete
    has_my_invites: Incomplete
    emoticon: Incomplete
    color: Incomplete
    def __init__(self, id: int, title: str, pinned_peers: list['TypeInputPeer'], include_peers: list['TypeInputPeer'], has_my_invites: bool | None = None, emoticon: str | None = None, color: int | None = None) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class DialogFilterDefault(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class DialogFilterSuggested(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    filter: Incomplete
    description: Incomplete
    def __init__(self, filter: TypeDialogFilter, description: str) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class DialogFolder(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    folder: Incomplete
    peer: Incomplete
    top_message: Incomplete
    unread_muted_peers_count: Incomplete
    unread_unmuted_peers_count: Incomplete
    unread_muted_messages_count: Incomplete
    unread_unmuted_messages_count: Incomplete
    pinned: Incomplete
    def __init__(self, folder: TypeFolder, peer: TypePeer, top_message: int, unread_muted_peers_count: int, unread_unmuted_peers_count: int, unread_muted_messages_count: int, unread_unmuted_messages_count: int, pinned: bool | None = None) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class DialogPeer(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    peer: Incomplete
    def __init__(self, peer: TypePeer) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class DialogPeerFolder(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    folder_id: Incomplete
    def __init__(self, folder_id: int) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class Document(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    id: Incomplete
    access_hash: Incomplete
    file_reference: Incomplete
    date: Incomplete
    mime_type: Incomplete
    size: Incomplete
    dc_id: Incomplete
    attributes: Incomplete
    thumbs: Incomplete
    video_thumbs: Incomplete
    def __init__(self, id: int, access_hash: int, file_reference: bytes, date: datetime | None, mime_type: str, size: int, dc_id: int, attributes: list['TypeDocumentAttribute'], thumbs: list['TypePhotoSize'] | None = None, video_thumbs: list['TypeVideoSize'] | None = None) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class DocumentAttributeAnimated(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class DocumentAttributeAudio(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    duration: Incomplete
    voice: Incomplete
    title: Incomplete
    performer: Incomplete
    waveform: Incomplete
    def __init__(self, duration: int, voice: bool | None = None, title: str | None = None, performer: str | None = None, waveform: bytes | None = None) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class DocumentAttributeCustomEmoji(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    alt: Incomplete
    stickerset: Incomplete
    free: Incomplete
    text_color: Incomplete
    def __init__(self, alt: str, stickerset: TypeInputStickerSet, free: bool | None = None, text_color: bool | None = None) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class DocumentAttributeFilename(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    file_name: Incomplete
    def __init__(self, file_name: str) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class DocumentAttributeHasStickers(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class DocumentAttributeImageSize(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    w: Incomplete
    h: Incomplete
    def __init__(self, w: int, h: int) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class DocumentAttributeSticker(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    alt: Incomplete
    stickerset: Incomplete
    mask: Incomplete
    mask_coords: Incomplete
    def __init__(self, alt: str, stickerset: TypeInputStickerSet, mask: bool | None = None, mask_coords: TypeMaskCoords | None = None) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class DocumentAttributeVideo(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    duration: Incomplete
    w: Incomplete
    h: Incomplete
    round_message: Incomplete
    supports_streaming: Incomplete
    nosound: Incomplete
    preload_prefix_size: Incomplete
    video_start_ts: Incomplete
    video_codec: Incomplete
    def __init__(self, duration: float, w: int, h: int, round_message: bool | None = None, supports_streaming: bool | None = None, nosound: bool | None = None, preload_prefix_size: int | None = None, video_start_ts: float | None = None, video_codec: str | None = None) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class DocumentEmpty(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    id: Incomplete
    def __init__(self, id: int) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class DraftMessage(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    message: Incomplete
    date: Incomplete
    no_webpage: Incomplete
    invert_media: Incomplete
    reply_to: Incomplete
    entities: Incomplete
    media: Incomplete
    effect: Incomplete
    def __init__(self, message: str, date: datetime | None, no_webpage: bool | None = None, invert_media: bool | None = None, reply_to: TypeInputReplyTo | None = None, entities: list['TypeMessageEntity'] | None = None, media: TypeInputMedia | None = None, effect: int | None = None) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class DraftMessageEmpty(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    date: Incomplete
    def __init__(self, date: datetime | None = None) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class EmailVerificationApple(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    token: Incomplete
    def __init__(self, token: str) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class EmailVerificationCode(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    code: Incomplete
    def __init__(self, code: str) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class EmailVerificationGoogle(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    token: Incomplete
    def __init__(self, token: str) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class EmailVerifyPurposeLoginChange(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class EmailVerifyPurposeLoginSetup(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    phone_number: Incomplete
    phone_code_hash: Incomplete
    def __init__(self, phone_number: str, phone_code_hash: str) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class EmailVerifyPurposePassport(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class EmojiGroup(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    title: Incomplete
    icon_emoji_id: Incomplete
    emoticons: Incomplete
    def __init__(self, title: str, icon_emoji_id: int, emoticons: list[str]) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class EmojiGroupGreeting(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    title: Incomplete
    icon_emoji_id: Incomplete
    emoticons: Incomplete
    def __init__(self, title: str, icon_emoji_id: int, emoticons: list[str]) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class EmojiGroupPremium(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    title: Incomplete
    icon_emoji_id: Incomplete
    def __init__(self, title: str, icon_emoji_id: int) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class EmojiKeyword(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    keyword: Incomplete
    emoticons: Incomplete
    def __init__(self, keyword: str, emoticons: list[str]) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class EmojiKeywordDeleted(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    keyword: Incomplete
    emoticons: Incomplete
    def __init__(self, keyword: str, emoticons: list[str]) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class EmojiKeywordsDifference(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    lang_code: Incomplete
    from_version: Incomplete
    version: Incomplete
    keywords: Incomplete
    def __init__(self, lang_code: str, from_version: int, version: int, keywords: list['TypeEmojiKeyword']) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class EmojiLanguage(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    lang_code: Incomplete
    def __init__(self, lang_code: str) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class EmojiList(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    hash: Incomplete
    document_id: Incomplete
    def __init__(self, hash: int, document_id: list[int]) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class EmojiListNotModified(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class EmojiStatus(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    document_id: Incomplete
    def __init__(self, document_id: int) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class EmojiStatusEmpty(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class EmojiStatusUntil(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    document_id: Incomplete
    until: Incomplete
    def __init__(self, document_id: int, until: datetime | None) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class EmojiURL(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    url: Incomplete
    def __init__(self, url: str) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class EncryptedChat(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    id: Incomplete
    access_hash: Incomplete
    date: Incomplete
    admin_id: Incomplete
    participant_id: Incomplete
    g_a_or_b: Incomplete
    key_fingerprint: Incomplete
    def __init__(self, id: int, access_hash: int, date: datetime | None, admin_id: int, participant_id: int, g_a_or_b: bytes, key_fingerprint: int) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class EncryptedChatDiscarded(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    id: Incomplete
    history_deleted: Incomplete
    def __init__(self, id: int, history_deleted: bool | None = None) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class EncryptedChatEmpty(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    id: Incomplete
    def __init__(self, id: int) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class EncryptedChatRequested(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    id: Incomplete
    access_hash: Incomplete
    date: Incomplete
    admin_id: Incomplete
    participant_id: Incomplete
    g_a: Incomplete
    folder_id: Incomplete
    def __init__(self, id: int, access_hash: int, date: datetime | None, admin_id: int, participant_id: int, g_a: bytes, folder_id: int | None = None) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class EncryptedChatWaiting(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    id: Incomplete
    access_hash: Incomplete
    date: Incomplete
    admin_id: Incomplete
    participant_id: Incomplete
    def __init__(self, id: int, access_hash: int, date: datetime | None, admin_id: int, participant_id: int) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class EncryptedFile(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    id: Incomplete
    access_hash: Incomplete
    size: Incomplete
    dc_id: Incomplete
    key_fingerprint: Incomplete
    def __init__(self, id: int, access_hash: int, size: int, dc_id: int, key_fingerprint: int) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class EncryptedFileEmpty(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class EncryptedMessage(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    chat_id: Incomplete
    date: Incomplete
    bytes: Incomplete
    file: Incomplete
    random_id: Incomplete
    def __init__(self, chat_id: int, date: datetime | None, bytes: bytes, file: TypeEncryptedFile, random_id: int = None) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class EncryptedMessageService(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    chat_id: Incomplete
    date: Incomplete
    bytes: Incomplete
    random_id: Incomplete
    def __init__(self, chat_id: int, date: datetime | None, bytes: bytes, random_id: int = None) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class ExportedChatlistInvite(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    title: Incomplete
    url: Incomplete
    peers: Incomplete
    def __init__(self, title: str, url: str, peers: list['TypePeer']) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class ExportedContactToken(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    url: Incomplete
    expires: Incomplete
    def __init__(self, url: str, expires: datetime | None) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class ExportedMessageLink(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    link: Incomplete
    html: Incomplete
    def __init__(self, link: str, html: str) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class ExportedStoryLink(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    link: Incomplete
    def __init__(self, link: str) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class FactCheck(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    hash: Incomplete
    need_check: Incomplete
    country: Incomplete
    text: Incomplete
    def __init__(self, hash: int, need_check: bool | None = None, country: str | None = None, text: TypeTextWithEntities | None = None) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class FileHash(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    offset: Incomplete
    limit: Incomplete
    hash: Incomplete
    def __init__(self, offset: int, limit: int, hash: bytes) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class Folder(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    id: Incomplete
    title: Incomplete
    autofill_new_broadcasts: Incomplete
    autofill_public_groups: Incomplete
    autofill_new_correspondents: Incomplete
    photo: Incomplete
    def __init__(self, id: int, title: str, autofill_new_broadcasts: bool | None = None, autofill_public_groups: bool | None = None, autofill_new_correspondents: bool | None = None, photo: TypeChatPhoto | None = None) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class FolderPeer(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    peer: Incomplete
    folder_id: Incomplete
    def __init__(self, peer: TypePeer, folder_id: int) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class ForumTopic(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    id: Incomplete
    date: Incomplete
    title: Incomplete
    icon_color: Incomplete
    top_message: Incomplete
    read_inbox_max_id: Incomplete
    read_outbox_max_id: Incomplete
    unread_count: Incomplete
    unread_mentions_count: Incomplete
    unread_reactions_count: Incomplete
    from_id: Incomplete
    notify_settings: Incomplete
    my: Incomplete
    closed: Incomplete
    pinned: Incomplete
    short: Incomplete
    hidden: Incomplete
    icon_emoji_id: Incomplete
    draft: Incomplete
    def __init__(self, id: int, date: datetime | None, title: str, icon_color: int, top_message: int, read_inbox_max_id: int, read_outbox_max_id: int, unread_count: int, unread_mentions_count: int, unread_reactions_count: int, from_id: TypePeer, notify_settings: TypePeerNotifySettings, my: bool | None = None, closed: bool | None = None, pinned: bool | None = None, short: bool | None = None, hidden: bool | None = None, icon_emoji_id: int | None = None, draft: TypeDraftMessage | None = None) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class ForumTopicDeleted(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    id: Incomplete
    def __init__(self, id: int) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class FoundStory(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    peer: Incomplete
    story: Incomplete
    def __init__(self, peer: TypePeer, story: TypeStoryItem) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class FutureSalt(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    valid_since: Incomplete
    valid_until: Incomplete
    salt: Incomplete
    def __init__(self, valid_since: datetime | None, valid_until: datetime | None, salt: int) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class FutureSalts(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    req_msg_id: Incomplete
    now: Incomplete
    salts: Incomplete
    def __init__(self, req_msg_id: int, now: int, salts: list['Typefuture_salt']) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class Game(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    id: Incomplete
    access_hash: Incomplete
    short_name: Incomplete
    title: Incomplete
    description: Incomplete
    photo: Incomplete
    document: Incomplete
    def __init__(self, id: int, access_hash: int, short_name: str, title: str, description: str, photo: TypePhoto, document: TypeDocument | None = None) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class GeoPoint(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    long: Incomplete
    lat: Incomplete
    access_hash: Incomplete
    accuracy_radius: Incomplete
    def __init__(self, long: float, lat: float, access_hash: int, accuracy_radius: int | None = None) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class GeoPointAddress(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    country_iso2: Incomplete
    state: Incomplete
    city: Incomplete
    street: Incomplete
    def __init__(self, country_iso2: str, state: str | None = None, city: str | None = None, street: str | None = None) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class GeoPointEmpty(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class GlobalPrivacySettings(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    archive_and_mute_new_noncontact_peers: Incomplete
    keep_archived_unmuted: Incomplete
    keep_archived_folders: Incomplete
    hide_read_marks: Incomplete
    new_noncontact_peers_require_premium: Incomplete
    def __init__(self, archive_and_mute_new_noncontact_peers: bool | None = None, keep_archived_unmuted: bool | None = None, keep_archived_folders: bool | None = None, hide_read_marks: bool | None = None, new_noncontact_peers_require_premium: bool | None = None) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class GroupCall(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    id: Incomplete
    access_hash: Incomplete
    participants_count: Incomplete
    unmuted_video_limit: Incomplete
    version: Incomplete
    join_muted: Incomplete
    can_change_join_muted: Incomplete
    join_date_asc: Incomplete
    schedule_start_subscribed: Incomplete
    can_start_video: Incomplete
    record_video_active: Incomplete
    rtmp_stream: Incomplete
    listeners_hidden: Incomplete
    title: Incomplete
    stream_dc_id: Incomplete
    record_start_date: Incomplete
    schedule_date: Incomplete
    unmuted_video_count: Incomplete
    def __init__(self, id: int, access_hash: int, participants_count: int, unmuted_video_limit: int, version: int, join_muted: bool | None = None, can_change_join_muted: bool | None = None, join_date_asc: bool | None = None, schedule_start_subscribed: bool | None = None, can_start_video: bool | None = None, record_video_active: bool | None = None, rtmp_stream: bool | None = None, listeners_hidden: bool | None = None, title: str | None = None, stream_dc_id: int | None = None, record_start_date: datetime | None = None, schedule_date: datetime | None = None, unmuted_video_count: int | None = None) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class GroupCallDiscarded(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    id: Incomplete
    access_hash: Incomplete
    duration: Incomplete
    def __init__(self, id: int, access_hash: int, duration: int) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class GroupCallParticipant(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    peer: Incomplete
    date: Incomplete
    source: Incomplete
    muted: Incomplete
    left: Incomplete
    can_self_unmute: Incomplete
    just_joined: Incomplete
    versioned: Incomplete
    min: Incomplete
    muted_by_you: Incomplete
    volume_by_admin: Incomplete
    is_self: Incomplete
    video_joined: Incomplete
    active_date: Incomplete
    volume: Incomplete
    about: Incomplete
    raise_hand_rating: Incomplete
    video: Incomplete
    presentation: Incomplete
    def __init__(self, peer: TypePeer, date: datetime | None, source: int, muted: bool | None = None, left: bool | None = None, can_self_unmute: bool | None = None, just_joined: bool | None = None, versioned: bool | None = None, min: bool | None = None, muted_by_you: bool | None = None, volume_by_admin: bool | None = None, is_self: bool | None = None, video_joined: bool | None = None, active_date: datetime | None = None, volume: int | None = None, about: str | None = None, raise_hand_rating: int | None = None, video: TypeGroupCallParticipantVideo | None = None, presentation: TypeGroupCallParticipantVideo | None = None) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class GroupCallParticipantVideo(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    endpoint: Incomplete
    source_groups: Incomplete
    paused: Incomplete
    audio_source: Incomplete
    def __init__(self, endpoint: str, source_groups: list['TypeGroupCallParticipantVideoSourceGroup'], paused: bool | None = None, audio_source: int | None = None) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class GroupCallParticipantVideoSourceGroup(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    semantics: Incomplete
    sources: Incomplete
    def __init__(self, semantics: str, sources: list[int]) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class GroupCallStreamChannel(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    channel: Incomplete
    scale: Incomplete
    last_timestamp_ms: Incomplete
    def __init__(self, channel: int, scale: int, last_timestamp_ms: int) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class HighScore(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    pos: Incomplete
    user_id: Incomplete
    score: Incomplete
    def __init__(self, pos: int, user_id: int, score: int) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class HttpWait(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    max_delay: Incomplete
    wait_after: Incomplete
    max_wait: Incomplete
    def __init__(self, max_delay: int, wait_after: int, max_wait: int) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class ImportedContact(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    user_id: Incomplete
    client_id: Incomplete
    def __init__(self, user_id: int, client_id: int) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class InlineBotSwitchPM(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    text: Incomplete
    start_param: Incomplete
    def __init__(self, text: str, start_param: str) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class InlineBotWebView(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    text: Incomplete
    url: Incomplete
    def __init__(self, text: str, url: str) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class InlineQueryPeerTypeBotPM(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class InlineQueryPeerTypeBroadcast(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class InlineQueryPeerTypeChat(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class InlineQueryPeerTypeMegagroup(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class InlineQueryPeerTypePM(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class InlineQueryPeerTypeSameBotPM(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class InputAppEvent(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    time: Incomplete
    type: Incomplete
    peer: Incomplete
    data: Incomplete
    def __init__(self, time: float, type: str, peer: int, data: TypeJSONValue) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class InputBotAppID(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    id: Incomplete
    access_hash: Incomplete
    def __init__(self, id: int, access_hash: int) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class InputBotAppShortName(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    bot_id: Incomplete
    short_name: Incomplete
    def __init__(self, bot_id: TypeInputUser, short_name: str) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class InputBotInlineMessageGame(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    reply_markup: Incomplete
    def __init__(self, reply_markup: TypeReplyMarkup | None = None) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class InputBotInlineMessageID(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    dc_id: Incomplete
    id: Incomplete
    access_hash: Incomplete
    def __init__(self, dc_id: int, id: int, access_hash: int) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class InputBotInlineMessageID64(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    dc_id: Incomplete
    owner_id: Incomplete
    id: Incomplete
    access_hash: Incomplete
    def __init__(self, dc_id: int, owner_id: int, id: int, access_hash: int) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class InputBotInlineMessageMediaAuto(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    message: Incomplete
    invert_media: Incomplete
    entities: Incomplete
    reply_markup: Incomplete
    def __init__(self, message: str, invert_media: bool | None = None, entities: list['TypeMessageEntity'] | None = None, reply_markup: TypeReplyMarkup | None = None) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class InputBotInlineMessageMediaContact(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    phone_number: Incomplete
    first_name: Incomplete
    last_name: Incomplete
    vcard: Incomplete
    reply_markup: Incomplete
    def __init__(self, phone_number: str, first_name: str, last_name: str, vcard: str, reply_markup: TypeReplyMarkup | None = None) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class InputBotInlineMessageMediaGeo(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    geo_point: Incomplete
    heading: Incomplete
    period: Incomplete
    proximity_notification_radius: Incomplete
    reply_markup: Incomplete
    def __init__(self, geo_point: TypeInputGeoPoint, heading: int | None = None, period: int | None = None, proximity_notification_radius: int | None = None, reply_markup: TypeReplyMarkup | None = None) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class InputBotInlineMessageMediaInvoice(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    title: Incomplete
    description: Incomplete
    invoice: Incomplete
    payload: Incomplete
    provider: Incomplete
    provider_data: Incomplete
    photo: Incomplete
    reply_markup: Incomplete
    def __init__(self, title: str, description: str, invoice: TypeInvoice, payload: bytes, provider: str, provider_data: TypeDataJSON, photo: TypeInputWebDocument | None = None, reply_markup: TypeReplyMarkup | None = None) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class InputBotInlineMessageMediaVenue(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    geo_point: Incomplete
    title: Incomplete
    address: Incomplete
    provider: Incomplete
    venue_id: Incomplete
    venue_type: Incomplete
    reply_markup: Incomplete
    def __init__(self, geo_point: TypeInputGeoPoint, title: str, address: str, provider: str, venue_id: str, venue_type: str, reply_markup: TypeReplyMarkup | None = None) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class InputBotInlineMessageMediaWebPage(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    message: Incomplete
    url: Incomplete
    invert_media: Incomplete
    force_large_media: Incomplete
    force_small_media: Incomplete
    optional: Incomplete
    entities: Incomplete
    reply_markup: Incomplete
    def __init__(self, message: str, url: str, invert_media: bool | None = None, force_large_media: bool | None = None, force_small_media: bool | None = None, optional: bool | None = None, entities: list['TypeMessageEntity'] | None = None, reply_markup: TypeReplyMarkup | None = None) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class InputBotInlineMessageText(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    message: Incomplete
    no_webpage: Incomplete
    invert_media: Incomplete
    entities: Incomplete
    reply_markup: Incomplete
    def __init__(self, message: str, no_webpage: bool | None = None, invert_media: bool | None = None, entities: list['TypeMessageEntity'] | None = None, reply_markup: TypeReplyMarkup | None = None) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class InputBotInlineResult(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    id: Incomplete
    type: Incomplete
    send_message: Incomplete
    title: Incomplete
    description: Incomplete
    url: Incomplete
    thumb: Incomplete
    content: Incomplete
    def __init__(self, id: str, type: str, send_message: TypeInputBotInlineMessage, title: str | None = None, description: str | None = None, url: str | None = None, thumb: TypeInputWebDocument | None = None, content: TypeInputWebDocument | None = None) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class InputBotInlineResultDocument(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    id: Incomplete
    type: Incomplete
    document: Incomplete
    send_message: Incomplete
    title: Incomplete
    description: Incomplete
    def __init__(self, id: str, type: str, document: TypeInputDocument, send_message: TypeInputBotInlineMessage, title: str | None = None, description: str | None = None) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class InputBotInlineResultGame(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    id: Incomplete
    short_name: Incomplete
    send_message: Incomplete
    def __init__(self, id: str, short_name: str, send_message: TypeInputBotInlineMessage) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class InputBotInlineResultPhoto(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    id: Incomplete
    type: Incomplete
    photo: Incomplete
    send_message: Incomplete
    def __init__(self, id: str, type: str, photo: TypeInputPhoto, send_message: TypeInputBotInlineMessage) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class InputBusinessAwayMessage(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    shortcut_id: Incomplete
    schedule: Incomplete
    recipients: Incomplete
    offline_only: Incomplete
    def __init__(self, shortcut_id: int, schedule: TypeBusinessAwayMessageSchedule, recipients: TypeInputBusinessRecipients, offline_only: bool | None = None) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class InputBusinessBotRecipients(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    existing_chats: Incomplete
    new_chats: Incomplete
    contacts: Incomplete
    non_contacts: Incomplete
    exclude_selected: Incomplete
    users: Incomplete
    exclude_users: Incomplete
    def __init__(self, existing_chats: bool | None = None, new_chats: bool | None = None, contacts: bool | None = None, non_contacts: bool | None = None, exclude_selected: bool | None = None, users: list['TypeInputUser'] | None = None, exclude_users: list['TypeInputUser'] | None = None) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class InputBusinessChatLink(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    message: Incomplete
    entities: Incomplete
    title: Incomplete
    def __init__(self, message: str, entities: list['TypeMessageEntity'] | None = None, title: str | None = None) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class InputBusinessGreetingMessage(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    shortcut_id: Incomplete
    recipients: Incomplete
    no_activity_days: Incomplete
    def __init__(self, shortcut_id: int, recipients: TypeInputBusinessRecipients, no_activity_days: int) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class InputBusinessIntro(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    title: Incomplete
    description: Incomplete
    sticker: Incomplete
    def __init__(self, title: str, description: str, sticker: TypeInputDocument | None = None) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class InputBusinessRecipients(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    existing_chats: Incomplete
    new_chats: Incomplete
    contacts: Incomplete
    non_contacts: Incomplete
    exclude_selected: Incomplete
    users: Incomplete
    def __init__(self, existing_chats: bool | None = None, new_chats: bool | None = None, contacts: bool | None = None, non_contacts: bool | None = None, exclude_selected: bool | None = None, users: list['TypeInputUser'] | None = None) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class InputChannel(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    channel_id: Incomplete
    access_hash: Incomplete
    def __init__(self, channel_id: int, access_hash: int) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class InputChannelEmpty(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class InputChannelFromMessage(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    peer: Incomplete
    msg_id: Incomplete
    channel_id: Incomplete
    def __init__(self, peer: TypeInputPeer, msg_id: int, channel_id: int) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class InputChatPhoto(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    id: Incomplete
    def __init__(self, id: TypeInputPhoto) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class InputChatPhotoEmpty(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class InputChatUploadedPhoto(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    file: Incomplete
    video: Incomplete
    video_start_ts: Incomplete
    video_emoji_markup: Incomplete
    def __init__(self, file: TypeInputFile | None = None, video: TypeInputFile | None = None, video_start_ts: float | None = None, video_emoji_markup: TypeVideoSize | None = None) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class InputChatlistDialogFilter(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    filter_id: Incomplete
    def __init__(self, filter_id: int) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class InputCheckPasswordEmpty(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class InputCheckPasswordSRP(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    srp_id: Incomplete
    A: Incomplete
    M1: Incomplete
    def __init__(self, srp_id: int, A: bytes, M1: bytes) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class InputClientProxy(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    address: Incomplete
    port: Incomplete
    def __init__(self, address: str, port: int) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class InputCollectiblePhone(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    phone: Incomplete
    def __init__(self, phone: str) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class InputCollectibleUsername(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    username: Incomplete
    def __init__(self, username: str) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class InputDialogPeer(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    peer: Incomplete
    def __init__(self, peer: TypeInputPeer) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class InputDialogPeerFolder(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    folder_id: Incomplete
    def __init__(self, folder_id: int) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class InputDocument(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    id: Incomplete
    access_hash: Incomplete
    file_reference: Incomplete
    def __init__(self, id: int, access_hash: int, file_reference: bytes) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class InputDocumentEmpty(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class InputDocumentFileLocation(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    id: Incomplete
    access_hash: Incomplete
    file_reference: Incomplete
    thumb_size: Incomplete
    def __init__(self, id: int, access_hash: int, file_reference: bytes, thumb_size: str) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class InputEncryptedChat(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    chat_id: Incomplete
    access_hash: Incomplete
    def __init__(self, chat_id: int, access_hash: int) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class InputEncryptedFile(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    id: Incomplete
    access_hash: Incomplete
    def __init__(self, id: int, access_hash: int) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class InputEncryptedFileBigUploaded(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    id: Incomplete
    parts: Incomplete
    key_fingerprint: Incomplete
    def __init__(self, id: int, parts: int, key_fingerprint: int) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class InputEncryptedFileEmpty(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class InputEncryptedFileLocation(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    id: Incomplete
    access_hash: Incomplete
    def __init__(self, id: int, access_hash: int) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class InputEncryptedFileUploaded(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    id: Incomplete
    parts: Incomplete
    md5_checksum: Incomplete
    key_fingerprint: Incomplete
    def __init__(self, id: int, parts: int, md5_checksum: str, key_fingerprint: int) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class InputFile(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    id: Incomplete
    parts: Incomplete
    name: Incomplete
    md5_checksum: Incomplete
    def __init__(self, id: int, parts: int, name: str, md5_checksum: str) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class InputFileBig(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    id: Incomplete
    parts: Incomplete
    name: Incomplete
    def __init__(self, id: int, parts: int, name: str) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class InputFileLocation(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    volume_id: Incomplete
    local_id: Incomplete
    secret: Incomplete
    file_reference: Incomplete
    def __init__(self, volume_id: int, local_id: int, secret: int, file_reference: bytes) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class InputFileStoryDocument(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    id: Incomplete
    def __init__(self, id: TypeInputDocument) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class InputFolderPeer(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    peer: Incomplete
    folder_id: Incomplete
    def __init__(self, peer: TypeInputPeer, folder_id: int) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class InputGameID(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    id: Incomplete
    access_hash: Incomplete
    def __init__(self, id: int, access_hash: int) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class InputGameShortName(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    bot_id: Incomplete
    short_name: Incomplete
    def __init__(self, bot_id: TypeInputUser, short_name: str) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class InputGeoPoint(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    lat: Incomplete
    long: Incomplete
    accuracy_radius: Incomplete
    def __init__(self, lat: float, long: float, accuracy_radius: int | None = None) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class InputGeoPointEmpty(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class InputGroupCall(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    id: Incomplete
    access_hash: Incomplete
    def __init__(self, id: int, access_hash: int) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class InputGroupCallStream(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    call: Incomplete
    time_ms: Incomplete
    scale: Incomplete
    video_channel: Incomplete
    video_quality: Incomplete
    def __init__(self, call: TypeInputGroupCall, time_ms: int, scale: int, video_channel: int | None = None, video_quality: int | None = None) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class InputInvoiceChatInviteSubscription(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    hash: Incomplete
    def __init__(self, hash: str) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class InputInvoiceMessage(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    peer: Incomplete
    msg_id: Incomplete
    def __init__(self, peer: TypeInputPeer, msg_id: int) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class InputInvoicePremiumGiftCode(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    purpose: Incomplete
    option: Incomplete
    def __init__(self, purpose: TypeInputStorePaymentPurpose, option: TypePremiumGiftCodeOption) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class InputInvoiceSlug(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    slug: Incomplete
    def __init__(self, slug: str) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class InputInvoiceStarGift(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    user_id: Incomplete
    gift_id: Incomplete
    hide_name: Incomplete
    message: Incomplete
    def __init__(self, user_id: TypeInputUser, gift_id: int, hide_name: bool | None = None, message: TypeTextWithEntities | None = None) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class InputInvoiceStars(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    purpose: Incomplete
    def __init__(self, purpose: TypeInputStorePaymentPurpose) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class InputKeyboardButtonRequestPeer(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    text: Incomplete
    button_id: Incomplete
    peer_type: Incomplete
    max_quantity: Incomplete
    name_requested: Incomplete
    username_requested: Incomplete
    photo_requested: Incomplete
    def __init__(self, text: str, button_id: int, peer_type: TypeRequestPeerType, max_quantity: int, name_requested: bool | None = None, username_requested: bool | None = None, photo_requested: bool | None = None) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class InputKeyboardButtonUrlAuth(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    text: Incomplete
    url: Incomplete
    bot: Incomplete
    request_write_access: Incomplete
    fwd_text: Incomplete
    def __init__(self, text: str, url: str, bot: TypeInputUser, request_write_access: bool | None = None, fwd_text: str | None = None) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class InputKeyboardButtonUserProfile(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    text: Incomplete
    user_id: Incomplete
    def __init__(self, text: str, user_id: TypeInputUser) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class InputMediaAreaChannelPost(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    coordinates: Incomplete
    channel: Incomplete
    msg_id: Incomplete
    def __init__(self, coordinates: TypeMediaAreaCoordinates, channel: TypeInputChannel, msg_id: int) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class InputMediaAreaVenue(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    coordinates: Incomplete
    query_id: Incomplete
    result_id: Incomplete
    def __init__(self, coordinates: TypeMediaAreaCoordinates, query_id: int, result_id: str) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class InputMediaContact(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    phone_number: Incomplete
    first_name: Incomplete
    last_name: Incomplete
    vcard: Incomplete
    def __init__(self, phone_number: str, first_name: str, last_name: str, vcard: str) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class InputMediaDice(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    emoticon: Incomplete
    def __init__(self, emoticon: str) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class InputMediaDocument(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    id: Incomplete
    spoiler: Incomplete
    ttl_seconds: Incomplete
    query: Incomplete
    def __init__(self, id: TypeInputDocument, spoiler: bool | None = None, ttl_seconds: int | None = None, query: str | None = None) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class InputMediaDocumentExternal(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    url: Incomplete
    spoiler: Incomplete
    ttl_seconds: Incomplete
    def __init__(self, url: str, spoiler: bool | None = None, ttl_seconds: int | None = None) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class InputMediaEmpty(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class InputMediaGame(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    id: Incomplete
    def __init__(self, id: TypeInputGame) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class InputMediaGeoLive(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    geo_point: Incomplete
    stopped: Incomplete
    heading: Incomplete
    period: Incomplete
    proximity_notification_radius: Incomplete
    def __init__(self, geo_point: TypeInputGeoPoint, stopped: bool | None = None, heading: int | None = None, period: int | None = None, proximity_notification_radius: int | None = None) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class InputMediaGeoPoint(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    geo_point: Incomplete
    def __init__(self, geo_point: TypeInputGeoPoint) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class InputMediaInvoice(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    title: Incomplete
    description: Incomplete
    invoice: Incomplete
    payload: Incomplete
    provider_data: Incomplete
    photo: Incomplete
    provider: Incomplete
    start_param: Incomplete
    extended_media: Incomplete
    def __init__(self, title: str, description: str, invoice: TypeInvoice, payload: bytes, provider_data: TypeDataJSON, photo: TypeInputWebDocument | None = None, provider: str | None = None, start_param: str | None = None, extended_media: TypeInputMedia | None = None) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class InputMediaPaidMedia(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    stars_amount: Incomplete
    extended_media: Incomplete
    payload: Incomplete
    def __init__(self, stars_amount: int, extended_media: list['TypeInputMedia'], payload: str | None = None) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class InputMediaPhoto(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    id: Incomplete
    spoiler: Incomplete
    ttl_seconds: Incomplete
    def __init__(self, id: TypeInputPhoto, spoiler: bool | None = None, ttl_seconds: int | None = None) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class InputMediaPhotoExternal(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    url: Incomplete
    spoiler: Incomplete
    ttl_seconds: Incomplete
    def __init__(self, url: str, spoiler: bool | None = None, ttl_seconds: int | None = None) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class InputMediaPoll(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    poll: Incomplete
    correct_answers: Incomplete
    solution: Incomplete
    solution_entities: Incomplete
    def __init__(self, poll: TypePoll, correct_answers: list[bytes] | None = None, solution: str | None = None, solution_entities: list['TypeMessageEntity'] | None = None) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class InputMediaStory(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    peer: Incomplete
    id: Incomplete
    def __init__(self, peer: TypeInputPeer, id: int) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class InputMediaUploadedDocument(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    file: Incomplete
    mime_type: Incomplete
    attributes: Incomplete
    nosound_video: Incomplete
    force_file: Incomplete
    spoiler: Incomplete
    thumb: Incomplete
    stickers: Incomplete
    ttl_seconds: Incomplete
    def __init__(self, file: TypeInputFile, mime_type: str, attributes: list['TypeDocumentAttribute'], nosound_video: bool | None = None, force_file: bool | None = None, spoiler: bool | None = None, thumb: TypeInputFile | None = None, stickers: list['TypeInputDocument'] | None = None, ttl_seconds: int | None = None) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class InputMediaUploadedPhoto(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    file: Incomplete
    spoiler: Incomplete
    stickers: Incomplete
    ttl_seconds: Incomplete
    def __init__(self, file: TypeInputFile, spoiler: bool | None = None, stickers: list['TypeInputDocument'] | None = None, ttl_seconds: int | None = None) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class InputMediaVenue(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    geo_point: Incomplete
    title: Incomplete
    address: Incomplete
    provider: Incomplete
    venue_id: Incomplete
    venue_type: Incomplete
    def __init__(self, geo_point: TypeInputGeoPoint, title: str, address: str, provider: str, venue_id: str, venue_type: str) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class InputMediaWebPage(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    url: Incomplete
    force_large_media: Incomplete
    force_small_media: Incomplete
    optional: Incomplete
    def __init__(self, url: str, force_large_media: bool | None = None, force_small_media: bool | None = None, optional: bool | None = None) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class InputMessageCallbackQuery(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    id: Incomplete
    query_id: Incomplete
    def __init__(self, id: int, query_id: int) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class InputMessageEntityMentionName(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    offset: Incomplete
    length: Incomplete
    user_id: Incomplete
    def __init__(self, offset: int, length: int, user_id: TypeInputUser) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class InputMessageID(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    id: Incomplete
    def __init__(self, id: int) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class InputMessagePinned(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class InputMessageReplyTo(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    id: Incomplete
    def __init__(self, id: int) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class InputMessagesFilterChatPhotos(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class InputMessagesFilterContacts(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class InputMessagesFilterDocument(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class InputMessagesFilterEmpty(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class InputMessagesFilterGeo(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class InputMessagesFilterGif(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class InputMessagesFilterMusic(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class InputMessagesFilterMyMentions(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class InputMessagesFilterPhoneCalls(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    missed: Incomplete
    def __init__(self, missed: bool | None = None) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class InputMessagesFilterPhotoVideo(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class InputMessagesFilterPhotos(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class InputMessagesFilterPinned(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class InputMessagesFilterRoundVideo(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class InputMessagesFilterRoundVoice(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class InputMessagesFilterUrl(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class InputMessagesFilterVideo(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class InputMessagesFilterVoice(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class InputNotifyBroadcasts(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class InputNotifyChats(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class InputNotifyForumTopic(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    peer: Incomplete
    top_msg_id: Incomplete
    def __init__(self, peer: TypeInputPeer, top_msg_id: int) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class InputNotifyPeer(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    peer: Incomplete
    def __init__(self, peer: TypeInputPeer) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class InputNotifyUsers(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class InputPaymentCredentials(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    data: Incomplete
    save: Incomplete
    def __init__(self, data: TypeDataJSON, save: bool | None = None) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class InputPaymentCredentialsApplePay(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    payment_data: Incomplete
    def __init__(self, payment_data: TypeDataJSON) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class InputPaymentCredentialsGooglePay(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    payment_token: Incomplete
    def __init__(self, payment_token: TypeDataJSON) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class InputPaymentCredentialsSaved(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    id: Incomplete
    tmp_password: Incomplete
    def __init__(self, id: str, tmp_password: bytes) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class InputPeerChannel(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    channel_id: Incomplete
    access_hash: Incomplete
    def __init__(self, channel_id: int, access_hash: int) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class InputPeerChannelFromMessage(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    peer: Incomplete
    msg_id: Incomplete
    channel_id: Incomplete
    def __init__(self, peer: TypeInputPeer, msg_id: int, channel_id: int) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class InputPeerChat(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    chat_id: Incomplete
    def __init__(self, chat_id: int) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class InputPeerEmpty(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class InputPeerNotifySettings(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    show_previews: Incomplete
    silent: Incomplete
    mute_until: Incomplete
    sound: Incomplete
    stories_muted: Incomplete
    stories_hide_sender: Incomplete
    stories_sound: Incomplete
    def __init__(self, show_previews: bool | None = None, silent: bool | None = None, mute_until: datetime | None = None, sound: TypeNotificationSound | None = None, stories_muted: bool | None = None, stories_hide_sender: bool | None = None, stories_sound: TypeNotificationSound | None = None) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class InputPeerPhotoFileLocation(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    peer: Incomplete
    photo_id: Incomplete
    big: Incomplete
    def __init__(self, peer: TypeInputPeer, photo_id: int, big: bool | None = None) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class InputPeerSelf(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class InputPeerUser(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    user_id: Incomplete
    access_hash: Incomplete
    def __init__(self, user_id: int, access_hash: int) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class InputPeerUserFromMessage(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    peer: Incomplete
    msg_id: Incomplete
    user_id: Incomplete
    def __init__(self, peer: TypeInputPeer, msg_id: int, user_id: int) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class InputPhoneCall(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    id: Incomplete
    access_hash: Incomplete
    def __init__(self, id: int, access_hash: int) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class InputPhoneContact(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    client_id: Incomplete
    phone: Incomplete
    first_name: Incomplete
    last_name: Incomplete
    def __init__(self, client_id: int, phone: str, first_name: str, last_name: str) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class InputPhoto(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    id: Incomplete
    access_hash: Incomplete
    file_reference: Incomplete
    def __init__(self, id: int, access_hash: int, file_reference: bytes) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class InputPhotoEmpty(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class InputPhotoFileLocation(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    id: Incomplete
    access_hash: Incomplete
    file_reference: Incomplete
    thumb_size: Incomplete
    def __init__(self, id: int, access_hash: int, file_reference: bytes, thumb_size: str) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class InputPhotoLegacyFileLocation(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    id: Incomplete
    access_hash: Incomplete
    file_reference: Incomplete
    volume_id: Incomplete
    local_id: Incomplete
    secret: Incomplete
    def __init__(self, id: int, access_hash: int, file_reference: bytes, volume_id: int, local_id: int, secret: int) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class InputPrivacyKeyAbout(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class InputPrivacyKeyAddedByPhone(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class InputPrivacyKeyBirthday(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class InputPrivacyKeyChatInvite(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class InputPrivacyKeyForwards(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class InputPrivacyKeyPhoneCall(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class InputPrivacyKeyPhoneNumber(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class InputPrivacyKeyPhoneP2P(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class InputPrivacyKeyProfilePhoto(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class InputPrivacyKeyStarGiftsAutoSave(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class InputPrivacyKeyStatusTimestamp(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class InputPrivacyKeyVoiceMessages(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class InputPrivacyValueAllowAll(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class InputPrivacyValueAllowBots(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class InputPrivacyValueAllowChatParticipants(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    chats: Incomplete
    def __init__(self, chats: list[int]) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class InputPrivacyValueAllowCloseFriends(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class InputPrivacyValueAllowContacts(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class InputPrivacyValueAllowPremium(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class InputPrivacyValueAllowUsers(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    users: Incomplete
    def __init__(self, users: list['TypeInputUser']) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class InputPrivacyValueDisallowAll(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class InputPrivacyValueDisallowBots(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class InputPrivacyValueDisallowChatParticipants(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    chats: Incomplete
    def __init__(self, chats: list[int]) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class InputPrivacyValueDisallowContacts(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class InputPrivacyValueDisallowUsers(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    users: Incomplete
    def __init__(self, users: list['TypeInputUser']) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class InputQuickReplyShortcut(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    shortcut: Incomplete
    def __init__(self, shortcut: str) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class InputQuickReplyShortcutId(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    shortcut_id: Incomplete
    def __init__(self, shortcut_id: int) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class InputReplyToMessage(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    reply_to_msg_id: Incomplete
    top_msg_id: Incomplete
    reply_to_peer_id: Incomplete
    quote_text: Incomplete
    quote_entities: Incomplete
    quote_offset: Incomplete
    def __init__(self, reply_to_msg_id: int, top_msg_id: int | None = None, reply_to_peer_id: TypeInputPeer | None = None, quote_text: str | None = None, quote_entities: list['TypeMessageEntity'] | None = None, quote_offset: int | None = None) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class InputReplyToStory(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    peer: Incomplete
    story_id: Incomplete
    def __init__(self, peer: TypeInputPeer, story_id: int) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class InputReportReasonChildAbuse(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class InputReportReasonCopyright(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class InputReportReasonFake(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class InputReportReasonGeoIrrelevant(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class InputReportReasonIllegalDrugs(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class InputReportReasonOther(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class InputReportReasonPersonalDetails(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class InputReportReasonPornography(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class InputReportReasonSpam(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class InputReportReasonViolence(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class InputSecureFile(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    id: Incomplete
    access_hash: Incomplete
    def __init__(self, id: int, access_hash: int) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class InputSecureFileLocation(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    id: Incomplete
    access_hash: Incomplete
    def __init__(self, id: int, access_hash: int) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class InputSecureFileUploaded(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    id: Incomplete
    parts: Incomplete
    md5_checksum: Incomplete
    file_hash: Incomplete
    secret: Incomplete
    def __init__(self, id: int, parts: int, md5_checksum: str, file_hash: bytes, secret: bytes) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class InputSecureValue(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    type: Incomplete
    data: Incomplete
    front_side: Incomplete
    reverse_side: Incomplete
    selfie: Incomplete
    translation: Incomplete
    files: Incomplete
    plain_data: Incomplete
    def __init__(self, type: TypeSecureValueType, data: TypeSecureData | None = None, front_side: TypeInputSecureFile | None = None, reverse_side: TypeInputSecureFile | None = None, selfie: TypeInputSecureFile | None = None, translation: list['TypeInputSecureFile'] | None = None, files: list['TypeInputSecureFile'] | None = None, plain_data: TypeSecurePlainData | None = None) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class InputSingleMedia(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    media: Incomplete
    message: Incomplete
    random_id: Incomplete
    entities: Incomplete
    def __init__(self, media: TypeInputMedia, message: str, random_id: int = None, entities: list['TypeMessageEntity'] | None = None) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class InputStarsTransaction(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    id: Incomplete
    refund: Incomplete
    def __init__(self, id: str, refund: bool | None = None) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class InputStickerSetAnimatedEmoji(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class InputStickerSetAnimatedEmojiAnimations(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class InputStickerSetDice(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    emoticon: Incomplete
    def __init__(self, emoticon: str) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class InputStickerSetEmojiChannelDefaultStatuses(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class InputStickerSetEmojiDefaultStatuses(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class InputStickerSetEmojiDefaultTopicIcons(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class InputStickerSetEmojiGenericAnimations(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class InputStickerSetEmpty(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class InputStickerSetID(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    id: Incomplete
    access_hash: Incomplete
    def __init__(self, id: int, access_hash: int) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class InputStickerSetItem(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    document: Incomplete
    emoji: Incomplete
    mask_coords: Incomplete
    keywords: Incomplete
    def __init__(self, document: TypeInputDocument, emoji: str, mask_coords: TypeMaskCoords | None = None, keywords: str | None = None) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class InputStickerSetPremiumGifts(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class InputStickerSetShortName(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    short_name: Incomplete
    def __init__(self, short_name: str) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class InputStickerSetThumb(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    stickerset: Incomplete
    thumb_version: Incomplete
    def __init__(self, stickerset: TypeInputStickerSet, thumb_version: int) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class InputStickeredMediaDocument(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    id: Incomplete
    def __init__(self, id: TypeInputDocument) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class InputStickeredMediaPhoto(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    id: Incomplete
    def __init__(self, id: TypeInputPhoto) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class InputStorePaymentGiftPremium(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    user_id: Incomplete
    currency: Incomplete
    amount: Incomplete
    def __init__(self, user_id: TypeInputUser, currency: str, amount: int) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class InputStorePaymentPremiumGiftCode(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    users: Incomplete
    currency: Incomplete
    amount: Incomplete
    boost_peer: Incomplete
    message: Incomplete
    def __init__(self, users: list['TypeInputUser'], currency: str, amount: int, boost_peer: TypeInputPeer | None = None, message: TypeTextWithEntities | None = None) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class InputStorePaymentPremiumGiveaway(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    boost_peer: Incomplete
    until_date: Incomplete
    currency: Incomplete
    amount: Incomplete
    only_new_subscribers: Incomplete
    winners_are_visible: Incomplete
    additional_peers: Incomplete
    countries_iso2: Incomplete
    prize_description: Incomplete
    random_id: Incomplete
    def __init__(self, boost_peer: TypeInputPeer, until_date: datetime | None, currency: str, amount: int, only_new_subscribers: bool | None = None, winners_are_visible: bool | None = None, additional_peers: list['TypeInputPeer'] | None = None, countries_iso2: list[str] | None = None, prize_description: str | None = None, random_id: int = None) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class InputStorePaymentPremiumSubscription(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    restore: Incomplete
    upgrade: Incomplete
    def __init__(self, restore: bool | None = None, upgrade: bool | None = None) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class InputStorePaymentStarsGift(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    user_id: Incomplete
    stars: Incomplete
    currency: Incomplete
    amount: Incomplete
    def __init__(self, user_id: TypeInputUser, stars: int, currency: str, amount: int) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class InputStorePaymentStarsGiveaway(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    stars: Incomplete
    boost_peer: Incomplete
    until_date: Incomplete
    currency: Incomplete
    amount: Incomplete
    users: Incomplete
    only_new_subscribers: Incomplete
    winners_are_visible: Incomplete
    additional_peers: Incomplete
    countries_iso2: Incomplete
    prize_description: Incomplete
    random_id: Incomplete
    def __init__(self, stars: int, boost_peer: TypeInputPeer, until_date: datetime | None, currency: str, amount: int, users: int, only_new_subscribers: bool | None = None, winners_are_visible: bool | None = None, additional_peers: list['TypeInputPeer'] | None = None, countries_iso2: list[str] | None = None, prize_description: str | None = None, random_id: int = None) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class InputStorePaymentStarsTopup(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    stars: Incomplete
    currency: Incomplete
    amount: Incomplete
    def __init__(self, stars: int, currency: str, amount: int) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class InputTakeoutFileLocation(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class InputTheme(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    id: Incomplete
    access_hash: Incomplete
    def __init__(self, id: int, access_hash: int) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class InputThemeSettings(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    base_theme: Incomplete
    accent_color: Incomplete
    message_colors_animated: Incomplete
    outbox_accent_color: Incomplete
    message_colors: Incomplete
    wallpaper: Incomplete
    wallpaper_settings: Incomplete
    def __init__(self, base_theme: TypeBaseTheme, accent_color: int, message_colors_animated: bool | None = None, outbox_accent_color: int | None = None, message_colors: list[int] | None = None, wallpaper: TypeInputWallPaper | None = None, wallpaper_settings: TypeWallPaperSettings | None = None) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class InputThemeSlug(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    slug: Incomplete
    def __init__(self, slug: str) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class InputUser(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    user_id: Incomplete
    access_hash: Incomplete
    def __init__(self, user_id: int, access_hash: int) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class InputUserEmpty(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class InputUserFromMessage(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    peer: Incomplete
    msg_id: Incomplete
    user_id: Incomplete
    def __init__(self, peer: TypeInputPeer, msg_id: int, user_id: int) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class InputUserSelf(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class InputWallPaper(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    id: Incomplete
    access_hash: Incomplete
    def __init__(self, id: int, access_hash: int) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class InputWallPaperNoFile(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    id: Incomplete
    def __init__(self, id: int) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class InputWallPaperSlug(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    slug: Incomplete
    def __init__(self, slug: str) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class InputWebDocument(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    url: Incomplete
    size: Incomplete
    mime_type: Incomplete
    attributes: Incomplete
    def __init__(self, url: str, size: int, mime_type: str, attributes: list['TypeDocumentAttribute']) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class InputWebFileAudioAlbumThumbLocation(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    small: Incomplete
    document: Incomplete
    title: Incomplete
    performer: Incomplete
    def __init__(self, small: bool | None = None, document: TypeInputDocument | None = None, title: str | None = None, performer: str | None = None) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class InputWebFileGeoPointLocation(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    geo_point: Incomplete
    access_hash: Incomplete
    w: Incomplete
    h: Incomplete
    zoom: Incomplete
    scale: Incomplete
    def __init__(self, geo_point: TypeInputGeoPoint, access_hash: int, w: int, h: int, zoom: int, scale: int) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class InputWebFileLocation(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    url: Incomplete
    access_hash: Incomplete
    def __init__(self, url: str, access_hash: int) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class Invoice(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    currency: Incomplete
    prices: Incomplete
    test: Incomplete
    name_requested: Incomplete
    phone_requested: Incomplete
    email_requested: Incomplete
    shipping_address_requested: Incomplete
    flexible: Incomplete
    phone_to_provider: Incomplete
    email_to_provider: Incomplete
    recurring: Incomplete
    max_tip_amount: Incomplete
    suggested_tip_amounts: Incomplete
    terms_url: Incomplete
    subscription_period: Incomplete
    def __init__(self, currency: str, prices: list['TypeLabeledPrice'], test: bool | None = None, name_requested: bool | None = None, phone_requested: bool | None = None, email_requested: bool | None = None, shipping_address_requested: bool | None = None, flexible: bool | None = None, phone_to_provider: bool | None = None, email_to_provider: bool | None = None, recurring: bool | None = None, max_tip_amount: int | None = None, suggested_tip_amounts: list[int] | None = None, terms_url: str | None = None, subscription_period: int | None = None) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class IpPort(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    ipv4: Incomplete
    port: Incomplete
    def __init__(self, ipv4: int, port: int) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class IpPortSecret(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    ipv4: Incomplete
    port: Incomplete
    secret: Incomplete
    def __init__(self, ipv4: int, port: int, secret: bytes) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class JsonArray(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    value: Incomplete
    def __init__(self, value: list['TypeJSONValue']) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class JsonBool(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    value: Incomplete
    def __init__(self, value: bool) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class JsonNull(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class JsonNumber(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    value: Incomplete
    def __init__(self, value: float) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class JsonObject(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    value: Incomplete
    def __init__(self, value: list['TypeJSONObjectValue']) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class JsonObjectValue(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    key: Incomplete
    value: Incomplete
    def __init__(self, key: str, value: TypeJSONValue) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class JsonString(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    value: Incomplete
    def __init__(self, value: str) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class KeyboardButton(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    text: Incomplete
    def __init__(self, text: str) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class KeyboardButtonBuy(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    text: Incomplete
    def __init__(self, text: str) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class KeyboardButtonCallback(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    text: Incomplete
    data: Incomplete
    requires_password: Incomplete
    def __init__(self, text: str, data: bytes, requires_password: bool | None = None) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class KeyboardButtonCopy(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    text: Incomplete
    copy_text: Incomplete
    def __init__(self, text: str, copy_text: str) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class KeyboardButtonGame(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    text: Incomplete
    def __init__(self, text: str) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class KeyboardButtonRequestGeoLocation(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    text: Incomplete
    def __init__(self, text: str) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class KeyboardButtonRequestPeer(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    text: Incomplete
    button_id: Incomplete
    peer_type: Incomplete
    max_quantity: Incomplete
    def __init__(self, text: str, button_id: int, peer_type: TypeRequestPeerType, max_quantity: int) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class KeyboardButtonRequestPhone(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    text: Incomplete
    def __init__(self, text: str) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class KeyboardButtonRequestPoll(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    text: Incomplete
    quiz: Incomplete
    def __init__(self, text: str, quiz: bool | None = None) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class KeyboardButtonRow(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    buttons: Incomplete
    def __init__(self, buttons: list['TypeKeyboardButton']) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class KeyboardButtonSimpleWebView(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    text: Incomplete
    url: Incomplete
    def __init__(self, text: str, url: str) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class KeyboardButtonSwitchInline(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    text: Incomplete
    query: Incomplete
    same_peer: Incomplete
    peer_types: Incomplete
    def __init__(self, text: str, query: str, same_peer: bool | None = None, peer_types: list['TypeInlineQueryPeerType'] | None = None) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class KeyboardButtonUrl(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    text: Incomplete
    url: Incomplete
    def __init__(self, text: str, url: str) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class KeyboardButtonUrlAuth(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    text: Incomplete
    url: Incomplete
    button_id: Incomplete
    fwd_text: Incomplete
    def __init__(self, text: str, url: str, button_id: int, fwd_text: str | None = None) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class KeyboardButtonUserProfile(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    text: Incomplete
    user_id: Incomplete
    def __init__(self, text: str, user_id: int) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class KeyboardButtonWebView(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    text: Incomplete
    url: Incomplete
    def __init__(self, text: str, url: str) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class LabeledPrice(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    label: Incomplete
    amount: Incomplete
    def __init__(self, label: str, amount: int) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class LangPackDifference(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    lang_code: Incomplete
    from_version: Incomplete
    version: Incomplete
    strings: Incomplete
    def __init__(self, lang_code: str, from_version: int, version: int, strings: list['TypeLangPackString']) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class LangPackLanguage(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    name: Incomplete
    native_name: Incomplete
    lang_code: Incomplete
    plural_code: Incomplete
    strings_count: Incomplete
    translated_count: Incomplete
    translations_url: Incomplete
    official: Incomplete
    rtl: Incomplete
    beta: Incomplete
    base_lang_code: Incomplete
    def __init__(self, name: str, native_name: str, lang_code: str, plural_code: str, strings_count: int, translated_count: int, translations_url: str, official: bool | None = None, rtl: bool | None = None, beta: bool | None = None, base_lang_code: str | None = None) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class LangPackString(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    key: Incomplete
    value: Incomplete
    def __init__(self, key: str, value: str) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class LangPackStringDeleted(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    key: Incomplete
    def __init__(self, key: str) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class LangPackStringPluralized(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    key: Incomplete
    other_value: Incomplete
    zero_value: Incomplete
    one_value: Incomplete
    two_value: Incomplete
    few_value: Incomplete
    many_value: Incomplete
    def __init__(self, key: str, other_value: str, zero_value: str | None = None, one_value: str | None = None, two_value: str | None = None, few_value: str | None = None, many_value: str | None = None) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class MaskCoords(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    n: Incomplete
    x: Incomplete
    y: Incomplete
    zoom: Incomplete
    def __init__(self, n: int, x: float, y: float, zoom: float) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class MediaAreaChannelPost(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    coordinates: Incomplete
    channel_id: Incomplete
    msg_id: Incomplete
    def __init__(self, coordinates: TypeMediaAreaCoordinates, channel_id: int, msg_id: int) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class MediaAreaCoordinates(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    x: Incomplete
    y: Incomplete
    w: Incomplete
    h: Incomplete
    rotation: Incomplete
    radius: Incomplete
    def __init__(self, x: float, y: float, w: float, h: float, rotation: float, radius: float | None = None) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class MediaAreaGeoPoint(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    coordinates: Incomplete
    geo: Incomplete
    address: Incomplete
    def __init__(self, coordinates: TypeMediaAreaCoordinates, geo: TypeGeoPoint, address: TypeGeoPointAddress | None = None) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class MediaAreaSuggestedReaction(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    coordinates: Incomplete
    reaction: Incomplete
    dark: Incomplete
    flipped: Incomplete
    def __init__(self, coordinates: TypeMediaAreaCoordinates, reaction: TypeReaction, dark: bool | None = None, flipped: bool | None = None) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class MediaAreaUrl(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    coordinates: Incomplete
    url: Incomplete
    def __init__(self, coordinates: TypeMediaAreaCoordinates, url: str) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class MediaAreaVenue(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    coordinates: Incomplete
    geo: Incomplete
    title: Incomplete
    address: Incomplete
    provider: Incomplete
    venue_id: Incomplete
    venue_type: Incomplete
    def __init__(self, coordinates: TypeMediaAreaCoordinates, geo: TypeGeoPoint, title: str, address: str, provider: str, venue_id: str, venue_type: str) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class MediaAreaWeather(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    coordinates: Incomplete
    emoji: Incomplete
    temperature_c: Incomplete
    color: Incomplete
    def __init__(self, coordinates: TypeMediaAreaCoordinates, emoji: str, temperature_c: float, color: int) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class Message(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    id: Incomplete
    peer_id: Incomplete
    date: Incomplete
    message: Incomplete
    out: Incomplete
    mentioned: Incomplete
    media_unread: Incomplete
    silent: Incomplete
    post: Incomplete
    from_scheduled: Incomplete
    legacy: Incomplete
    edit_hide: Incomplete
    pinned: Incomplete
    noforwards: Incomplete
    invert_media: Incomplete
    offline: Incomplete
    video_processing_pending: Incomplete
    from_id: Incomplete
    from_boosts_applied: Incomplete
    saved_peer_id: Incomplete
    fwd_from: Incomplete
    via_bot_id: Incomplete
    via_business_bot_id: Incomplete
    reply_to: Incomplete
    media: Incomplete
    reply_markup: Incomplete
    entities: Incomplete
    views: Incomplete
    forwards: Incomplete
    replies: Incomplete
    edit_date: Incomplete
    post_author: Incomplete
    grouped_id: Incomplete
    reactions: Incomplete
    restriction_reason: Incomplete
    ttl_period: Incomplete
    quick_reply_shortcut_id: Incomplete
    effect: Incomplete
    factcheck: Incomplete
    def __init__(self, id: int, peer_id: TypePeer, date: datetime | None, message: str, out: bool | None = None, mentioned: bool | None = None, media_unread: bool | None = None, silent: bool | None = None, post: bool | None = None, from_scheduled: bool | None = None, legacy: bool | None = None, edit_hide: bool | None = None, pinned: bool | None = None, noforwards: bool | None = None, invert_media: bool | None = None, offline: bool | None = None, video_processing_pending: bool | None = None, from_id: TypePeer | None = None, from_boosts_applied: int | None = None, saved_peer_id: TypePeer | None = None, fwd_from: TypeMessageFwdHeader | None = None, via_bot_id: int | None = None, via_business_bot_id: int | None = None, reply_to: TypeMessageReplyHeader | None = None, media: TypeMessageMedia | None = None, reply_markup: TypeReplyMarkup | None = None, entities: list['TypeMessageEntity'] | None = None, views: int | None = None, forwards: int | None = None, replies: TypeMessageReplies | None = None, edit_date: datetime | None = None, post_author: str | None = None, grouped_id: int | None = None, reactions: TypeMessageReactions | None = None, restriction_reason: list['TypeRestrictionReason'] | None = None, ttl_period: int | None = None, quick_reply_shortcut_id: int | None = None, effect: int | None = None, factcheck: TypeFactCheck | None = None) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class MessageActionBoostApply(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    boosts: Incomplete
    def __init__(self, boosts: int) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class MessageActionBotAllowed(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    attach_menu: Incomplete
    from_request: Incomplete
    domain: Incomplete
    app: Incomplete
    def __init__(self, attach_menu: bool | None = None, from_request: bool | None = None, domain: str | None = None, app: TypeBotApp | None = None) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class MessageActionChannelCreate(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    title: Incomplete
    def __init__(self, title: str) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class MessageActionChannelMigrateFrom(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    title: Incomplete
    chat_id: Incomplete
    def __init__(self, title: str, chat_id: int) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class MessageActionChatAddUser(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    users: Incomplete
    def __init__(self, users: list[int]) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class MessageActionChatCreate(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    title: Incomplete
    users: Incomplete
    def __init__(self, title: str, users: list[int]) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class MessageActionChatDeletePhoto(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class MessageActionChatDeleteUser(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    user_id: Incomplete
    def __init__(self, user_id: int) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class MessageActionChatEditPhoto(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    photo: Incomplete
    def __init__(self, photo: TypePhoto) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class MessageActionChatEditTitle(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    title: Incomplete
    def __init__(self, title: str) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class MessageActionChatJoinedByLink(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    inviter_id: Incomplete
    def __init__(self, inviter_id: int) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class MessageActionChatJoinedByRequest(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class MessageActionChatMigrateTo(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    channel_id: Incomplete
    def __init__(self, channel_id: int) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class MessageActionContactSignUp(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class MessageActionCustomAction(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    message: Incomplete
    def __init__(self, message: str) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class MessageActionEmpty(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class MessageActionGameScore(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    game_id: Incomplete
    score: Incomplete
    def __init__(self, game_id: int, score: int) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class MessageActionGeoProximityReached(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    from_id: Incomplete
    to_id: Incomplete
    distance: Incomplete
    def __init__(self, from_id: TypePeer, to_id: TypePeer, distance: int) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class MessageActionGiftCode(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    months: Incomplete
    slug: Incomplete
    via_giveaway: Incomplete
    unclaimed: Incomplete
    boost_peer: Incomplete
    currency: Incomplete
    amount: Incomplete
    crypto_currency: Incomplete
    crypto_amount: Incomplete
    message: Incomplete
    def __init__(self, months: int, slug: str, via_giveaway: bool | None = None, unclaimed: bool | None = None, boost_peer: TypePeer | None = None, currency: str | None = None, amount: int | None = None, crypto_currency: str | None = None, crypto_amount: int | None = None, message: TypeTextWithEntities | None = None) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class MessageActionGiftPremium(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    currency: Incomplete
    amount: Incomplete
    months: Incomplete
    crypto_currency: Incomplete
    crypto_amount: Incomplete
    message: Incomplete
    def __init__(self, currency: str, amount: int, months: int, crypto_currency: str | None = None, crypto_amount: int | None = None, message: TypeTextWithEntities | None = None) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class MessageActionGiftStars(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    currency: Incomplete
    amount: Incomplete
    stars: Incomplete
    crypto_currency: Incomplete
    crypto_amount: Incomplete
    transaction_id: Incomplete
    def __init__(self, currency: str, amount: int, stars: int, crypto_currency: str | None = None, crypto_amount: int | None = None, transaction_id: str | None = None) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class MessageActionGiveawayLaunch(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    stars: Incomplete
    def __init__(self, stars: int | None = None) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class MessageActionGiveawayResults(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    winners_count: Incomplete
    unclaimed_count: Incomplete
    stars: Incomplete
    def __init__(self, winners_count: int, unclaimed_count: int, stars: bool | None = None) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class MessageActionGroupCall(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    call: Incomplete
    duration: Incomplete
    def __init__(self, call: TypeInputGroupCall, duration: int | None = None) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class MessageActionGroupCallScheduled(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    call: Incomplete
    schedule_date: Incomplete
    def __init__(self, call: TypeInputGroupCall, schedule_date: datetime | None) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class MessageActionHistoryClear(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class MessageActionInviteToGroupCall(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    call: Incomplete
    users: Incomplete
    def __init__(self, call: TypeInputGroupCall, users: list[int]) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class MessageActionPaymentRefunded(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    peer: Incomplete
    currency: Incomplete
    total_amount: Incomplete
    charge: Incomplete
    payload: Incomplete
    def __init__(self, peer: TypePeer, currency: str, total_amount: int, charge: TypePaymentCharge, payload: bytes | None = None) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class MessageActionPaymentSent(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    currency: Incomplete
    total_amount: Incomplete
    recurring_init: Incomplete
    recurring_used: Incomplete
    invoice_slug: Incomplete
    def __init__(self, currency: str, total_amount: int, recurring_init: bool | None = None, recurring_used: bool | None = None, invoice_slug: str | None = None) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class MessageActionPaymentSentMe(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    currency: Incomplete
    total_amount: Incomplete
    payload: Incomplete
    charge: Incomplete
    recurring_init: Incomplete
    recurring_used: Incomplete
    info: Incomplete
    shipping_option_id: Incomplete
    def __init__(self, currency: str, total_amount: int, payload: bytes, charge: TypePaymentCharge, recurring_init: bool | None = None, recurring_used: bool | None = None, info: TypePaymentRequestedInfo | None = None, shipping_option_id: str | None = None) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class MessageActionPhoneCall(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    call_id: Incomplete
    video: Incomplete
    reason: Incomplete
    duration: Incomplete
    def __init__(self, call_id: int, video: bool | None = None, reason: TypePhoneCallDiscardReason | None = None, duration: int | None = None) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class MessageActionPinMessage(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class MessageActionPrizeStars(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    stars: Incomplete
    transaction_id: Incomplete
    boost_peer: Incomplete
    giveaway_msg_id: Incomplete
    unclaimed: Incomplete
    def __init__(self, stars: int, transaction_id: str, boost_peer: TypePeer, giveaway_msg_id: int, unclaimed: bool | None = None) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class MessageActionRequestedPeer(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    button_id: Incomplete
    peers: Incomplete
    def __init__(self, button_id: int, peers: list['TypePeer']) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class MessageActionRequestedPeerSentMe(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    button_id: Incomplete
    peers: Incomplete
    def __init__(self, button_id: int, peers: list['TypeRequestedPeer']) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class MessageActionScreenshotTaken(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class MessageActionSecureValuesSent(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    types: Incomplete
    def __init__(self, types: list['TypeSecureValueType']) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class MessageActionSecureValuesSentMe(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    values: Incomplete
    credentials: Incomplete
    def __init__(self, values: list['TypeSecureValue'], credentials: TypeSecureCredentialsEncrypted) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class MessageActionSetChatTheme(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    emoticon: Incomplete
    def __init__(self, emoticon: str) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class MessageActionSetChatWallPaper(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    wallpaper: Incomplete
    same: Incomplete
    for_both: Incomplete
    def __init__(self, wallpaper: TypeWallPaper, same: bool | None = None, for_both: bool | None = None) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class MessageActionSetMessagesTTL(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    period: Incomplete
    auto_setting_from: Incomplete
    def __init__(self, period: int, auto_setting_from: int | None = None) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class MessageActionStarGift(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    gift: Incomplete
    name_hidden: Incomplete
    saved: Incomplete
    converted: Incomplete
    message: Incomplete
    convert_stars: Incomplete
    def __init__(self, gift: TypeStarGift, name_hidden: bool | None = None, saved: bool | None = None, converted: bool | None = None, message: TypeTextWithEntities | None = None, convert_stars: int | None = None) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class MessageActionSuggestProfilePhoto(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    photo: Incomplete
    def __init__(self, photo: TypePhoto) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class MessageActionTopicCreate(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    title: Incomplete
    icon_color: Incomplete
    icon_emoji_id: Incomplete
    def __init__(self, title: str, icon_color: int, icon_emoji_id: int | None = None) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class MessageActionTopicEdit(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    title: Incomplete
    icon_emoji_id: Incomplete
    closed: Incomplete
    hidden: Incomplete
    def __init__(self, title: str | None = None, icon_emoji_id: int | None = None, closed: bool | None = None, hidden: bool | None = None) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class MessageActionWebViewDataSent(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    text: Incomplete
    def __init__(self, text: str) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class MessageActionWebViewDataSentMe(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    text: Incomplete
    data: Incomplete
    def __init__(self, text: str, data: str) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class MessageEmpty(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    id: Incomplete
    peer_id: Incomplete
    def __init__(self, id: int, peer_id: TypePeer | None = None) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class MessageEntityBankCard(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    offset: Incomplete
    length: Incomplete
    def __init__(self, offset: int, length: int) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class MessageEntityBlockquote(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    offset: Incomplete
    length: Incomplete
    collapsed: Incomplete
    def __init__(self, offset: int, length: int, collapsed: bool | None = None) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class MessageEntityBold(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    offset: Incomplete
    length: Incomplete
    def __init__(self, offset: int, length: int) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class MessageEntityBotCommand(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    offset: Incomplete
    length: Incomplete
    def __init__(self, offset: int, length: int) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class MessageEntityCashtag(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    offset: Incomplete
    length: Incomplete
    def __init__(self, offset: int, length: int) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class MessageEntityCode(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    offset: Incomplete
    length: Incomplete
    def __init__(self, offset: int, length: int) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class MessageEntityCustomEmoji(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    offset: Incomplete
    length: Incomplete
    document_id: Incomplete
    def __init__(self, offset: int, length: int, document_id: int) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class MessageEntityEmail(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    offset: Incomplete
    length: Incomplete
    def __init__(self, offset: int, length: int) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class MessageEntityHashtag(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    offset: Incomplete
    length: Incomplete
    def __init__(self, offset: int, length: int) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class MessageEntityItalic(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    offset: Incomplete
    length: Incomplete
    def __init__(self, offset: int, length: int) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class MessageEntityMention(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    offset: Incomplete
    length: Incomplete
    def __init__(self, offset: int, length: int) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class MessageEntityMentionName(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    offset: Incomplete
    length: Incomplete
    user_id: Incomplete
    def __init__(self, offset: int, length: int, user_id: int) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class MessageEntityPhone(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    offset: Incomplete
    length: Incomplete
    def __init__(self, offset: int, length: int) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class MessageEntityPre(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    offset: Incomplete
    length: Incomplete
    language: Incomplete
    def __init__(self, offset: int, length: int, language: str) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class MessageEntitySpoiler(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    offset: Incomplete
    length: Incomplete
    def __init__(self, offset: int, length: int) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class MessageEntityStrike(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    offset: Incomplete
    length: Incomplete
    def __init__(self, offset: int, length: int) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class MessageEntityTextUrl(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    offset: Incomplete
    length: Incomplete
    url: Incomplete
    def __init__(self, offset: int, length: int, url: str) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class MessageEntityUnderline(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    offset: Incomplete
    length: Incomplete
    def __init__(self, offset: int, length: int) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class MessageEntityUnknown(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    offset: Incomplete
    length: Incomplete
    def __init__(self, offset: int, length: int) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class MessageEntityUrl(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    offset: Incomplete
    length: Incomplete
    def __init__(self, offset: int, length: int) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class MessageExtendedMedia(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    media: Incomplete
    def __init__(self, media: TypeMessageMedia) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class MessageExtendedMediaPreview(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    w: Incomplete
    h: Incomplete
    thumb: Incomplete
    video_duration: Incomplete
    def __init__(self, w: int | None = None, h: int | None = None, thumb: TypePhotoSize | None = None, video_duration: int | None = None) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class MessageFwdHeader(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    date: Incomplete
    imported: Incomplete
    saved_out: Incomplete
    from_id: Incomplete
    from_name: Incomplete
    channel_post: Incomplete
    post_author: Incomplete
    saved_from_peer: Incomplete
    saved_from_msg_id: Incomplete
    saved_from_id: Incomplete
    saved_from_name: Incomplete
    saved_date: Incomplete
    psa_type: Incomplete
    def __init__(self, date: datetime | None, imported: bool | None = None, saved_out: bool | None = None, from_id: TypePeer | None = None, from_name: str | None = None, channel_post: int | None = None, post_author: str | None = None, saved_from_peer: TypePeer | None = None, saved_from_msg_id: int | None = None, saved_from_id: TypePeer | None = None, saved_from_name: str | None = None, saved_date: datetime | None = None, psa_type: str | None = None) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class MessageMediaContact(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    phone_number: Incomplete
    first_name: Incomplete
    last_name: Incomplete
    vcard: Incomplete
    user_id: Incomplete
    def __init__(self, phone_number: str, first_name: str, last_name: str, vcard: str, user_id: int) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class MessageMediaDice(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    value: Incomplete
    emoticon: Incomplete
    def __init__(self, value: int, emoticon: str) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class MessageMediaDocument(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    nopremium: Incomplete
    spoiler: Incomplete
    video: Incomplete
    round: Incomplete
    voice: Incomplete
    document: Incomplete
    alt_documents: Incomplete
    ttl_seconds: Incomplete
    def __init__(self, nopremium: bool | None = None, spoiler: bool | None = None, video: bool | None = None, round: bool | None = None, voice: bool | None = None, document: TypeDocument | None = None, alt_documents: list['TypeDocument'] | None = None, ttl_seconds: int | None = None) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class MessageMediaEmpty(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class MessageMediaGame(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    game: Incomplete
    def __init__(self, game: TypeGame) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class MessageMediaGeo(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    geo: Incomplete
    def __init__(self, geo: TypeGeoPoint) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class MessageMediaGeoLive(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    geo: Incomplete
    period: Incomplete
    heading: Incomplete
    proximity_notification_radius: Incomplete
    def __init__(self, geo: TypeGeoPoint, period: int, heading: int | None = None, proximity_notification_radius: int | None = None) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class MessageMediaGiveaway(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    channels: Incomplete
    quantity: Incomplete
    until_date: Incomplete
    only_new_subscribers: Incomplete
    winners_are_visible: Incomplete
    countries_iso2: Incomplete
    prize_description: Incomplete
    months: Incomplete
    stars: Incomplete
    def __init__(self, channels: list[int], quantity: int, until_date: datetime | None, only_new_subscribers: bool | None = None, winners_are_visible: bool | None = None, countries_iso2: list[str] | None = None, prize_description: str | None = None, months: int | None = None, stars: int | None = None) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class MessageMediaGiveawayResults(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    channel_id: Incomplete
    launch_msg_id: Incomplete
    winners_count: Incomplete
    unclaimed_count: Incomplete
    winners: Incomplete
    until_date: Incomplete
    only_new_subscribers: Incomplete
    refunded: Incomplete
    additional_peers_count: Incomplete
    months: Incomplete
    stars: Incomplete
    prize_description: Incomplete
    def __init__(self, channel_id: int, launch_msg_id: int, winners_count: int, unclaimed_count: int, winners: list[int], until_date: datetime | None, only_new_subscribers: bool | None = None, refunded: bool | None = None, additional_peers_count: int | None = None, months: int | None = None, stars: int | None = None, prize_description: str | None = None) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class MessageMediaInvoice(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    title: Incomplete
    description: Incomplete
    currency: Incomplete
    total_amount: Incomplete
    start_param: Incomplete
    shipping_address_requested: Incomplete
    test: Incomplete
    photo: Incomplete
    receipt_msg_id: Incomplete
    extended_media: Incomplete
    def __init__(self, title: str, description: str, currency: str, total_amount: int, start_param: str, shipping_address_requested: bool | None = None, test: bool | None = None, photo: TypeWebDocument | None = None, receipt_msg_id: int | None = None, extended_media: TypeMessageExtendedMedia | None = None) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class MessageMediaPaidMedia(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    stars_amount: Incomplete
    extended_media: Incomplete
    def __init__(self, stars_amount: int, extended_media: list['TypeMessageExtendedMedia']) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class MessageMediaPhoto(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    spoiler: Incomplete
    photo: Incomplete
    ttl_seconds: Incomplete
    def __init__(self, spoiler: bool | None = None, photo: TypePhoto | None = None, ttl_seconds: int | None = None) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class MessageMediaPoll(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    poll: Incomplete
    results: Incomplete
    def __init__(self, poll: TypePoll, results: TypePollResults) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class MessageMediaStory(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    peer: Incomplete
    id: Incomplete
    via_mention: Incomplete
    story: Incomplete
    def __init__(self, peer: TypePeer, id: int, via_mention: bool | None = None, story: TypeStoryItem | None = None) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class MessageMediaUnsupported(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class MessageMediaVenue(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    geo: Incomplete
    title: Incomplete
    address: Incomplete
    provider: Incomplete
    venue_id: Incomplete
    venue_type: Incomplete
    def __init__(self, geo: TypeGeoPoint, title: str, address: str, provider: str, venue_id: str, venue_type: str) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class MessageMediaWebPage(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    webpage: Incomplete
    force_large_media: Incomplete
    force_small_media: Incomplete
    manual: Incomplete
    safe: Incomplete
    def __init__(self, webpage: TypeWebPage, force_large_media: bool | None = None, force_small_media: bool | None = None, manual: bool | None = None, safe: bool | None = None) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class MessagePeerReaction(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    peer_id: Incomplete
    date: Incomplete
    reaction: Incomplete
    big: Incomplete
    unread: Incomplete
    my: Incomplete
    def __init__(self, peer_id: TypePeer, date: datetime | None, reaction: TypeReaction, big: bool | None = None, unread: bool | None = None, my: bool | None = None) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class MessagePeerVote(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    peer: Incomplete
    option: Incomplete
    date: Incomplete
    def __init__(self, peer: TypePeer, option: bytes, date: datetime | None) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class MessagePeerVoteInputOption(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    peer: Incomplete
    date: Incomplete
    def __init__(self, peer: TypePeer, date: datetime | None) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class MessagePeerVoteMultiple(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    peer: Incomplete
    options: Incomplete
    date: Incomplete
    def __init__(self, peer: TypePeer, options: list[bytes], date: datetime | None) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class MessageRange(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    min_id: Incomplete
    max_id: Incomplete
    def __init__(self, min_id: int, max_id: int) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class MessageReactions(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    results: Incomplete
    min: Incomplete
    can_see_list: Incomplete
    reactions_as_tags: Incomplete
    recent_reactions: Incomplete
    top_reactors: Incomplete
    def __init__(self, results: list['TypeReactionCount'], min: bool | None = None, can_see_list: bool | None = None, reactions_as_tags: bool | None = None, recent_reactions: list['TypeMessagePeerReaction'] | None = None, top_reactors: list['TypeMessageReactor'] | None = None) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class MessageReactor(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    count: Incomplete
    top: Incomplete
    my: Incomplete
    anonymous: Incomplete
    peer_id: Incomplete
    def __init__(self, count: int, top: bool | None = None, my: bool | None = None, anonymous: bool | None = None, peer_id: TypePeer | None = None) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class MessageReplies(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    replies: Incomplete
    replies_pts: Incomplete
    comments: Incomplete
    recent_repliers: Incomplete
    channel_id: Incomplete
    max_id: Incomplete
    read_max_id: Incomplete
    def __init__(self, replies: int, replies_pts: int, comments: bool | None = None, recent_repliers: list['TypePeer'] | None = None, channel_id: int | None = None, max_id: int | None = None, read_max_id: int | None = None) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class MessageReplyHeader(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    reply_to_scheduled: Incomplete
    forum_topic: Incomplete
    quote: Incomplete
    reply_to_msg_id: Incomplete
    reply_to_peer_id: Incomplete
    reply_from: Incomplete
    reply_media: Incomplete
    reply_to_top_id: Incomplete
    quote_text: Incomplete
    quote_entities: Incomplete
    quote_offset: Incomplete
    def __init__(self, reply_to_scheduled: bool | None = None, forum_topic: bool | None = None, quote: bool | None = None, reply_to_msg_id: int | None = None, reply_to_peer_id: TypePeer | None = None, reply_from: TypeMessageFwdHeader | None = None, reply_media: TypeMessageMedia | None = None, reply_to_top_id: int | None = None, quote_text: str | None = None, quote_entities: list['TypeMessageEntity'] | None = None, quote_offset: int | None = None) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class MessageReplyStoryHeader(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    peer: Incomplete
    story_id: Incomplete
    def __init__(self, peer: TypePeer, story_id: int) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class MessageReportOption(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    text: Incomplete
    option: Incomplete
    def __init__(self, text: str, option: bytes) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class MessageService(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    id: Incomplete
    peer_id: Incomplete
    date: Incomplete
    action: Incomplete
    out: Incomplete
    mentioned: Incomplete
    media_unread: Incomplete
    silent: Incomplete
    post: Incomplete
    legacy: Incomplete
    from_id: Incomplete
    reply_to: Incomplete
    ttl_period: Incomplete
    def __init__(self, id: int, peer_id: TypePeer, date: datetime | None, action: TypeMessageAction, out: bool | None = None, mentioned: bool | None = None, media_unread: bool | None = None, silent: bool | None = None, post: bool | None = None, legacy: bool | None = None, from_id: TypePeer | None = None, reply_to: TypeMessageReplyHeader | None = None, ttl_period: int | None = None) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class MessageViews(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    views: Incomplete
    forwards: Incomplete
    replies: Incomplete
    def __init__(self, views: int | None = None, forwards: int | None = None, replies: TypeMessageReplies | None = None) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class MissingInvitee(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    user_id: Incomplete
    premium_would_allow_invite: Incomplete
    premium_required_for_pm: Incomplete
    def __init__(self, user_id: int, premium_would_allow_invite: bool | None = None, premium_required_for_pm: bool | None = None) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class MsgDetailedInfo(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    msg_id: Incomplete
    answer_msg_id: Incomplete
    bytes: Incomplete
    status: Incomplete
    def __init__(self, msg_id: int, answer_msg_id: int, bytes: int, status: int) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class MsgNewDetailedInfo(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    answer_msg_id: Incomplete
    bytes: Incomplete
    status: Incomplete
    def __init__(self, answer_msg_id: int, bytes: int, status: int) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class MsgResendReq(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    msg_ids: Incomplete
    def __init__(self, msg_ids: list[int]) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class MsgsAck(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    msg_ids: Incomplete
    def __init__(self, msg_ids: list[int]) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class MsgsAllInfo(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    msg_ids: Incomplete
    info: Incomplete
    def __init__(self, msg_ids: list[int], info: str) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class MsgsStateInfo(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    req_msg_id: Incomplete
    info: Incomplete
    def __init__(self, req_msg_id: int, info: str) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class MsgsStateReq(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    msg_ids: Incomplete
    def __init__(self, msg_ids: list[int]) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class MyBoost(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    slot: Incomplete
    date: Incomplete
    expires: Incomplete
    peer: Incomplete
    cooldown_until_date: Incomplete
    def __init__(self, slot: int, date: datetime | None, expires: datetime | None, peer: TypePeer | None = None, cooldown_until_date: datetime | None = None) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class NearestDc(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    country: Incomplete
    this_dc: Incomplete
    nearest_dc: Incomplete
    def __init__(self, country: str, this_dc: int, nearest_dc: int) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class NewSessionCreated(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    first_msg_id: Incomplete
    unique_id: Incomplete
    server_salt: Incomplete
    def __init__(self, first_msg_id: int, unique_id: int, server_salt: int) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class NotificationSoundDefault(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class NotificationSoundLocal(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    title: Incomplete
    data: Incomplete
    def __init__(self, title: str, data: str) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class NotificationSoundNone(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class NotificationSoundRingtone(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    id: Incomplete
    def __init__(self, id: int) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class NotifyBroadcasts(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class NotifyChats(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class NotifyForumTopic(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    peer: Incomplete
    top_msg_id: Incomplete
    def __init__(self, peer: TypePeer, top_msg_id: int) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class NotifyPeer(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    peer: Incomplete
    def __init__(self, peer: TypePeer) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class NotifyUsers(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class OutboxReadDate(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    date: Incomplete
    def __init__(self, date: datetime | None) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class PQInnerData(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    pq: Incomplete
    p: Incomplete
    q: Incomplete
    nonce: Incomplete
    server_nonce: Incomplete
    new_nonce: Incomplete
    def __init__(self, pq: bytes, p: bytes, q: bytes, nonce: int, server_nonce: int, new_nonce: int) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class PQInnerDataDc(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    pq: Incomplete
    p: Incomplete
    q: Incomplete
    nonce: Incomplete
    server_nonce: Incomplete
    new_nonce: Incomplete
    dc: Incomplete
    def __init__(self, pq: bytes, p: bytes, q: bytes, nonce: int, server_nonce: int, new_nonce: int, dc: int) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class PQInnerDataTemp(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    pq: Incomplete
    p: Incomplete
    q: Incomplete
    nonce: Incomplete
    server_nonce: Incomplete
    new_nonce: Incomplete
    expires_in: Incomplete
    def __init__(self, pq: bytes, p: bytes, q: bytes, nonce: int, server_nonce: int, new_nonce: int, expires_in: int) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class PQInnerDataTempDc(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    pq: Incomplete
    p: Incomplete
    q: Incomplete
    nonce: Incomplete
    server_nonce: Incomplete
    new_nonce: Incomplete
    dc: Incomplete
    expires_in: Incomplete
    def __init__(self, pq: bytes, p: bytes, q: bytes, nonce: int, server_nonce: int, new_nonce: int, dc: int, expires_in: int) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class Page(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    url: Incomplete
    blocks: Incomplete
    photos: Incomplete
    documents: Incomplete
    part: Incomplete
    rtl: Incomplete
    v2: Incomplete
    views: Incomplete
    def __init__(self, url: str, blocks: list['TypePageBlock'], photos: list['TypePhoto'], documents: list['TypeDocument'], part: bool | None = None, rtl: bool | None = None, v2: bool | None = None, views: int | None = None) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class PageBlockAnchor(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    name: Incomplete
    def __init__(self, name: str) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class PageBlockAudio(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    audio_id: Incomplete
    caption: Incomplete
    def __init__(self, audio_id: int, caption: TypePageCaption) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class PageBlockAuthorDate(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    author: Incomplete
    published_date: Incomplete
    def __init__(self, author: TypeRichText, published_date: datetime | None) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class PageBlockBlockquote(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    text: Incomplete
    caption: Incomplete
    def __init__(self, text: TypeRichText, caption: TypeRichText) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class PageBlockChannel(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    channel: Incomplete
    def __init__(self, channel: TypeChat) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class PageBlockCollage(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    items: Incomplete
    caption: Incomplete
    def __init__(self, items: list['TypePageBlock'], caption: TypePageCaption) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class PageBlockCover(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    cover: Incomplete
    def __init__(self, cover: TypePageBlock) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class PageBlockDetails(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    blocks: Incomplete
    title: Incomplete
    open: Incomplete
    def __init__(self, blocks: list['TypePageBlock'], title: TypeRichText, open: bool | None = None) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class PageBlockDivider(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class PageBlockEmbed(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    caption: Incomplete
    full_width: Incomplete
    allow_scrolling: Incomplete
    url: Incomplete
    html: Incomplete
    poster_photo_id: Incomplete
    w: Incomplete
    h: Incomplete
    def __init__(self, caption: TypePageCaption, full_width: bool | None = None, allow_scrolling: bool | None = None, url: str | None = None, html: str | None = None, poster_photo_id: int | None = None, w: int | None = None, h: int | None = None) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class PageBlockEmbedPost(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    url: Incomplete
    webpage_id: Incomplete
    author_photo_id: Incomplete
    author: Incomplete
    date: Incomplete
    blocks: Incomplete
    caption: Incomplete
    def __init__(self, url: str, webpage_id: int, author_photo_id: int, author: str, date: datetime | None, blocks: list['TypePageBlock'], caption: TypePageCaption) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class PageBlockFooter(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    text: Incomplete
    def __init__(self, text: TypeRichText) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class PageBlockHeader(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    text: Incomplete
    def __init__(self, text: TypeRichText) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class PageBlockKicker(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    text: Incomplete
    def __init__(self, text: TypeRichText) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class PageBlockList(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    items: Incomplete
    def __init__(self, items: list['TypePageListItem']) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class PageBlockMap(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    geo: Incomplete
    zoom: Incomplete
    w: Incomplete
    h: Incomplete
    caption: Incomplete
    def __init__(self, geo: TypeGeoPoint, zoom: int, w: int, h: int, caption: TypePageCaption) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class PageBlockOrderedList(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    items: Incomplete
    def __init__(self, items: list['TypePageListOrderedItem']) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class PageBlockParagraph(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    text: Incomplete
    def __init__(self, text: TypeRichText) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class PageBlockPhoto(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    photo_id: Incomplete
    caption: Incomplete
    url: Incomplete
    webpage_id: Incomplete
    def __init__(self, photo_id: int, caption: TypePageCaption, url: str | None = None, webpage_id: int | None = None) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class PageBlockPreformatted(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    text: Incomplete
    language: Incomplete
    def __init__(self, text: TypeRichText, language: str) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class PageBlockPullquote(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    text: Incomplete
    caption: Incomplete
    def __init__(self, text: TypeRichText, caption: TypeRichText) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class PageBlockRelatedArticles(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    title: Incomplete
    articles: Incomplete
    def __init__(self, title: TypeRichText, articles: list['TypePageRelatedArticle']) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class PageBlockSlideshow(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    items: Incomplete
    caption: Incomplete
    def __init__(self, items: list['TypePageBlock'], caption: TypePageCaption) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class PageBlockSubheader(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    text: Incomplete
    def __init__(self, text: TypeRichText) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class PageBlockSubtitle(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    text: Incomplete
    def __init__(self, text: TypeRichText) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class PageBlockTable(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    title: Incomplete
    rows: Incomplete
    bordered: Incomplete
    striped: Incomplete
    def __init__(self, title: TypeRichText, rows: list['TypePageTableRow'], bordered: bool | None = None, striped: bool | None = None) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class PageBlockTitle(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    text: Incomplete
    def __init__(self, text: TypeRichText) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class PageBlockUnsupported(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class PageBlockVideo(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    video_id: Incomplete
    caption: Incomplete
    autoplay: Incomplete
    loop: Incomplete
    def __init__(self, video_id: int, caption: TypePageCaption, autoplay: bool | None = None, loop: bool | None = None) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class PageCaption(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    text: Incomplete
    credit: Incomplete
    def __init__(self, text: TypeRichText, credit: TypeRichText) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class PageListItemBlocks(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    blocks: Incomplete
    def __init__(self, blocks: list['TypePageBlock']) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class PageListItemText(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    text: Incomplete
    def __init__(self, text: TypeRichText) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class PageListOrderedItemBlocks(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    num: Incomplete
    blocks: Incomplete
    def __init__(self, num: str, blocks: list['TypePageBlock']) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class PageListOrderedItemText(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    num: Incomplete
    text: Incomplete
    def __init__(self, num: str, text: TypeRichText) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class PageRelatedArticle(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    url: Incomplete
    webpage_id: Incomplete
    title: Incomplete
    description: Incomplete
    photo_id: Incomplete
    author: Incomplete
    published_date: Incomplete
    def __init__(self, url: str, webpage_id: int, title: str | None = None, description: str | None = None, photo_id: int | None = None, author: str | None = None, published_date: datetime | None = None) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class PageTableCell(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    header: Incomplete
    align_center: Incomplete
    align_right: Incomplete
    valign_middle: Incomplete
    valign_bottom: Incomplete
    text: Incomplete
    colspan: Incomplete
    rowspan: Incomplete
    def __init__(self, header: bool | None = None, align_center: bool | None = None, align_right: bool | None = None, valign_middle: bool | None = None, valign_bottom: bool | None = None, text: TypeRichText | None = None, colspan: int | None = None, rowspan: int | None = None) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class PageTableRow(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    cells: Incomplete
    def __init__(self, cells: list['TypePageTableCell']) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class PasswordKdfAlgoSHA256SHA256PBKDF2HMACSHA512iter100000SHA256ModPow(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    salt1: Incomplete
    salt2: Incomplete
    g: Incomplete
    p: Incomplete
    def __init__(self, salt1: bytes, salt2: bytes, g: int, p: bytes) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class PasswordKdfAlgoUnknown(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class PaymentCharge(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    id: Incomplete
    provider_charge_id: Incomplete
    def __init__(self, id: str, provider_charge_id: str) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class PaymentFormMethod(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    url: Incomplete
    title: Incomplete
    def __init__(self, url: str, title: str) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class PaymentRequestedInfo(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    name: Incomplete
    phone: Incomplete
    email: Incomplete
    shipping_address: Incomplete
    def __init__(self, name: str | None = None, phone: str | None = None, email: str | None = None, shipping_address: TypePostAddress | None = None) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class PaymentSavedCredentialsCard(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    id: Incomplete
    title: Incomplete
    def __init__(self, id: str, title: str) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class PeerBlocked(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    peer_id: Incomplete
    date: Incomplete
    def __init__(self, peer_id: TypePeer, date: datetime | None) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class PeerChannel(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    channel_id: Incomplete
    def __init__(self, channel_id: int) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class PeerChat(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    chat_id: Incomplete
    def __init__(self, chat_id: int) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class PeerColor(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    color: Incomplete
    background_emoji_id: Incomplete
    def __init__(self, color: int | None = None, background_emoji_id: int | None = None) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class PeerLocated(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    peer: Incomplete
    expires: Incomplete
    distance: Incomplete
    def __init__(self, peer: TypePeer, expires: datetime | None, distance: int) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class PeerNotifySettings(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    show_previews: Incomplete
    silent: Incomplete
    mute_until: Incomplete
    ios_sound: Incomplete
    android_sound: Incomplete
    other_sound: Incomplete
    stories_muted: Incomplete
    stories_hide_sender: Incomplete
    stories_ios_sound: Incomplete
    stories_android_sound: Incomplete
    stories_other_sound: Incomplete
    def __init__(self, show_previews: bool | None = None, silent: bool | None = None, mute_until: datetime | None = None, ios_sound: TypeNotificationSound | None = None, android_sound: TypeNotificationSound | None = None, other_sound: TypeNotificationSound | None = None, stories_muted: bool | None = None, stories_hide_sender: bool | None = None, stories_ios_sound: TypeNotificationSound | None = None, stories_android_sound: TypeNotificationSound | None = None, stories_other_sound: TypeNotificationSound | None = None) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class PeerSelfLocated(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    expires: Incomplete
    def __init__(self, expires: datetime | None) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class PeerSettings(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    report_spam: Incomplete
    add_contact: Incomplete
    block_contact: Incomplete
    share_contact: Incomplete
    need_contacts_exception: Incomplete
    report_geo: Incomplete
    autoarchived: Incomplete
    invite_members: Incomplete
    request_chat_broadcast: Incomplete
    business_bot_paused: Incomplete
    business_bot_can_reply: Incomplete
    geo_distance: Incomplete
    request_chat_title: Incomplete
    request_chat_date: Incomplete
    business_bot_id: Incomplete
    business_bot_manage_url: Incomplete
    def __init__(self, report_spam: bool | None = None, add_contact: bool | None = None, block_contact: bool | None = None, share_contact: bool | None = None, need_contacts_exception: bool | None = None, report_geo: bool | None = None, autoarchived: bool | None = None, invite_members: bool | None = None, request_chat_broadcast: bool | None = None, business_bot_paused: bool | None = None, business_bot_can_reply: bool | None = None, geo_distance: int | None = None, request_chat_title: str | None = None, request_chat_date: datetime | None = None, business_bot_id: int | None = None, business_bot_manage_url: str | None = None) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class PeerStories(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    peer: Incomplete
    stories: Incomplete
    max_read_id: Incomplete
    def __init__(self, peer: TypePeer, stories: list['TypeStoryItem'], max_read_id: int | None = None) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class PeerUser(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    user_id: Incomplete
    def __init__(self, user_id: int) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class PhoneCall(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    id: Incomplete
    access_hash: Incomplete
    date: Incomplete
    admin_id: Incomplete
    participant_id: Incomplete
    g_a_or_b: Incomplete
    key_fingerprint: Incomplete
    protocol: Incomplete
    connections: Incomplete
    start_date: Incomplete
    p2p_allowed: Incomplete
    video: Incomplete
    custom_parameters: Incomplete
    def __init__(self, id: int, access_hash: int, date: datetime | None, admin_id: int, participant_id: int, g_a_or_b: bytes, key_fingerprint: int, protocol: TypePhoneCallProtocol, connections: list['TypePhoneConnection'], start_date: datetime | None, p2p_allowed: bool | None = None, video: bool | None = None, custom_parameters: TypeDataJSON | None = None) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class PhoneCallAccepted(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    id: Incomplete
    access_hash: Incomplete
    date: Incomplete
    admin_id: Incomplete
    participant_id: Incomplete
    g_b: Incomplete
    protocol: Incomplete
    video: Incomplete
    def __init__(self, id: int, access_hash: int, date: datetime | None, admin_id: int, participant_id: int, g_b: bytes, protocol: TypePhoneCallProtocol, video: bool | None = None) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class PhoneCallDiscardReasonBusy(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class PhoneCallDiscardReasonDisconnect(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class PhoneCallDiscardReasonHangup(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class PhoneCallDiscardReasonMissed(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class PhoneCallDiscarded(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    id: Incomplete
    need_rating: Incomplete
    need_debug: Incomplete
    video: Incomplete
    reason: Incomplete
    duration: Incomplete
    def __init__(self, id: int, need_rating: bool | None = None, need_debug: bool | None = None, video: bool | None = None, reason: TypePhoneCallDiscardReason | None = None, duration: int | None = None) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class PhoneCallEmpty(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    id: Incomplete
    def __init__(self, id: int) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class PhoneCallProtocol(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    min_layer: Incomplete
    max_layer: Incomplete
    library_versions: Incomplete
    udp_p2p: Incomplete
    udp_reflector: Incomplete
    def __init__(self, min_layer: int, max_layer: int, library_versions: list[str], udp_p2p: bool | None = None, udp_reflector: bool | None = None) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class PhoneCallRequested(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    id: Incomplete
    access_hash: Incomplete
    date: Incomplete
    admin_id: Incomplete
    participant_id: Incomplete
    g_a_hash: Incomplete
    protocol: Incomplete
    video: Incomplete
    def __init__(self, id: int, access_hash: int, date: datetime | None, admin_id: int, participant_id: int, g_a_hash: bytes, protocol: TypePhoneCallProtocol, video: bool | None = None) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class PhoneCallWaiting(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    id: Incomplete
    access_hash: Incomplete
    date: Incomplete
    admin_id: Incomplete
    participant_id: Incomplete
    protocol: Incomplete
    video: Incomplete
    receive_date: Incomplete
    def __init__(self, id: int, access_hash: int, date: datetime | None, admin_id: int, participant_id: int, protocol: TypePhoneCallProtocol, video: bool | None = None, receive_date: datetime | None = None) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class PhoneConnection(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    id: Incomplete
    ip: Incomplete
    ipv6: Incomplete
    port: Incomplete
    peer_tag: Incomplete
    tcp: Incomplete
    def __init__(self, id: int, ip: str, ipv6: str, port: int, peer_tag: bytes, tcp: bool | None = None) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class PhoneConnectionWebrtc(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    id: Incomplete
    ip: Incomplete
    ipv6: Incomplete
    port: Incomplete
    username: Incomplete
    password: Incomplete
    turn: Incomplete
    stun: Incomplete
    def __init__(self, id: int, ip: str, ipv6: str, port: int, username: str, password: str, turn: bool | None = None, stun: bool | None = None) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class Photo(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    id: Incomplete
    access_hash: Incomplete
    file_reference: Incomplete
    date: Incomplete
    sizes: Incomplete
    dc_id: Incomplete
    has_stickers: Incomplete
    video_sizes: Incomplete
    def __init__(self, id: int, access_hash: int, file_reference: bytes, date: datetime | None, sizes: list['TypePhotoSize'], dc_id: int, has_stickers: bool | None = None, video_sizes: list['TypeVideoSize'] | None = None) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class PhotoCachedSize(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    type: Incomplete
    w: Incomplete
    h: Incomplete
    bytes: Incomplete
    def __init__(self, type: str, w: int, h: int, bytes: bytes) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class PhotoEmpty(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    id: Incomplete
    def __init__(self, id: int) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class PhotoPathSize(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    type: Incomplete
    bytes: Incomplete
    def __init__(self, type: str, bytes: bytes) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class PhotoSize(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    type: Incomplete
    w: Incomplete
    h: Incomplete
    size: Incomplete
    def __init__(self, type: str, w: int, h: int, size: int) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class PhotoSizeEmpty(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    type: Incomplete
    def __init__(self, type: str) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class PhotoSizeProgressive(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    type: Incomplete
    w: Incomplete
    h: Incomplete
    sizes: Incomplete
    def __init__(self, type: str, w: int, h: int, sizes: list[int]) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class PhotoStrippedSize(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    type: Incomplete
    bytes: Incomplete
    def __init__(self, type: str, bytes: bytes) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class Poll(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    id: Incomplete
    question: Incomplete
    answers: Incomplete
    closed: Incomplete
    public_voters: Incomplete
    multiple_choice: Incomplete
    quiz: Incomplete
    close_period: Incomplete
    close_date: Incomplete
    def __init__(self, id: int, question: TypeTextWithEntities, answers: list['TypePollAnswer'], closed: bool | None = None, public_voters: bool | None = None, multiple_choice: bool | None = None, quiz: bool | None = None, close_period: int | None = None, close_date: datetime | None = None) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class PollAnswer(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    text: Incomplete
    option: Incomplete
    def __init__(self, text: TypeTextWithEntities, option: bytes) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class PollAnswerVoters(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    option: Incomplete
    voters: Incomplete
    chosen: Incomplete
    correct: Incomplete
    def __init__(self, option: bytes, voters: int, chosen: bool | None = None, correct: bool | None = None) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class PollResults(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    min: Incomplete
    results: Incomplete
    total_voters: Incomplete
    recent_voters: Incomplete
    solution: Incomplete
    solution_entities: Incomplete
    def __init__(self, min: bool | None = None, results: list['TypePollAnswerVoters'] | None = None, total_voters: int | None = None, recent_voters: list['TypePeer'] | None = None, solution: str | None = None, solution_entities: list['TypeMessageEntity'] | None = None) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class Pong(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    msg_id: Incomplete
    ping_id: Incomplete
    def __init__(self, msg_id: int, ping_id: int) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class PopularContact(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    client_id: Incomplete
    importers: Incomplete
    def __init__(self, client_id: int, importers: int) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class PostAddress(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    street_line1: Incomplete
    street_line2: Incomplete
    city: Incomplete
    state: Incomplete
    country_iso2: Incomplete
    post_code: Incomplete
    def __init__(self, street_line1: str, street_line2: str, city: str, state: str, country_iso2: str, post_code: str) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class PostInteractionCountersMessage(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    msg_id: Incomplete
    views: Incomplete
    forwards: Incomplete
    reactions: Incomplete
    def __init__(self, msg_id: int, views: int, forwards: int, reactions: int) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class PostInteractionCountersStory(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    story_id: Incomplete
    views: Incomplete
    forwards: Incomplete
    reactions: Incomplete
    def __init__(self, story_id: int, views: int, forwards: int, reactions: int) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class PremiumGiftCodeOption(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    users: Incomplete
    months: Incomplete
    currency: Incomplete
    amount: Incomplete
    store_product: Incomplete
    store_quantity: Incomplete
    def __init__(self, users: int, months: int, currency: str, amount: int, store_product: str | None = None, store_quantity: int | None = None) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class PremiumGiftOption(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    months: Incomplete
    currency: Incomplete
    amount: Incomplete
    bot_url: Incomplete
    store_product: Incomplete
    def __init__(self, months: int, currency: str, amount: int, bot_url: str, store_product: str | None = None) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class PremiumSubscriptionOption(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    months: Incomplete
    currency: Incomplete
    amount: Incomplete
    bot_url: Incomplete
    current: Incomplete
    can_purchase_upgrade: Incomplete
    transaction: Incomplete
    store_product: Incomplete
    def __init__(self, months: int, currency: str, amount: int, bot_url: str, current: bool | None = None, can_purchase_upgrade: bool | None = None, transaction: str | None = None, store_product: str | None = None) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class PrepaidGiveaway(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    id: Incomplete
    months: Incomplete
    quantity: Incomplete
    date: Incomplete
    def __init__(self, id: int, months: int, quantity: int, date: datetime | None) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class PrepaidStarsGiveaway(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    id: Incomplete
    stars: Incomplete
    quantity: Incomplete
    boosts: Incomplete
    date: Incomplete
    def __init__(self, id: int, stars: int, quantity: int, boosts: int, date: datetime | None) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class PrivacyKeyAbout(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class PrivacyKeyAddedByPhone(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class PrivacyKeyBirthday(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class PrivacyKeyChatInvite(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class PrivacyKeyForwards(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class PrivacyKeyPhoneCall(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class PrivacyKeyPhoneNumber(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class PrivacyKeyPhoneP2P(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class PrivacyKeyProfilePhoto(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class PrivacyKeyStarGiftsAutoSave(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class PrivacyKeyStatusTimestamp(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class PrivacyKeyVoiceMessages(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class PrivacyValueAllowAll(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class PrivacyValueAllowBots(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class PrivacyValueAllowChatParticipants(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    chats: Incomplete
    def __init__(self, chats: list[int]) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class PrivacyValueAllowCloseFriends(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class PrivacyValueAllowContacts(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class PrivacyValueAllowPremium(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class PrivacyValueAllowUsers(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    users: Incomplete
    def __init__(self, users: list[int]) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class PrivacyValueDisallowAll(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class PrivacyValueDisallowBots(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class PrivacyValueDisallowChatParticipants(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    chats: Incomplete
    def __init__(self, chats: list[int]) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class PrivacyValueDisallowContacts(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class PrivacyValueDisallowUsers(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    users: Incomplete
    def __init__(self, users: list[int]) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class PublicForwardMessage(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    message: Incomplete
    def __init__(self, message: TypeMessage) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class PublicForwardStory(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    peer: Incomplete
    story: Incomplete
    def __init__(self, peer: TypePeer, story: TypeStoryItem) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class QuickReply(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    shortcut_id: Incomplete
    shortcut: Incomplete
    top_message: Incomplete
    count: Incomplete
    def __init__(self, shortcut_id: int, shortcut: str, top_message: int, count: int) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class ReactionCount(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    reaction: Incomplete
    count: Incomplete
    chosen_order: Incomplete
    def __init__(self, reaction: TypeReaction, count: int, chosen_order: int | None = None) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class ReactionCustomEmoji(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    document_id: Incomplete
    def __init__(self, document_id: int) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class ReactionEmoji(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    emoticon: Incomplete
    def __init__(self, emoticon: str) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class ReactionEmpty(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class ReactionNotificationsFromAll(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class ReactionNotificationsFromContacts(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class ReactionPaid(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class ReactionsNotifySettings(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    sound: Incomplete
    show_previews: Incomplete
    messages_notify_from: Incomplete
    stories_notify_from: Incomplete
    def __init__(self, sound: TypeNotificationSound, show_previews: bool, messages_notify_from: TypeReactionNotificationsFrom | None = None, stories_notify_from: TypeReactionNotificationsFrom | None = None) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class ReadParticipantDate(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    user_id: Incomplete
    date: Incomplete
    def __init__(self, user_id: int, date: datetime | None) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class ReceivedNotifyMessage(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    id: Incomplete
    flags: Incomplete
    def __init__(self, id: int, flags: int) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class RecentMeUrlChat(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    url: Incomplete
    chat_id: Incomplete
    def __init__(self, url: str, chat_id: int) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class RecentMeUrlChatInvite(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    url: Incomplete
    chat_invite: Incomplete
    def __init__(self, url: str, chat_invite: TypeChatInvite) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class RecentMeUrlStickerSet(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    url: Incomplete
    set: Incomplete
    def __init__(self, url: str, set: TypeStickerSetCovered) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class RecentMeUrlUnknown(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    url: Incomplete
    def __init__(self, url: str) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class RecentMeUrlUser(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    url: Incomplete
    user_id: Incomplete
    def __init__(self, url: str, user_id: int) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class ReplyInlineMarkup(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    rows: Incomplete
    def __init__(self, rows: list['TypeKeyboardButtonRow']) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class ReplyKeyboardForceReply(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    single_use: Incomplete
    selective: Incomplete
    placeholder: Incomplete
    def __init__(self, single_use: bool | None = None, selective: bool | None = None, placeholder: str | None = None) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class ReplyKeyboardHide(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    selective: Incomplete
    def __init__(self, selective: bool | None = None) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class ReplyKeyboardMarkup(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    rows: Incomplete
    resize: Incomplete
    single_use: Incomplete
    selective: Incomplete
    persistent: Incomplete
    placeholder: Incomplete
    def __init__(self, rows: list['TypeKeyboardButtonRow'], resize: bool | None = None, single_use: bool | None = None, selective: bool | None = None, persistent: bool | None = None, placeholder: str | None = None) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class ReportResultAddComment(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    option: Incomplete
    optional: Incomplete
    def __init__(self, option: bytes, optional: bool | None = None) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class ReportResultChooseOption(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    title: Incomplete
    options: Incomplete
    def __init__(self, title: str, options: list['TypeMessageReportOption']) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class ReportResultReported(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class RequestPeerTypeBroadcast(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    creator: Incomplete
    has_username: Incomplete
    user_admin_rights: Incomplete
    bot_admin_rights: Incomplete
    def __init__(self, creator: bool | None = None, has_username: bool | None = None, user_admin_rights: TypeChatAdminRights | None = None, bot_admin_rights: TypeChatAdminRights | None = None) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class RequestPeerTypeChat(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    creator: Incomplete
    bot_participant: Incomplete
    has_username: Incomplete
    forum: Incomplete
    user_admin_rights: Incomplete
    bot_admin_rights: Incomplete
    def __init__(self, creator: bool | None = None, bot_participant: bool | None = None, has_username: bool | None = None, forum: bool | None = None, user_admin_rights: TypeChatAdminRights | None = None, bot_admin_rights: TypeChatAdminRights | None = None) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class RequestPeerTypeUser(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    bot: Incomplete
    premium: Incomplete
    def __init__(self, bot: bool | None = None, premium: bool | None = None) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class RequestedPeerChannel(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    channel_id: Incomplete
    title: Incomplete
    username: Incomplete
    photo: Incomplete
    def __init__(self, channel_id: int, title: str | None = None, username: str | None = None, photo: TypePhoto | None = None) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class RequestedPeerChat(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    chat_id: Incomplete
    title: Incomplete
    photo: Incomplete
    def __init__(self, chat_id: int, title: str | None = None, photo: TypePhoto | None = None) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class RequestedPeerUser(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    user_id: Incomplete
    first_name: Incomplete
    last_name: Incomplete
    username: Incomplete
    photo: Incomplete
    def __init__(self, user_id: int, first_name: str | None = None, last_name: str | None = None, username: str | None = None, photo: TypePhoto | None = None) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class ResPQ(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    nonce: Incomplete
    server_nonce: Incomplete
    pq: Incomplete
    server_public_key_fingerprints: Incomplete
    def __init__(self, nonce: int, server_nonce: int, pq: bytes, server_public_key_fingerprints: list[int]) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class RestrictionReason(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    platform: Incomplete
    reason: Incomplete
    text: Incomplete
    def __init__(self, platform: str, reason: str, text: str) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class RpcAnswerDropped(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    msg_id: Incomplete
    seq_no: Incomplete
    bytes: Incomplete
    def __init__(self, msg_id: int, seq_no: int, bytes: int) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class RpcAnswerDroppedRunning(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class RpcAnswerUnknown(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class RpcError(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    error_code: Incomplete
    error_message: Incomplete
    def __init__(self, error_code: int, error_message: str) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class SavedDialog(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    peer: Incomplete
    top_message: Incomplete
    pinned: Incomplete
    def __init__(self, peer: TypePeer, top_message: int, pinned: bool | None = None) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class SavedPhoneContact(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    phone: Incomplete
    first_name: Incomplete
    last_name: Incomplete
    date: Incomplete
    def __init__(self, phone: str, first_name: str, last_name: str, date: datetime | None) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class SavedReactionTag(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    reaction: Incomplete
    count: Incomplete
    title: Incomplete
    def __init__(self, reaction: TypeReaction, count: int, title: str | None = None) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class SearchResultPosition(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    msg_id: Incomplete
    date: Incomplete
    offset: Incomplete
    def __init__(self, msg_id: int, date: datetime | None, offset: int) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class SearchResultsCalendarPeriod(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    date: Incomplete
    min_msg_id: Incomplete
    max_msg_id: Incomplete
    count: Incomplete
    def __init__(self, date: datetime | None, min_msg_id: int, max_msg_id: int, count: int) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class SecureCredentialsEncrypted(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    data: Incomplete
    hash: Incomplete
    secret: Incomplete
    def __init__(self, data: bytes, hash: bytes, secret: bytes) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class SecureData(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    data: Incomplete
    data_hash: Incomplete
    secret: Incomplete
    def __init__(self, data: bytes, data_hash: bytes, secret: bytes) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class SecureFile(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    id: Incomplete
    access_hash: Incomplete
    size: Incomplete
    dc_id: Incomplete
    date: Incomplete
    file_hash: Incomplete
    secret: Incomplete
    def __init__(self, id: int, access_hash: int, size: int, dc_id: int, date: datetime | None, file_hash: bytes, secret: bytes) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class SecureFileEmpty(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class SecurePasswordKdfAlgoPBKDF2HMACSHA512iter100000(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    salt: Incomplete
    def __init__(self, salt: bytes) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class SecurePasswordKdfAlgoSHA512(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    salt: Incomplete
    def __init__(self, salt: bytes) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class SecurePasswordKdfAlgoUnknown(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class SecurePlainEmail(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    email: Incomplete
    def __init__(self, email: str) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class SecurePlainPhone(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    phone: Incomplete
    def __init__(self, phone: str) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class SecureRequiredType(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    type: Incomplete
    native_names: Incomplete
    selfie_required: Incomplete
    translation_required: Incomplete
    def __init__(self, type: TypeSecureValueType, native_names: bool | None = None, selfie_required: bool | None = None, translation_required: bool | None = None) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class SecureRequiredTypeOneOf(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    types: Incomplete
    def __init__(self, types: list['TypeSecureRequiredType']) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class SecureSecretSettings(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    secure_algo: Incomplete
    secure_secret: Incomplete
    secure_secret_id: Incomplete
    def __init__(self, secure_algo: TypeSecurePasswordKdfAlgo, secure_secret: bytes, secure_secret_id: int) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class SecureValue(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    type: Incomplete
    hash: Incomplete
    data: Incomplete
    front_side: Incomplete
    reverse_side: Incomplete
    selfie: Incomplete
    translation: Incomplete
    files: Incomplete
    plain_data: Incomplete
    def __init__(self, type: TypeSecureValueType, hash: bytes, data: TypeSecureData | None = None, front_side: TypeSecureFile | None = None, reverse_side: TypeSecureFile | None = None, selfie: TypeSecureFile | None = None, translation: list['TypeSecureFile'] | None = None, files: list['TypeSecureFile'] | None = None, plain_data: TypeSecurePlainData | None = None) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class SecureValueError(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    type: Incomplete
    hash: Incomplete
    text: Incomplete
    def __init__(self, type: TypeSecureValueType, hash: bytes, text: str) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class SecureValueErrorData(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    type: Incomplete
    data_hash: Incomplete
    field: Incomplete
    text: Incomplete
    def __init__(self, type: TypeSecureValueType, data_hash: bytes, field: str, text: str) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class SecureValueErrorFile(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    type: Incomplete
    file_hash: Incomplete
    text: Incomplete
    def __init__(self, type: TypeSecureValueType, file_hash: bytes, text: str) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class SecureValueErrorFiles(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    type: Incomplete
    file_hash: Incomplete
    text: Incomplete
    def __init__(self, type: TypeSecureValueType, file_hash: list[bytes], text: str) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class SecureValueErrorFrontSide(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    type: Incomplete
    file_hash: Incomplete
    text: Incomplete
    def __init__(self, type: TypeSecureValueType, file_hash: bytes, text: str) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class SecureValueErrorReverseSide(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    type: Incomplete
    file_hash: Incomplete
    text: Incomplete
    def __init__(self, type: TypeSecureValueType, file_hash: bytes, text: str) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class SecureValueErrorSelfie(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    type: Incomplete
    file_hash: Incomplete
    text: Incomplete
    def __init__(self, type: TypeSecureValueType, file_hash: bytes, text: str) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class SecureValueErrorTranslationFile(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    type: Incomplete
    file_hash: Incomplete
    text: Incomplete
    def __init__(self, type: TypeSecureValueType, file_hash: bytes, text: str) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class SecureValueErrorTranslationFiles(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    type: Incomplete
    file_hash: Incomplete
    text: Incomplete
    def __init__(self, type: TypeSecureValueType, file_hash: list[bytes], text: str) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class SecureValueHash(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    type: Incomplete
    hash: Incomplete
    def __init__(self, type: TypeSecureValueType, hash: bytes) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class SecureValueTypeAddress(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class SecureValueTypeBankStatement(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class SecureValueTypeDriverLicense(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class SecureValueTypeEmail(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class SecureValueTypeIdentityCard(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class SecureValueTypeInternalPassport(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class SecureValueTypePassport(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class SecureValueTypePassportRegistration(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class SecureValueTypePersonalDetails(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class SecureValueTypePhone(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class SecureValueTypeRentalAgreement(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class SecureValueTypeTemporaryRegistration(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class SecureValueTypeUtilityBill(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class SendAsPeer(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    peer: Incomplete
    premium_required: Incomplete
    def __init__(self, peer: TypePeer, premium_required: bool | None = None) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class SendMessageCancelAction(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class SendMessageChooseContactAction(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class SendMessageChooseStickerAction(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class SendMessageEmojiInteraction(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    emoticon: Incomplete
    msg_id: Incomplete
    interaction: Incomplete
    def __init__(self, emoticon: str, msg_id: int, interaction: TypeDataJSON) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class SendMessageEmojiInteractionSeen(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    emoticon: Incomplete
    def __init__(self, emoticon: str) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class SendMessageGamePlayAction(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class SendMessageGeoLocationAction(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class SendMessageHistoryImportAction(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    progress: Incomplete
    def __init__(self, progress: int) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class SendMessageRecordAudioAction(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class SendMessageRecordRoundAction(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class SendMessageRecordVideoAction(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class SendMessageTypingAction(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class SendMessageUploadAudioAction(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    progress: Incomplete
    def __init__(self, progress: int) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class SendMessageUploadDocumentAction(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    progress: Incomplete
    def __init__(self, progress: int) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class SendMessageUploadPhotoAction(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    progress: Incomplete
    def __init__(self, progress: int) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class SendMessageUploadRoundAction(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    progress: Incomplete
    def __init__(self, progress: int) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class SendMessageUploadVideoAction(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    progress: Incomplete
    def __init__(self, progress: int) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class ServerDHInnerData(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    nonce: Incomplete
    server_nonce: Incomplete
    g: Incomplete
    dh_prime: Incomplete
    g_a: Incomplete
    server_time: Incomplete
    def __init__(self, nonce: int, server_nonce: int, g: int, dh_prime: bytes, g_a: bytes, server_time: int) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class ServerDHParamsFail(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    nonce: Incomplete
    server_nonce: Incomplete
    new_nonce_hash: Incomplete
    def __init__(self, nonce: int, server_nonce: int, new_nonce_hash: int) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class ServerDHParamsOk(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    nonce: Incomplete
    server_nonce: Incomplete
    encrypted_answer: Incomplete
    def __init__(self, nonce: int, server_nonce: int, encrypted_answer: bytes) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class ShippingOption(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    id: Incomplete
    title: Incomplete
    prices: Incomplete
    def __init__(self, id: str, title: str, prices: list['TypeLabeledPrice']) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class SmsJob(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    job_id: Incomplete
    phone_number: Incomplete
    text: Incomplete
    def __init__(self, job_id: str, phone_number: str, text: str) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class SpeakingInGroupCallAction(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class SponsoredMessage(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    url: Incomplete
    title: Incomplete
    message: Incomplete
    button_text: Incomplete
    recommended: Incomplete
    can_report: Incomplete
    random_id: Incomplete
    entities: Incomplete
    photo: Incomplete
    media: Incomplete
    color: Incomplete
    sponsor_info: Incomplete
    additional_info: Incomplete
    def __init__(self, url: str, title: str, message: str, button_text: str, recommended: bool | None = None, can_report: bool | None = None, random_id: bytes = None, entities: list['TypeMessageEntity'] | None = None, photo: TypePhoto | None = None, media: TypeMessageMedia | None = None, color: TypePeerColor | None = None, sponsor_info: str | None = None, additional_info: str | None = None) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class SponsoredMessageReportOption(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    text: Incomplete
    option: Incomplete
    def __init__(self, text: str, option: bytes) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class StarGift(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    id: Incomplete
    sticker: Incomplete
    stars: Incomplete
    convert_stars: Incomplete
    limited: Incomplete
    sold_out: Incomplete
    birthday: Incomplete
    availability_remains: Incomplete
    availability_total: Incomplete
    first_sale_date: Incomplete
    last_sale_date: Incomplete
    def __init__(self, id: int, sticker: TypeDocument, stars: int, convert_stars: int, limited: bool | None = None, sold_out: bool | None = None, birthday: bool | None = None, availability_remains: int | None = None, availability_total: int | None = None, first_sale_date: datetime | None = None, last_sale_date: datetime | None = None) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class StarsGiftOption(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    stars: Incomplete
    currency: Incomplete
    amount: Incomplete
    extended: Incomplete
    store_product: Incomplete
    def __init__(self, stars: int, currency: str, amount: int, extended: bool | None = None, store_product: str | None = None) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class StarsGiveawayOption(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    stars: Incomplete
    yearly_boosts: Incomplete
    currency: Incomplete
    amount: Incomplete
    winners: Incomplete
    extended: Incomplete
    default: Incomplete
    store_product: Incomplete
    def __init__(self, stars: int, yearly_boosts: int, currency: str, amount: int, winners: list['TypeStarsGiveawayWinnersOption'], extended: bool | None = None, default: bool | None = None, store_product: str | None = None) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class StarsGiveawayWinnersOption(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    users: Incomplete
    per_user_stars: Incomplete
    default: Incomplete
    def __init__(self, users: int, per_user_stars: int, default: bool | None = None) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class StarsRevenueStatus(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    current_balance: Incomplete
    available_balance: Incomplete
    overall_revenue: Incomplete
    withdrawal_enabled: Incomplete
    next_withdrawal_at: Incomplete
    def __init__(self, current_balance: int, available_balance: int, overall_revenue: int, withdrawal_enabled: bool | None = None, next_withdrawal_at: int | None = None) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class StarsSubscription(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    id: Incomplete
    peer: Incomplete
    until_date: Incomplete
    pricing: Incomplete
    canceled: Incomplete
    can_refulfill: Incomplete
    missing_balance: Incomplete
    bot_canceled: Incomplete
    chat_invite_hash: Incomplete
    title: Incomplete
    photo: Incomplete
    invoice_slug: Incomplete
    def __init__(self, id: str, peer: TypePeer, until_date: datetime | None, pricing: TypeStarsSubscriptionPricing, canceled: bool | None = None, can_refulfill: bool | None = None, missing_balance: bool | None = None, bot_canceled: bool | None = None, chat_invite_hash: str | None = None, title: str | None = None, photo: TypeWebDocument | None = None, invoice_slug: str | None = None) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class StarsSubscriptionPricing(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    period: Incomplete
    amount: Incomplete
    def __init__(self, period: int, amount: int) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class StarsTopupOption(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    stars: Incomplete
    currency: Incomplete
    amount: Incomplete
    extended: Incomplete
    store_product: Incomplete
    def __init__(self, stars: int, currency: str, amount: int, extended: bool | None = None, store_product: str | None = None) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class StarsTransaction(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    id: Incomplete
    stars: Incomplete
    date: Incomplete
    peer: Incomplete
    refund: Incomplete
    pending: Incomplete
    failed: Incomplete
    gift: Incomplete
    reaction: Incomplete
    title: Incomplete
    description: Incomplete
    photo: Incomplete
    transaction_date: Incomplete
    transaction_url: Incomplete
    bot_payload: Incomplete
    msg_id: Incomplete
    extended_media: Incomplete
    subscription_period: Incomplete
    giveaway_post_id: Incomplete
    stargift: Incomplete
    floodskip_number: Incomplete
    def __init__(self, id: str, stars: int, date: datetime | None, peer: TypeStarsTransactionPeer, refund: bool | None = None, pending: bool | None = None, failed: bool | None = None, gift: bool | None = None, reaction: bool | None = None, title: str | None = None, description: str | None = None, photo: TypeWebDocument | None = None, transaction_date: datetime | None = None, transaction_url: str | None = None, bot_payload: bytes | None = None, msg_id: int | None = None, extended_media: list['TypeMessageMedia'] | None = None, subscription_period: int | None = None, giveaway_post_id: int | None = None, stargift: TypeStarGift | None = None, floodskip_number: int | None = None) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class StarsTransactionPeer(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    peer: Incomplete
    def __init__(self, peer: TypePeer) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class StarsTransactionPeerAPI(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class StarsTransactionPeerAds(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class StarsTransactionPeerAppStore(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class StarsTransactionPeerFragment(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class StarsTransactionPeerPlayMarket(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class StarsTransactionPeerPremiumBot(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class StarsTransactionPeerUnsupported(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class StatsAbsValueAndPrev(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    current: Incomplete
    previous: Incomplete
    def __init__(self, current: float, previous: float) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class StatsDateRangeDays(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    min_date: Incomplete
    max_date: Incomplete
    def __init__(self, min_date: datetime | None, max_date: datetime | None) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class StatsGraph(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    json: Incomplete
    zoom_token: Incomplete
    def __init__(self, json: TypeDataJSON, zoom_token: str | None = None) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class StatsGraphAsync(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    token: Incomplete
    def __init__(self, token: str) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class StatsGraphError(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    error: Incomplete
    def __init__(self, error: str) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class StatsGroupTopAdmin(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    user_id: Incomplete
    deleted: Incomplete
    kicked: Incomplete
    banned: Incomplete
    def __init__(self, user_id: int, deleted: int, kicked: int, banned: int) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class StatsGroupTopInviter(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    user_id: Incomplete
    invitations: Incomplete
    def __init__(self, user_id: int, invitations: int) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class StatsGroupTopPoster(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    user_id: Incomplete
    messages: Incomplete
    avg_chars: Incomplete
    def __init__(self, user_id: int, messages: int, avg_chars: int) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class StatsPercentValue(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    part: Incomplete
    total: Incomplete
    def __init__(self, part: float, total: float) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class StatsURL(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    url: Incomplete
    def __init__(self, url: str) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class StickerKeyword(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    document_id: Incomplete
    keyword: Incomplete
    def __init__(self, document_id: int, keyword: list[str]) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class StickerPack(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    emoticon: Incomplete
    documents: Incomplete
    def __init__(self, emoticon: str, documents: list[int]) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class StickerSet(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    id: Incomplete
    access_hash: Incomplete
    title: Incomplete
    short_name: Incomplete
    count: Incomplete
    hash: Incomplete
    archived: Incomplete
    official: Incomplete
    masks: Incomplete
    emojis: Incomplete
    text_color: Incomplete
    channel_emoji_status: Incomplete
    creator: Incomplete
    installed_date: Incomplete
    thumbs: Incomplete
    thumb_dc_id: Incomplete
    thumb_version: Incomplete
    thumb_document_id: Incomplete
    def __init__(self, id: int, access_hash: int, title: str, short_name: str, count: int, hash: int, archived: bool | None = None, official: bool | None = None, masks: bool | None = None, emojis: bool | None = None, text_color: bool | None = None, channel_emoji_status: bool | None = None, creator: bool | None = None, installed_date: datetime | None = None, thumbs: list['TypePhotoSize'] | None = None, thumb_dc_id: int | None = None, thumb_version: int | None = None, thumb_document_id: int | None = None) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class StickerSetCovered(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    set: Incomplete
    cover: Incomplete
    def __init__(self, set: TypeStickerSet, cover: TypeDocument) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class StickerSetFullCovered(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    set: Incomplete
    packs: Incomplete
    keywords: Incomplete
    documents: Incomplete
    def __init__(self, set: TypeStickerSet, packs: list['TypeStickerPack'], keywords: list['TypeStickerKeyword'], documents: list['TypeDocument']) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class StickerSetMultiCovered(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    set: Incomplete
    covers: Incomplete
    def __init__(self, set: TypeStickerSet, covers: list['TypeDocument']) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class StickerSetNoCovered(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    set: Incomplete
    def __init__(self, set: TypeStickerSet) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class StoriesStealthMode(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    active_until_date: Incomplete
    cooldown_until_date: Incomplete
    def __init__(self, active_until_date: datetime | None = None, cooldown_until_date: datetime | None = None) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class StoryFwdHeader(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    modified: Incomplete
    from_: Incomplete
    from_name: Incomplete
    story_id: Incomplete
    def __init__(self, modified: bool | None = None, from_: TypePeer | None = None, from_name: str | None = None, story_id: int | None = None) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class StoryItem(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    id: Incomplete
    date: Incomplete
    expire_date: Incomplete
    media: Incomplete
    pinned: Incomplete
    public: Incomplete
    close_friends: Incomplete
    min: Incomplete
    noforwards: Incomplete
    edited: Incomplete
    contacts: Incomplete
    selected_contacts: Incomplete
    out: Incomplete
    from_id: Incomplete
    fwd_from: Incomplete
    caption: Incomplete
    entities: Incomplete
    media_areas: Incomplete
    privacy: Incomplete
    views: Incomplete
    sent_reaction: Incomplete
    def __init__(self, id: int, date: datetime | None, expire_date: datetime | None, media: TypeMessageMedia, pinned: bool | None = None, public: bool | None = None, close_friends: bool | None = None, min: bool | None = None, noforwards: bool | None = None, edited: bool | None = None, contacts: bool | None = None, selected_contacts: bool | None = None, out: bool | None = None, from_id: TypePeer | None = None, fwd_from: TypeStoryFwdHeader | None = None, caption: str | None = None, entities: list['TypeMessageEntity'] | None = None, media_areas: list['TypeMediaArea'] | None = None, privacy: list['TypePrivacyRule'] | None = None, views: TypeStoryViews | None = None, sent_reaction: TypeReaction | None = None) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class StoryItemDeleted(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    id: Incomplete
    def __init__(self, id: int) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class StoryItemSkipped(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    id: Incomplete
    date: Incomplete
    expire_date: Incomplete
    close_friends: Incomplete
    def __init__(self, id: int, date: datetime | None, expire_date: datetime | None, close_friends: bool | None = None) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class StoryReaction(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    peer_id: Incomplete
    date: Incomplete
    reaction: Incomplete
    def __init__(self, peer_id: TypePeer, date: datetime | None, reaction: TypeReaction) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class StoryReactionPublicForward(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    message: Incomplete
    def __init__(self, message: TypeMessage) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class StoryReactionPublicRepost(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    peer_id: Incomplete
    story: Incomplete
    def __init__(self, peer_id: TypePeer, story: TypeStoryItem) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class StoryView(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    user_id: Incomplete
    date: Incomplete
    blocked: Incomplete
    blocked_my_stories_from: Incomplete
    reaction: Incomplete
    def __init__(self, user_id: int, date: datetime | None, blocked: bool | None = None, blocked_my_stories_from: bool | None = None, reaction: TypeReaction | None = None) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class StoryViewPublicForward(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    message: Incomplete
    blocked: Incomplete
    blocked_my_stories_from: Incomplete
    def __init__(self, message: TypeMessage, blocked: bool | None = None, blocked_my_stories_from: bool | None = None) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class StoryViewPublicRepost(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    peer_id: Incomplete
    story: Incomplete
    blocked: Incomplete
    blocked_my_stories_from: Incomplete
    def __init__(self, peer_id: TypePeer, story: TypeStoryItem, blocked: bool | None = None, blocked_my_stories_from: bool | None = None) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class StoryViews(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    views_count: Incomplete
    has_viewers: Incomplete
    forwards_count: Incomplete
    reactions: Incomplete
    reactions_count: Incomplete
    recent_viewers: Incomplete
    def __init__(self, views_count: int, has_viewers: bool | None = None, forwards_count: int | None = None, reactions: list['TypeReactionCount'] | None = None, reactions_count: int | None = None, recent_viewers: list[int] | None = None) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class TextAnchor(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    text: Incomplete
    name: Incomplete
    def __init__(self, text: TypeRichText, name: str) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class TextBold(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    text: Incomplete
    def __init__(self, text: TypeRichText) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class TextConcat(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    texts: Incomplete
    def __init__(self, texts: list['TypeRichText']) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class TextEmail(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    text: Incomplete
    email: Incomplete
    def __init__(self, text: TypeRichText, email: str) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class TextEmpty(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class TextFixed(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    text: Incomplete
    def __init__(self, text: TypeRichText) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class TextImage(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    document_id: Incomplete
    w: Incomplete
    h: Incomplete
    def __init__(self, document_id: int, w: int, h: int) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class TextItalic(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    text: Incomplete
    def __init__(self, text: TypeRichText) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class TextMarked(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    text: Incomplete
    def __init__(self, text: TypeRichText) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class TextPhone(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    text: Incomplete
    phone: Incomplete
    def __init__(self, text: TypeRichText, phone: str) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class TextPlain(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    text: Incomplete
    def __init__(self, text: str) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class TextStrike(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    text: Incomplete
    def __init__(self, text: TypeRichText) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class TextSubscript(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    text: Incomplete
    def __init__(self, text: TypeRichText) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class TextSuperscript(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    text: Incomplete
    def __init__(self, text: TypeRichText) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class TextUnderline(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    text: Incomplete
    def __init__(self, text: TypeRichText) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class TextUrl(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    text: Incomplete
    url: Incomplete
    webpage_id: Incomplete
    def __init__(self, text: TypeRichText, url: str, webpage_id: int) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class TextWithEntities(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    text: Incomplete
    entities: Incomplete
    def __init__(self, text: str, entities: list['TypeMessageEntity']) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class Theme(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    id: Incomplete
    access_hash: Incomplete
    slug: Incomplete
    title: Incomplete
    creator: Incomplete
    default: Incomplete
    for_chat: Incomplete
    document: Incomplete
    settings: Incomplete
    emoticon: Incomplete
    installs_count: Incomplete
    def __init__(self, id: int, access_hash: int, slug: str, title: str, creator: bool | None = None, default: bool | None = None, for_chat: bool | None = None, document: TypeDocument | None = None, settings: list['TypeThemeSettings'] | None = None, emoticon: str | None = None, installs_count: int | None = None) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class ThemeSettings(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    base_theme: Incomplete
    accent_color: Incomplete
    message_colors_animated: Incomplete
    outbox_accent_color: Incomplete
    message_colors: Incomplete
    wallpaper: Incomplete
    def __init__(self, base_theme: TypeBaseTheme, accent_color: int, message_colors_animated: bool | None = None, outbox_accent_color: int | None = None, message_colors: list[int] | None = None, wallpaper: TypeWallPaper | None = None) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class Timezone(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    id: Incomplete
    name: Incomplete
    utc_offset: Incomplete
    def __init__(self, id: str, name: str, utc_offset: int) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class TlsBlockDomain(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class TlsBlockGrease(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    seed: Incomplete
    def __init__(self, seed: int) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class TlsBlockPublicKey(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class TlsBlockRandom(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    length: Incomplete
    def __init__(self, length: int) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class TlsBlockScope(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    entries: Incomplete
    def __init__(self, entries: list['TypeTlsBlock']) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class TlsBlockString(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    data: Incomplete
    def __init__(self, data: str) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class TlsBlockZero(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    length: Incomplete
    def __init__(self, length: int) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class TlsClientHello(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    blocks: Incomplete
    def __init__(self, blocks: list['TypeTlsBlock']) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class TopPeer(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    peer: Incomplete
    rating: Incomplete
    def __init__(self, peer: TypePeer, rating: float) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class TopPeerCategoryBotsApp(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class TopPeerCategoryBotsInline(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class TopPeerCategoryBotsPM(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class TopPeerCategoryChannels(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class TopPeerCategoryCorrespondents(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class TopPeerCategoryForwardChats(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class TopPeerCategoryForwardUsers(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class TopPeerCategoryGroups(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class TopPeerCategoryPeers(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    category: Incomplete
    count: Incomplete
    peers: Incomplete
    def __init__(self, category: TypeTopPeerCategory, count: int, peers: list['TypeTopPeer']) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class TopPeerCategoryPhoneCalls(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class UpdateAttachMenuBots(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class UpdateAutoSaveSettings(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class UpdateBotBusinessConnect(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    connection: Incomplete
    qts: Incomplete
    def __init__(self, connection: TypeBotBusinessConnection, qts: int) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class UpdateBotCallbackQuery(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    query_id: Incomplete
    user_id: Incomplete
    peer: Incomplete
    msg_id: Incomplete
    chat_instance: Incomplete
    data: Incomplete
    game_short_name: Incomplete
    def __init__(self, query_id: int, user_id: int, peer: TypePeer, msg_id: int, chat_instance: int, data: bytes | None = None, game_short_name: str | None = None) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class UpdateBotChatBoost(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    peer: Incomplete
    boost: Incomplete
    qts: Incomplete
    def __init__(self, peer: TypePeer, boost: TypeBoost, qts: int) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class UpdateBotChatInviteRequester(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    peer: Incomplete
    date: Incomplete
    user_id: Incomplete
    about: Incomplete
    invite: Incomplete
    qts: Incomplete
    def __init__(self, peer: TypePeer, date: datetime | None, user_id: int, about: str, invite: TypeExportedChatInvite, qts: int) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class UpdateBotCommands(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    peer: Incomplete
    bot_id: Incomplete
    commands: Incomplete
    def __init__(self, peer: TypePeer, bot_id: int, commands: list['TypeBotCommand']) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class UpdateBotDeleteBusinessMessage(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    connection_id: Incomplete
    peer: Incomplete
    messages: Incomplete
    qts: Incomplete
    def __init__(self, connection_id: str, peer: TypePeer, messages: list[int], qts: int) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class UpdateBotEditBusinessMessage(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    connection_id: Incomplete
    message: Incomplete
    qts: Incomplete
    reply_to_message: Incomplete
    def __init__(self, connection_id: str, message: TypeMessage, qts: int, reply_to_message: TypeMessage | None = None) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class UpdateBotInlineQuery(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    query_id: Incomplete
    user_id: Incomplete
    query: Incomplete
    offset: Incomplete
    geo: Incomplete
    peer_type: Incomplete
    def __init__(self, query_id: int, user_id: int, query: str, offset: str, geo: TypeGeoPoint | None = None, peer_type: TypeInlineQueryPeerType | None = None) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class UpdateBotInlineSend(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    user_id: Incomplete
    query: Incomplete
    id: Incomplete
    geo: Incomplete
    msg_id: Incomplete
    def __init__(self, user_id: int, query: str, id: str, geo: TypeGeoPoint | None = None, msg_id: TypeInputBotInlineMessageID | None = None) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class UpdateBotMenuButton(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    bot_id: Incomplete
    button: Incomplete
    def __init__(self, bot_id: int, button: TypeBotMenuButton) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class UpdateBotMessageReaction(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    peer: Incomplete
    msg_id: Incomplete
    date: Incomplete
    actor: Incomplete
    old_reactions: Incomplete
    new_reactions: Incomplete
    qts: Incomplete
    def __init__(self, peer: TypePeer, msg_id: int, date: datetime | None, actor: TypePeer, old_reactions: list['TypeReaction'], new_reactions: list['TypeReaction'], qts: int) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class UpdateBotMessageReactions(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    peer: Incomplete
    msg_id: Incomplete
    date: Incomplete
    reactions: Incomplete
    qts: Incomplete
    def __init__(self, peer: TypePeer, msg_id: int, date: datetime | None, reactions: list['TypeReactionCount'], qts: int) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class UpdateBotNewBusinessMessage(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    connection_id: Incomplete
    message: Incomplete
    qts: Incomplete
    reply_to_message: Incomplete
    def __init__(self, connection_id: str, message: TypeMessage, qts: int, reply_to_message: TypeMessage | None = None) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class UpdateBotPrecheckoutQuery(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    query_id: Incomplete
    user_id: Incomplete
    payload: Incomplete
    currency: Incomplete
    total_amount: Incomplete
    info: Incomplete
    shipping_option_id: Incomplete
    def __init__(self, query_id: int, user_id: int, payload: bytes, currency: str, total_amount: int, info: TypePaymentRequestedInfo | None = None, shipping_option_id: str | None = None) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class UpdateBotPurchasedPaidMedia(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    user_id: Incomplete
    payload: Incomplete
    qts: Incomplete
    def __init__(self, user_id: int, payload: str, qts: int) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class UpdateBotShippingQuery(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    query_id: Incomplete
    user_id: Incomplete
    payload: Incomplete
    shipping_address: Incomplete
    def __init__(self, query_id: int, user_id: int, payload: bytes, shipping_address: TypePostAddress) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class UpdateBotStopped(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    user_id: Incomplete
    date: Incomplete
    stopped: Incomplete
    qts: Incomplete
    def __init__(self, user_id: int, date: datetime | None, stopped: bool, qts: int) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class UpdateBotSubscriptionExpire(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    user_id: Incomplete
    payload: Incomplete
    invoice_slug: Incomplete
    until_date: Incomplete
    qts: Incomplete
    def __init__(self, user_id: int, payload: str, invoice_slug: str, until_date: datetime | None, qts: int) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class UpdateBotWebhookJSON(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    data: Incomplete
    def __init__(self, data: TypeDataJSON) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class UpdateBotWebhookJSONQuery(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    query_id: Incomplete
    data: Incomplete
    timeout: Incomplete
    def __init__(self, query_id: int, data: TypeDataJSON, timeout: int) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class UpdateBroadcastRevenueTransactions(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    peer: Incomplete
    balances: Incomplete
    def __init__(self, peer: TypePeer, balances: TypeBroadcastRevenueBalances) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class UpdateBusinessBotCallbackQuery(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    query_id: Incomplete
    user_id: Incomplete
    connection_id: Incomplete
    message: Incomplete
    chat_instance: Incomplete
    reply_to_message: Incomplete
    data: Incomplete
    def __init__(self, query_id: int, user_id: int, connection_id: str, message: TypeMessage, chat_instance: int, reply_to_message: TypeMessage | None = None, data: bytes | None = None) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class UpdateChannel(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    channel_id: Incomplete
    def __init__(self, channel_id: int) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class UpdateChannelAvailableMessages(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    channel_id: Incomplete
    available_min_id: Incomplete
    def __init__(self, channel_id: int, available_min_id: int) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class UpdateChannelMessageForwards(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    channel_id: Incomplete
    id: Incomplete
    forwards: Incomplete
    def __init__(self, channel_id: int, id: int, forwards: int) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class UpdateChannelMessageViews(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    channel_id: Incomplete
    id: Incomplete
    views: Incomplete
    def __init__(self, channel_id: int, id: int, views: int) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class UpdateChannelParticipant(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    channel_id: Incomplete
    date: Incomplete
    actor_id: Incomplete
    user_id: Incomplete
    qts: Incomplete
    via_chatlist: Incomplete
    prev_participant: Incomplete
    new_participant: Incomplete
    invite: Incomplete
    def __init__(self, channel_id: int, date: datetime | None, actor_id: int, user_id: int, qts: int, via_chatlist: bool | None = None, prev_participant: TypeChannelParticipant | None = None, new_participant: TypeChannelParticipant | None = None, invite: TypeExportedChatInvite | None = None) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class UpdateChannelPinnedTopic(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    channel_id: Incomplete
    topic_id: Incomplete
    pinned: Incomplete
    def __init__(self, channel_id: int, topic_id: int, pinned: bool | None = None) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class UpdateChannelPinnedTopics(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    channel_id: Incomplete
    order: Incomplete
    def __init__(self, channel_id: int, order: list[int] | None = None) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class UpdateChannelReadMessagesContents(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    channel_id: Incomplete
    messages: Incomplete
    top_msg_id: Incomplete
    def __init__(self, channel_id: int, messages: list[int], top_msg_id: int | None = None) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class UpdateChannelTooLong(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    channel_id: Incomplete
    pts: Incomplete
    def __init__(self, channel_id: int, pts: int | None = None) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class UpdateChannelUserTyping(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    channel_id: Incomplete
    from_id: Incomplete
    action: Incomplete
    top_msg_id: Incomplete
    def __init__(self, channel_id: int, from_id: TypePeer, action: TypeSendMessageAction, top_msg_id: int | None = None) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class UpdateChannelViewForumAsMessages(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    channel_id: Incomplete
    enabled: Incomplete
    def __init__(self, channel_id: int, enabled: bool) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class UpdateChannelWebPage(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    channel_id: Incomplete
    webpage: Incomplete
    pts: Incomplete
    pts_count: Incomplete
    def __init__(self, channel_id: int, webpage: TypeWebPage, pts: int, pts_count: int) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class UpdateChat(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    chat_id: Incomplete
    def __init__(self, chat_id: int) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class UpdateChatDefaultBannedRights(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    peer: Incomplete
    default_banned_rights: Incomplete
    version: Incomplete
    def __init__(self, peer: TypePeer, default_banned_rights: TypeChatBannedRights, version: int) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class UpdateChatParticipant(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    chat_id: Incomplete
    date: Incomplete
    actor_id: Incomplete
    user_id: Incomplete
    qts: Incomplete
    prev_participant: Incomplete
    new_participant: Incomplete
    invite: Incomplete
    def __init__(self, chat_id: int, date: datetime | None, actor_id: int, user_id: int, qts: int, prev_participant: TypeChatParticipant | None = None, new_participant: TypeChatParticipant | None = None, invite: TypeExportedChatInvite | None = None) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class UpdateChatParticipantAdd(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    chat_id: Incomplete
    user_id: Incomplete
    inviter_id: Incomplete
    date: Incomplete
    version: Incomplete
    def __init__(self, chat_id: int, user_id: int, inviter_id: int, date: datetime | None, version: int) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class UpdateChatParticipantAdmin(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    chat_id: Incomplete
    user_id: Incomplete
    is_admin: Incomplete
    version: Incomplete
    def __init__(self, chat_id: int, user_id: int, is_admin: bool, version: int) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class UpdateChatParticipantDelete(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    chat_id: Incomplete
    user_id: Incomplete
    version: Incomplete
    def __init__(self, chat_id: int, user_id: int, version: int) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class UpdateChatParticipants(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    participants: Incomplete
    def __init__(self, participants: TypeChatParticipants) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class UpdateChatUserTyping(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    chat_id: Incomplete
    from_id: Incomplete
    action: Incomplete
    def __init__(self, chat_id: int, from_id: TypePeer, action: TypeSendMessageAction) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class UpdateConfig(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class UpdateContactsReset(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class UpdateDcOptions(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    dc_options: Incomplete
    def __init__(self, dc_options: list['TypeDcOption']) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class UpdateDeleteChannelMessages(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    channel_id: Incomplete
    messages: Incomplete
    pts: Incomplete
    pts_count: Incomplete
    def __init__(self, channel_id: int, messages: list[int], pts: int, pts_count: int) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class UpdateDeleteMessages(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    messages: Incomplete
    pts: Incomplete
    pts_count: Incomplete
    def __init__(self, messages: list[int], pts: int, pts_count: int) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class UpdateDeleteQuickReply(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    shortcut_id: Incomplete
    def __init__(self, shortcut_id: int) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class UpdateDeleteQuickReplyMessages(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    shortcut_id: Incomplete
    messages: Incomplete
    def __init__(self, shortcut_id: int, messages: list[int]) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class UpdateDeleteScheduledMessages(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    peer: Incomplete
    messages: Incomplete
    sent_messages: Incomplete
    def __init__(self, peer: TypePeer, messages: list[int], sent_messages: list[int] | None = None) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class UpdateDialogFilter(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    id: Incomplete
    filter: Incomplete
    def __init__(self, id: int, filter: TypeDialogFilter | None = None) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class UpdateDialogFilterOrder(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    order: Incomplete
    def __init__(self, order: list[int]) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class UpdateDialogFilters(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class UpdateDialogPinned(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    peer: Incomplete
    pinned: Incomplete
    folder_id: Incomplete
    def __init__(self, peer: TypeDialogPeer, pinned: bool | None = None, folder_id: int | None = None) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class UpdateDialogUnreadMark(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    peer: Incomplete
    unread: Incomplete
    def __init__(self, peer: TypeDialogPeer, unread: bool | None = None) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class UpdateDraftMessage(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    peer: Incomplete
    draft: Incomplete
    top_msg_id: Incomplete
    def __init__(self, peer: TypePeer, draft: TypeDraftMessage, top_msg_id: int | None = None) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class UpdateEditChannelMessage(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    message: Incomplete
    pts: Incomplete
    pts_count: Incomplete
    def __init__(self, message: TypeMessage, pts: int, pts_count: int) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class UpdateEditMessage(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    message: Incomplete
    pts: Incomplete
    pts_count: Incomplete
    def __init__(self, message: TypeMessage, pts: int, pts_count: int) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class UpdateEncryptedChatTyping(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    chat_id: Incomplete
    def __init__(self, chat_id: int) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class UpdateEncryptedMessagesRead(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    chat_id: Incomplete
    max_date: Incomplete
    date: Incomplete
    def __init__(self, chat_id: int, max_date: datetime | None, date: datetime | None) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class UpdateEncryption(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    chat: Incomplete
    date: Incomplete
    def __init__(self, chat: TypeEncryptedChat, date: datetime | None) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class UpdateFavedStickers(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class UpdateFolderPeers(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    folder_peers: Incomplete
    pts: Incomplete
    pts_count: Incomplete
    def __init__(self, folder_peers: list['TypeFolderPeer'], pts: int, pts_count: int) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class UpdateGeoLiveViewed(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    peer: Incomplete
    msg_id: Incomplete
    def __init__(self, peer: TypePeer, msg_id: int) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class UpdateGroupCall(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    chat_id: Incomplete
    call: Incomplete
    def __init__(self, chat_id: int, call: TypeGroupCall) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class UpdateGroupCallConnection(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    params: Incomplete
    presentation: Incomplete
    def __init__(self, params: TypeDataJSON, presentation: bool | None = None) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class UpdateGroupCallParticipants(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    call: Incomplete
    participants: Incomplete
    version: Incomplete
    def __init__(self, call: TypeInputGroupCall, participants: list['TypeGroupCallParticipant'], version: int) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class UpdateInlineBotCallbackQuery(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    query_id: Incomplete
    user_id: Incomplete
    msg_id: Incomplete
    chat_instance: Incomplete
    data: Incomplete
    game_short_name: Incomplete
    def __init__(self, query_id: int, user_id: int, msg_id: TypeInputBotInlineMessageID, chat_instance: int, data: bytes | None = None, game_short_name: str | None = None) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class UpdateLangPack(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    difference: Incomplete
    def __init__(self, difference: TypeLangPackDifference) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class UpdateLangPackTooLong(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    lang_code: Incomplete
    def __init__(self, lang_code: str) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class UpdateLoginToken(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class UpdateMessageExtendedMedia(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    peer: Incomplete
    msg_id: Incomplete
    extended_media: Incomplete
    def __init__(self, peer: TypePeer, msg_id: int, extended_media: list['TypeMessageExtendedMedia']) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class UpdateMessageID(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    id: Incomplete
    random_id: Incomplete
    def __init__(self, id: int, random_id: int = None) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class UpdateMessagePoll(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    poll_id: Incomplete
    results: Incomplete
    poll: Incomplete
    def __init__(self, poll_id: int, results: TypePollResults, poll: TypePoll | None = None) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class UpdateMessagePollVote(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    poll_id: Incomplete
    peer: Incomplete
    options: Incomplete
    qts: Incomplete
    def __init__(self, poll_id: int, peer: TypePeer, options: list[bytes], qts: int) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class UpdateMessageReactions(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    peer: Incomplete
    msg_id: Incomplete
    reactions: Incomplete
    top_msg_id: Incomplete
    def __init__(self, peer: TypePeer, msg_id: int, reactions: TypeMessageReactions, top_msg_id: int | None = None) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class UpdateMoveStickerSetToTop(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    stickerset: Incomplete
    masks: Incomplete
    emojis: Incomplete
    def __init__(self, stickerset: int, masks: bool | None = None, emojis: bool | None = None) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class UpdateNewAuthorization(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    hash: Incomplete
    unconfirmed: Incomplete
    date: Incomplete
    device: Incomplete
    location: Incomplete
    def __init__(self, hash: int, unconfirmed: bool | None = None, date: datetime | None = None, device: str | None = None, location: str | None = None) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class UpdateNewChannelMessage(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    message: Incomplete
    pts: Incomplete
    pts_count: Incomplete
    def __init__(self, message: TypeMessage, pts: int, pts_count: int) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class UpdateNewEncryptedMessage(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    message: Incomplete
    qts: Incomplete
    def __init__(self, message: TypeEncryptedMessage, qts: int) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class UpdateNewMessage(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    message: Incomplete
    pts: Incomplete
    pts_count: Incomplete
    def __init__(self, message: TypeMessage, pts: int, pts_count: int) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class UpdateNewQuickReply(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    quick_reply: Incomplete
    def __init__(self, quick_reply: TypeQuickReply) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class UpdateNewScheduledMessage(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    message: Incomplete
    def __init__(self, message: TypeMessage) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class UpdateNewStickerSet(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    stickerset: Incomplete
    def __init__(self, stickerset: TypeStickerSet) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class UpdateNewStoryReaction(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    story_id: Incomplete
    peer: Incomplete
    reaction: Incomplete
    def __init__(self, story_id: int, peer: TypePeer, reaction: TypeReaction) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class UpdateNotifySettings(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    peer: Incomplete
    notify_settings: Incomplete
    def __init__(self, peer: TypeNotifyPeer, notify_settings: TypePeerNotifySettings) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class UpdatePaidReactionPrivacy(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    private: Incomplete
    def __init__(self, private: bool) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class UpdatePeerBlocked(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    peer_id: Incomplete
    blocked: Incomplete
    blocked_my_stories_from: Incomplete
    def __init__(self, peer_id: TypePeer, blocked: bool | None = None, blocked_my_stories_from: bool | None = None) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class UpdatePeerHistoryTTL(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    peer: Incomplete
    ttl_period: Incomplete
    def __init__(self, peer: TypePeer, ttl_period: int | None = None) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class UpdatePeerLocated(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    peers: Incomplete
    def __init__(self, peers: list['TypePeerLocated']) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class UpdatePeerSettings(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    peer: Incomplete
    settings: Incomplete
    def __init__(self, peer: TypePeer, settings: TypePeerSettings) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class UpdatePeerWallpaper(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    peer: Incomplete
    wallpaper_overridden: Incomplete
    wallpaper: Incomplete
    def __init__(self, peer: TypePeer, wallpaper_overridden: bool | None = None, wallpaper: TypeWallPaper | None = None) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class UpdatePendingJoinRequests(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    peer: Incomplete
    requests_pending: Incomplete
    recent_requesters: Incomplete
    def __init__(self, peer: TypePeer, requests_pending: int, recent_requesters: list[int]) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class UpdatePhoneCall(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    phone_call: Incomplete
    def __init__(self, phone_call: TypePhoneCall) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class UpdatePhoneCallSignalingData(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    phone_call_id: Incomplete
    data: Incomplete
    def __init__(self, phone_call_id: int, data: bytes) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class UpdatePinnedChannelMessages(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    channel_id: Incomplete
    messages: Incomplete
    pts: Incomplete
    pts_count: Incomplete
    pinned: Incomplete
    def __init__(self, channel_id: int, messages: list[int], pts: int, pts_count: int, pinned: bool | None = None) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class UpdatePinnedDialogs(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    folder_id: Incomplete
    order: Incomplete
    def __init__(self, folder_id: int | None = None, order: list['TypeDialogPeer'] | None = None) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class UpdatePinnedMessages(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    peer: Incomplete
    messages: Incomplete
    pts: Incomplete
    pts_count: Incomplete
    pinned: Incomplete
    def __init__(self, peer: TypePeer, messages: list[int], pts: int, pts_count: int, pinned: bool | None = None) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class UpdatePinnedSavedDialogs(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    order: Incomplete
    def __init__(self, order: list['TypeDialogPeer'] | None = None) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class UpdatePrivacy(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    key: Incomplete
    rules: Incomplete
    def __init__(self, key: TypePrivacyKey, rules: list['TypePrivacyRule']) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class UpdatePtsChanged(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class UpdateQuickReplies(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    quick_replies: Incomplete
    def __init__(self, quick_replies: list['TypeQuickReply']) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class UpdateQuickReplyMessage(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    message: Incomplete
    def __init__(self, message: TypeMessage) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class UpdateReadChannelDiscussionInbox(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    channel_id: Incomplete
    top_msg_id: Incomplete
    read_max_id: Incomplete
    broadcast_id: Incomplete
    broadcast_post: Incomplete
    def __init__(self, channel_id: int, top_msg_id: int, read_max_id: int, broadcast_id: int | None = None, broadcast_post: int | None = None) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class UpdateReadChannelDiscussionOutbox(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    channel_id: Incomplete
    top_msg_id: Incomplete
    read_max_id: Incomplete
    def __init__(self, channel_id: int, top_msg_id: int, read_max_id: int) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class UpdateReadChannelInbox(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    channel_id: Incomplete
    max_id: Incomplete
    still_unread_count: Incomplete
    pts: Incomplete
    folder_id: Incomplete
    def __init__(self, channel_id: int, max_id: int, still_unread_count: int, pts: int, folder_id: int | None = None) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class UpdateReadChannelOutbox(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    channel_id: Incomplete
    max_id: Incomplete
    def __init__(self, channel_id: int, max_id: int) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class UpdateReadFeaturedEmojiStickers(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class UpdateReadFeaturedStickers(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class UpdateReadHistoryInbox(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    peer: Incomplete
    max_id: Incomplete
    still_unread_count: Incomplete
    pts: Incomplete
    pts_count: Incomplete
    folder_id: Incomplete
    def __init__(self, peer: TypePeer, max_id: int, still_unread_count: int, pts: int, pts_count: int, folder_id: int | None = None) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class UpdateReadHistoryOutbox(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    peer: Incomplete
    max_id: Incomplete
    pts: Incomplete
    pts_count: Incomplete
    def __init__(self, peer: TypePeer, max_id: int, pts: int, pts_count: int) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class UpdateReadMessagesContents(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    messages: Incomplete
    pts: Incomplete
    pts_count: Incomplete
    date: Incomplete
    def __init__(self, messages: list[int], pts: int, pts_count: int, date: datetime | None = None) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class UpdateReadStories(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    peer: Incomplete
    max_id: Incomplete
    def __init__(self, peer: TypePeer, max_id: int) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class UpdateRecentEmojiStatuses(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class UpdateRecentReactions(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class UpdateRecentStickers(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class UpdateSavedDialogPinned(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    peer: Incomplete
    pinned: Incomplete
    def __init__(self, peer: TypeDialogPeer, pinned: bool | None = None) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class UpdateSavedGifs(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class UpdateSavedReactionTags(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class UpdateSavedRingtones(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class UpdateSentStoryReaction(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    peer: Incomplete
    story_id: Incomplete
    reaction: Incomplete
    def __init__(self, peer: TypePeer, story_id: int, reaction: TypeReaction) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class UpdateServiceNotification(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    type: Incomplete
    message: Incomplete
    media: Incomplete
    entities: Incomplete
    popup: Incomplete
    invert_media: Incomplete
    inbox_date: Incomplete
    def __init__(self, type: str, message: str, media: TypeMessageMedia, entities: list['TypeMessageEntity'], popup: bool | None = None, invert_media: bool | None = None, inbox_date: datetime | None = None) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class UpdateShort(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    update: Incomplete
    date: Incomplete
    def __init__(self, update: TypeUpdate, date: datetime | None) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class UpdateShortChatMessage(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    id: Incomplete
    from_id: Incomplete
    chat_id: Incomplete
    message: Incomplete
    pts: Incomplete
    pts_count: Incomplete
    date: Incomplete
    out: Incomplete
    mentioned: Incomplete
    media_unread: Incomplete
    silent: Incomplete
    fwd_from: Incomplete
    via_bot_id: Incomplete
    reply_to: Incomplete
    entities: Incomplete
    ttl_period: Incomplete
    def __init__(self, id: int, from_id: int, chat_id: int, message: str, pts: int, pts_count: int, date: datetime | None, out: bool | None = None, mentioned: bool | None = None, media_unread: bool | None = None, silent: bool | None = None, fwd_from: TypeMessageFwdHeader | None = None, via_bot_id: int | None = None, reply_to: TypeMessageReplyHeader | None = None, entities: list['TypeMessageEntity'] | None = None, ttl_period: int | None = None) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class UpdateShortMessage(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    id: Incomplete
    user_id: Incomplete
    message: Incomplete
    pts: Incomplete
    pts_count: Incomplete
    date: Incomplete
    out: Incomplete
    mentioned: Incomplete
    media_unread: Incomplete
    silent: Incomplete
    fwd_from: Incomplete
    via_bot_id: Incomplete
    reply_to: Incomplete
    entities: Incomplete
    ttl_period: Incomplete
    def __init__(self, id: int, user_id: int, message: str, pts: int, pts_count: int, date: datetime | None, out: bool | None = None, mentioned: bool | None = None, media_unread: bool | None = None, silent: bool | None = None, fwd_from: TypeMessageFwdHeader | None = None, via_bot_id: int | None = None, reply_to: TypeMessageReplyHeader | None = None, entities: list['TypeMessageEntity'] | None = None, ttl_period: int | None = None) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class UpdateShortSentMessage(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    id: Incomplete
    pts: Incomplete
    pts_count: Incomplete
    date: Incomplete
    out: Incomplete
    media: Incomplete
    entities: Incomplete
    ttl_period: Incomplete
    def __init__(self, id: int, pts: int, pts_count: int, date: datetime | None, out: bool | None = None, media: TypeMessageMedia | None = None, entities: list['TypeMessageEntity'] | None = None, ttl_period: int | None = None) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class UpdateSmsJob(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    job_id: Incomplete
    def __init__(self, job_id: str) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class UpdateStarsBalance(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    balance: Incomplete
    def __init__(self, balance: int) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class UpdateStarsRevenueStatus(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    peer: Incomplete
    status: Incomplete
    def __init__(self, peer: TypePeer, status: TypeStarsRevenueStatus) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class UpdateStickerSets(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    masks: Incomplete
    emojis: Incomplete
    def __init__(self, masks: bool | None = None, emojis: bool | None = None) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class UpdateStickerSetsOrder(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    order: Incomplete
    masks: Incomplete
    emojis: Incomplete
    def __init__(self, order: list[int], masks: bool | None = None, emojis: bool | None = None) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class UpdateStoriesStealthMode(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    stealth_mode: Incomplete
    def __init__(self, stealth_mode: TypeStoriesStealthMode) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class UpdateStory(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    peer: Incomplete
    story: Incomplete
    def __init__(self, peer: TypePeer, story: TypeStoryItem) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class UpdateStoryID(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    id: Incomplete
    random_id: Incomplete
    def __init__(self, id: int, random_id: int = None) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class UpdateTheme(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    theme: Incomplete
    def __init__(self, theme: TypeTheme) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class UpdateTranscribedAudio(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    peer: Incomplete
    msg_id: Incomplete
    transcription_id: Incomplete
    text: Incomplete
    pending: Incomplete
    def __init__(self, peer: TypePeer, msg_id: int, transcription_id: int, text: str, pending: bool | None = None) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class UpdateUser(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    user_id: Incomplete
    def __init__(self, user_id: int) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class UpdateUserEmojiStatus(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    user_id: Incomplete
    emoji_status: Incomplete
    def __init__(self, user_id: int, emoji_status: TypeEmojiStatus) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class UpdateUserName(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    user_id: Incomplete
    first_name: Incomplete
    last_name: Incomplete
    usernames: Incomplete
    def __init__(self, user_id: int, first_name: str, last_name: str, usernames: list['TypeUsername']) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class UpdateUserPhone(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    user_id: Incomplete
    phone: Incomplete
    def __init__(self, user_id: int, phone: str) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class UpdateUserStatus(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    user_id: Incomplete
    status: Incomplete
    def __init__(self, user_id: int, status: TypeUserStatus) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class UpdateUserTyping(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    user_id: Incomplete
    action: Incomplete
    def __init__(self, user_id: int, action: TypeSendMessageAction) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class UpdateWebPage(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    webpage: Incomplete
    pts: Incomplete
    pts_count: Incomplete
    def __init__(self, webpage: TypeWebPage, pts: int, pts_count: int) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class UpdateWebViewResultSent(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    query_id: Incomplete
    def __init__(self, query_id: int) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class Updates(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    updates: Incomplete
    users: Incomplete
    chats: Incomplete
    date: Incomplete
    seq: Incomplete
    def __init__(self, updates: list['TypeUpdate'], users: list['TypeUser'], chats: list['TypeChat'], date: datetime | None, seq: int) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class UpdatesCombined(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    updates: Incomplete
    users: Incomplete
    chats: Incomplete
    date: Incomplete
    seq_start: Incomplete
    seq: Incomplete
    def __init__(self, updates: list['TypeUpdate'], users: list['TypeUser'], chats: list['TypeChat'], date: datetime | None, seq_start: int, seq: int) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class UpdatesTooLong(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class UrlAuthResultAccepted(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    url: Incomplete
    def __init__(self, url: str) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class UrlAuthResultDefault(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class UrlAuthResultRequest(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    bot: Incomplete
    domain: Incomplete
    request_write_access: Incomplete
    def __init__(self, bot: TypeUser, domain: str, request_write_access: bool | None = None) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class User(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    id: Incomplete
    is_self: Incomplete
    contact: Incomplete
    mutual_contact: Incomplete
    deleted: Incomplete
    bot: Incomplete
    bot_chat_history: Incomplete
    bot_nochats: Incomplete
    verified: Incomplete
    restricted: Incomplete
    min: Incomplete
    bot_inline_geo: Incomplete
    support: Incomplete
    scam: Incomplete
    apply_min_photo: Incomplete
    fake: Incomplete
    bot_attach_menu: Incomplete
    premium: Incomplete
    attach_menu_enabled: Incomplete
    bot_can_edit: Incomplete
    close_friend: Incomplete
    stories_hidden: Incomplete
    stories_unavailable: Incomplete
    contact_require_premium: Incomplete
    bot_business: Incomplete
    bot_has_main_app: Incomplete
    access_hash: Incomplete
    first_name: Incomplete
    last_name: Incomplete
    username: Incomplete
    phone: Incomplete
    photo: Incomplete
    status: Incomplete
    bot_info_version: Incomplete
    restriction_reason: Incomplete
    bot_inline_placeholder: Incomplete
    lang_code: Incomplete
    emoji_status: Incomplete
    usernames: Incomplete
    stories_max_id: Incomplete
    color: Incomplete
    profile_color: Incomplete
    bot_active_users: Incomplete
    def __init__(self, id: int, is_self: bool | None = None, contact: bool | None = None, mutual_contact: bool | None = None, deleted: bool | None = None, bot: bool | None = None, bot_chat_history: bool | None = None, bot_nochats: bool | None = None, verified: bool | None = None, restricted: bool | None = None, min: bool | None = None, bot_inline_geo: bool | None = None, support: bool | None = None, scam: bool | None = None, apply_min_photo: bool | None = None, fake: bool | None = None, bot_attach_menu: bool | None = None, premium: bool | None = None, attach_menu_enabled: bool | None = None, bot_can_edit: bool | None = None, close_friend: bool | None = None, stories_hidden: bool | None = None, stories_unavailable: bool | None = None, contact_require_premium: bool | None = None, bot_business: bool | None = None, bot_has_main_app: bool | None = None, access_hash: int | None = None, first_name: str | None = None, last_name: str | None = None, username: str | None = None, phone: str | None = None, photo: TypeUserProfilePhoto | None = None, status: TypeUserStatus | None = None, bot_info_version: int | None = None, restriction_reason: list['TypeRestrictionReason'] | None = None, bot_inline_placeholder: str | None = None, lang_code: str | None = None, emoji_status: TypeEmojiStatus | None = None, usernames: list['TypeUsername'] | None = None, stories_max_id: int | None = None, color: TypePeerColor | None = None, profile_color: TypePeerColor | None = None, bot_active_users: int | None = None) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class UserEmpty(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    id: Incomplete
    def __init__(self, id: int) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class UserFull(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    id: Incomplete
    settings: Incomplete
    notify_settings: Incomplete
    common_chats_count: Incomplete
    blocked: Incomplete
    phone_calls_available: Incomplete
    phone_calls_private: Incomplete
    can_pin_message: Incomplete
    has_scheduled: Incomplete
    video_calls_available: Incomplete
    voice_messages_forbidden: Incomplete
    translations_disabled: Incomplete
    stories_pinned_available: Incomplete
    blocked_my_stories_from: Incomplete
    wallpaper_overridden: Incomplete
    contact_require_premium: Incomplete
    read_dates_private: Incomplete
    sponsored_enabled: Incomplete
    can_view_revenue: Incomplete
    bot_can_manage_emoji_status: Incomplete
    about: Incomplete
    personal_photo: Incomplete
    profile_photo: Incomplete
    fallback_photo: Incomplete
    bot_info: Incomplete
    pinned_msg_id: Incomplete
    folder_id: Incomplete
    ttl_period: Incomplete
    theme_emoticon: Incomplete
    private_forward_name: Incomplete
    bot_group_admin_rights: Incomplete
    bot_broadcast_admin_rights: Incomplete
    premium_gifts: Incomplete
    wallpaper: Incomplete
    stories: Incomplete
    business_work_hours: Incomplete
    business_location: Incomplete
    business_greeting_message: Incomplete
    business_away_message: Incomplete
    business_intro: Incomplete
    birthday: Incomplete
    personal_channel_id: Incomplete
    personal_channel_message: Incomplete
    stargifts_count: Incomplete
    def __init__(self, id: int, settings: TypePeerSettings, notify_settings: TypePeerNotifySettings, common_chats_count: int, blocked: bool | None = None, phone_calls_available: bool | None = None, phone_calls_private: bool | None = None, can_pin_message: bool | None = None, has_scheduled: bool | None = None, video_calls_available: bool | None = None, voice_messages_forbidden: bool | None = None, translations_disabled: bool | None = None, stories_pinned_available: bool | None = None, blocked_my_stories_from: bool | None = None, wallpaper_overridden: bool | None = None, contact_require_premium: bool | None = None, read_dates_private: bool | None = None, sponsored_enabled: bool | None = None, can_view_revenue: bool | None = None, bot_can_manage_emoji_status: bool | None = None, about: str | None = None, personal_photo: TypePhoto | None = None, profile_photo: TypePhoto | None = None, fallback_photo: TypePhoto | None = None, bot_info: TypeBotInfo | None = None, pinned_msg_id: int | None = None, folder_id: int | None = None, ttl_period: int | None = None, theme_emoticon: str | None = None, private_forward_name: str | None = None, bot_group_admin_rights: TypeChatAdminRights | None = None, bot_broadcast_admin_rights: TypeChatAdminRights | None = None, premium_gifts: list['TypePremiumGiftOption'] | None = None, wallpaper: TypeWallPaper | None = None, stories: TypePeerStories | None = None, business_work_hours: TypeBusinessWorkHours | None = None, business_location: TypeBusinessLocation | None = None, business_greeting_message: TypeBusinessGreetingMessage | None = None, business_away_message: TypeBusinessAwayMessage | None = None, business_intro: TypeBusinessIntro | None = None, birthday: TypeBirthday | None = None, personal_channel_id: int | None = None, personal_channel_message: int | None = None, stargifts_count: int | None = None) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class UserProfilePhoto(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    photo_id: Incomplete
    dc_id: Incomplete
    has_video: Incomplete
    personal: Incomplete
    stripped_thumb: Incomplete
    def __init__(self, photo_id: int, dc_id: int, has_video: bool | None = None, personal: bool | None = None, stripped_thumb: bytes | None = None) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class UserProfilePhotoEmpty(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class UserStarGift(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    date: Incomplete
    gift: Incomplete
    name_hidden: Incomplete
    unsaved: Incomplete
    from_id: Incomplete
    message: Incomplete
    msg_id: Incomplete
    convert_stars: Incomplete
    def __init__(self, date: datetime | None, gift: TypeStarGift, name_hidden: bool | None = None, unsaved: bool | None = None, from_id: int | None = None, message: TypeTextWithEntities | None = None, msg_id: int | None = None, convert_stars: int | None = None) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class UserStatusEmpty(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class UserStatusLastMonth(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    by_me: Incomplete
    def __init__(self, by_me: bool | None = None) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class UserStatusLastWeek(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    by_me: Incomplete
    def __init__(self, by_me: bool | None = None) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class UserStatusOffline(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    was_online: Incomplete
    def __init__(self, was_online: datetime | None) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class UserStatusOnline(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    expires: Incomplete
    def __init__(self, expires: datetime | None) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class UserStatusRecently(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    by_me: Incomplete
    def __init__(self, by_me: bool | None = None) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class Username(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    username: Incomplete
    editable: Incomplete
    active: Incomplete
    def __init__(self, username: str, editable: bool | None = None, active: bool | None = None) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class VideoSize(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    type: Incomplete
    w: Incomplete
    h: Incomplete
    size: Incomplete
    video_start_ts: Incomplete
    def __init__(self, type: str, w: int, h: int, size: int, video_start_ts: float | None = None) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class VideoSizeEmojiMarkup(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    emoji_id: Incomplete
    background_colors: Incomplete
    def __init__(self, emoji_id: int, background_colors: list[int]) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class VideoSizeStickerMarkup(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    stickerset: Incomplete
    sticker_id: Incomplete
    background_colors: Incomplete
    def __init__(self, stickerset: TypeInputStickerSet, sticker_id: int, background_colors: list[int]) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class WallPaper(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    id: Incomplete
    access_hash: Incomplete
    slug: Incomplete
    document: Incomplete
    creator: Incomplete
    default: Incomplete
    pattern: Incomplete
    dark: Incomplete
    settings: Incomplete
    def __init__(self, id: int, access_hash: int, slug: str, document: TypeDocument, creator: bool | None = None, default: bool | None = None, pattern: bool | None = None, dark: bool | None = None, settings: TypeWallPaperSettings | None = None) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class WallPaperNoFile(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    id: Incomplete
    default: Incomplete
    dark: Incomplete
    settings: Incomplete
    def __init__(self, id: int, default: bool | None = None, dark: bool | None = None, settings: TypeWallPaperSettings | None = None) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class WallPaperSettings(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    blur: Incomplete
    motion: Incomplete
    background_color: Incomplete
    second_background_color: Incomplete
    third_background_color: Incomplete
    fourth_background_color: Incomplete
    intensity: Incomplete
    rotation: Incomplete
    emoticon: Incomplete
    def __init__(self, blur: bool | None = None, motion: bool | None = None, background_color: int | None = None, second_background_color: int | None = None, third_background_color: int | None = None, fourth_background_color: int | None = None, intensity: int | None = None, rotation: int | None = None, emoticon: str | None = None) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class WebAuthorization(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    hash: Incomplete
    bot_id: Incomplete
    domain: Incomplete
    browser: Incomplete
    platform: Incomplete
    date_created: Incomplete
    date_active: Incomplete
    ip: Incomplete
    region: Incomplete
    def __init__(self, hash: int, bot_id: int, domain: str, browser: str, platform: str, date_created: datetime | None, date_active: datetime | None, ip: str, region: str) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class WebDocument(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    url: Incomplete
    access_hash: Incomplete
    size: Incomplete
    mime_type: Incomplete
    attributes: Incomplete
    def __init__(self, url: str, access_hash: int, size: int, mime_type: str, attributes: list['TypeDocumentAttribute']) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class WebDocumentNoProxy(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    url: Incomplete
    size: Incomplete
    mime_type: Incomplete
    attributes: Incomplete
    def __init__(self, url: str, size: int, mime_type: str, attributes: list['TypeDocumentAttribute']) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class WebPage(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    id: Incomplete
    url: Incomplete
    display_url: Incomplete
    hash: Incomplete
    has_large_media: Incomplete
    type: Incomplete
    site_name: Incomplete
    title: Incomplete
    description: Incomplete
    photo: Incomplete
    embed_url: Incomplete
    embed_type: Incomplete
    embed_width: Incomplete
    embed_height: Incomplete
    duration: Incomplete
    author: Incomplete
    document: Incomplete
    cached_page: Incomplete
    attributes: Incomplete
    def __init__(self, id: int, url: str, display_url: str, hash: int, has_large_media: bool | None = None, type: str | None = None, site_name: str | None = None, title: str | None = None, description: str | None = None, photo: TypePhoto | None = None, embed_url: str | None = None, embed_type: str | None = None, embed_width: int | None = None, embed_height: int | None = None, duration: int | None = None, author: str | None = None, document: TypeDocument | None = None, cached_page: TypePage | None = None, attributes: list['TypeWebPageAttribute'] | None = None) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class WebPageAttributeStickerSet(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    stickers: Incomplete
    emojis: Incomplete
    text_color: Incomplete
    def __init__(self, stickers: list['TypeDocument'], emojis: bool | None = None, text_color: bool | None = None) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class WebPageAttributeStory(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    peer: Incomplete
    id: Incomplete
    story: Incomplete
    def __init__(self, peer: TypePeer, id: int, story: TypeStoryItem | None = None) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class WebPageAttributeTheme(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    documents: Incomplete
    settings: Incomplete
    def __init__(self, documents: list['TypeDocument'] | None = None, settings: TypeThemeSettings | None = None) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class WebPageEmpty(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    id: Incomplete
    url: Incomplete
    def __init__(self, id: int, url: str | None = None) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class WebPageNotModified(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    cached_page_views: Incomplete
    def __init__(self, cached_page_views: int | None = None) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class WebPagePending(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    id: Incomplete
    date: Incomplete
    url: Incomplete
    def __init__(self, id: int, date: datetime | None, url: str | None = None) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class WebViewMessageSent(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    msg_id: Incomplete
    def __init__(self, msg_id: TypeInputBotInlineMessageID | None = None) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class WebViewResultUrl(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    url: Incomplete
    fullsize: Incomplete
    fullscreen: Incomplete
    query_id: Incomplete
    def __init__(self, url: str, fullsize: bool | None = None, fullscreen: bool | None = None, query_id: int | None = None) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...
TypeAccessPointRule = AccessPointRule
TypeAccountDaysTTL = AccountDaysTTL
TypeAttachMenuBot = AttachMenuBot
TypeAttachMenuBotIcon = AttachMenuBotIcon
TypeAttachMenuBotIconColor = AttachMenuBotIconColor
TypeAttachMenuBots = AttachMenuBotsNotModified | AttachMenuBots
TypeAttachMenuBotsBot = AttachMenuBotsBot
TypeAttachMenuPeerType = AttachMenuPeerTypeSameBotPM | AttachMenuPeerTypeBotPM | AttachMenuPeerTypePM | AttachMenuPeerTypeChat | AttachMenuPeerTypeBroadcast
TypeAuthorization = Authorization
TypeAutoDownloadSettings = AutoDownloadSettings
TypeAutoSaveException = AutoSaveException
TypeAutoSaveSettings = AutoSaveSettings
TypeAvailableEffect = AvailableEffect
TypeAvailableReaction = AvailableReaction
TypeBadMsgNotification = BadMsgNotification | BadServerSalt
TypeBankCardOpenUrl = BankCardOpenUrl
TypeBaseTheme = BaseThemeClassic | BaseThemeDay | BaseThemeNight | BaseThemeTinted | BaseThemeArctic
TypeBindAuthKeyInner = BindAuthKeyInner
TypeBirthday = Birthday
TypeBoost = Boost
TypeBotApp = BotAppNotModified | BotApp
TypeBotAppSettings = BotAppSettings
TypeBotBusinessConnection = BotBusinessConnection
TypeBotCommand = BotCommand
TypeBotCommandScope = BotCommandScopeDefault | BotCommandScopeUsers | BotCommandScopeChats | BotCommandScopeChatAdmins | BotCommandScopePeer | BotCommandScopePeerAdmins | BotCommandScopePeerUser
TypeBotInfo = BotInfo
TypeBotInlineResult = BotInlineResult | BotInlineMediaResult
TypeBotInlineMessage = BotInlineMessageMediaAuto | BotInlineMessageText | BotInlineMessageMediaGeo | BotInlineMessageMediaVenue | BotInlineMessageMediaContact | BotInlineMessageMediaInvoice | BotInlineMessageMediaWebPage
TypeBotMenuButton = BotMenuButtonDefault | BotMenuButtonCommands | BotMenuButton
TypeBotPreviewMedia = BotPreviewMedia
TypeBroadcastRevenueBalances = BroadcastRevenueBalances
TypeBroadcastRevenueTransaction = BroadcastRevenueTransactionProceeds | BroadcastRevenueTransactionWithdrawal | BroadcastRevenueTransactionRefund
TypeBusinessAwayMessage = BusinessAwayMessage
TypeBusinessAwayMessageSchedule = BusinessAwayMessageScheduleAlways | BusinessAwayMessageScheduleOutsideWorkHours | BusinessAwayMessageScheduleCustom
TypeBusinessBotRecipients = BusinessBotRecipients
TypeBusinessChatLink = BusinessChatLink
TypeBusinessGreetingMessage = BusinessGreetingMessage
TypeBusinessIntro = BusinessIntro
TypeBusinessLocation = BusinessLocation
TypeBusinessRecipients = BusinessRecipients
TypeBusinessWeeklyOpen = BusinessWeeklyOpen
TypeBusinessWorkHours = BusinessWorkHours
TypeCdnConfig = CdnConfig
TypeCdnPublicKey = CdnPublicKey
TypeChat = ChatEmpty | Chat | ChatForbidden | Channel | ChannelForbidden
TypeChannelAdminLogEvent = ChannelAdminLogEvent
TypeChannelAdminLogEventAction = ChannelAdminLogEventActionChangeTitle | ChannelAdminLogEventActionChangeAbout | ChannelAdminLogEventActionChangeUsername | ChannelAdminLogEventActionChangePhoto | ChannelAdminLogEventActionToggleInvites | ChannelAdminLogEventActionToggleSignatures | ChannelAdminLogEventActionUpdatePinned | ChannelAdminLogEventActionEditMessage | ChannelAdminLogEventActionDeleteMessage | ChannelAdminLogEventActionParticipantJoin | ChannelAdminLogEventActionParticipantLeave | ChannelAdminLogEventActionParticipantInvite | ChannelAdminLogEventActionParticipantToggleBan | ChannelAdminLogEventActionParticipantToggleAdmin | ChannelAdminLogEventActionChangeStickerSet | ChannelAdminLogEventActionTogglePreHistoryHidden | ChannelAdminLogEventActionDefaultBannedRights | ChannelAdminLogEventActionStopPoll | ChannelAdminLogEventActionChangeLinkedChat | ChannelAdminLogEventActionChangeLocation | ChannelAdminLogEventActionToggleSlowMode | ChannelAdminLogEventActionStartGroupCall | ChannelAdminLogEventActionDiscardGroupCall | ChannelAdminLogEventActionParticipantMute | ChannelAdminLogEventActionParticipantUnmute | ChannelAdminLogEventActionToggleGroupCallSetting | ChannelAdminLogEventActionParticipantJoinByInvite | ChannelAdminLogEventActionExportedInviteDelete | ChannelAdminLogEventActionExportedInviteRevoke | ChannelAdminLogEventActionExportedInviteEdit | ChannelAdminLogEventActionParticipantVolume | ChannelAdminLogEventActionChangeHistoryTTL | ChannelAdminLogEventActionParticipantJoinByRequest | ChannelAdminLogEventActionToggleNoForwards | ChannelAdminLogEventActionSendMessage | ChannelAdminLogEventActionChangeAvailableReactions | ChannelAdminLogEventActionChangeUsernames | ChannelAdminLogEventActionToggleForum | ChannelAdminLogEventActionCreateTopic | ChannelAdminLogEventActionEditTopic | ChannelAdminLogEventActionDeleteTopic | ChannelAdminLogEventActionPinTopic | ChannelAdminLogEventActionToggleAntiSpam | ChannelAdminLogEventActionChangePeerColor | ChannelAdminLogEventActionChangeProfilePeerColor | ChannelAdminLogEventActionChangeWallpaper | ChannelAdminLogEventActionChangeEmojiStatus | ChannelAdminLogEventActionChangeEmojiStickerSet | ChannelAdminLogEventActionToggleSignatureProfiles | ChannelAdminLogEventActionParticipantSubExtend
TypeChannelAdminLogEventsFilter = ChannelAdminLogEventsFilter
TypeChatFull = ChatFull | ChannelFull
TypeChannelLocation = ChannelLocationEmpty | ChannelLocation
TypeChannelMessagesFilter = ChannelMessagesFilterEmpty | ChannelMessagesFilter
TypeChannelParticipant = ChannelParticipant | ChannelParticipantSelf | ChannelParticipantCreator | ChannelParticipantAdmin | ChannelParticipantBanned | ChannelParticipantLeft
TypeChannelParticipantsFilter = ChannelParticipantsRecent | ChannelParticipantsAdmins | ChannelParticipantsKicked | ChannelParticipantsBots | ChannelParticipantsBanned | ChannelParticipantsSearch | ChannelParticipantsContacts | ChannelParticipantsMentions
TypeChatAdminRights = ChatAdminRights
TypeChatAdminWithInvites = ChatAdminWithInvites
TypeChatBannedRights = ChatBannedRights
TypeChatInvite = ChatInviteAlready | ChatInvite | ChatInvitePeek
TypeExportedChatInvite = ChatInviteExported | ChatInvitePublicJoinRequests
TypeChatInviteImporter = ChatInviteImporter
TypeChatOnlines = ChatOnlines
TypeChatParticipant = ChatParticipant | ChatParticipantCreator | ChatParticipantAdmin
TypeChatParticipants = ChatParticipantsForbidden | ChatParticipants
TypeChatPhoto = ChatPhotoEmpty | ChatPhoto
TypeChatReactions = ChatReactionsNone | ChatReactionsAll | ChatReactionsSome
TypeClient_DH_Inner_Data = ClientDHInnerData
TypeCodeSettings = CodeSettings
TypeConfig = Config
TypeConnectedBot = ConnectedBot
TypeContact = Contact
TypeContactBirthday = ContactBirthday
TypeContactStatus = ContactStatus
TypeDataJSON = DataJSON
TypeDcOption = DcOption
TypeDefaultHistoryTTL = DefaultHistoryTTL
TypeDestroyAuthKeyRes = DestroyAuthKeyOk | DestroyAuthKeyNone | DestroyAuthKeyFail
TypeDestroySessionRes = DestroySessionOk | DestroySessionNone
TypeSet_client_DH_params_answer = DhGenOk | DhGenRetry | DhGenFail
TypeDialog = Dialog | DialogFolder
TypeDialogFilter = DialogFilter | DialogFilterDefault | DialogFilterChatlist
TypeDialogFilterSuggested = DialogFilterSuggested
TypeDialogPeer = DialogPeer | DialogPeerFolder
TypeDocument = DocumentEmpty | Document
TypeDocumentAttribute = DocumentAttributeImageSize | DocumentAttributeAnimated | DocumentAttributeSticker | DocumentAttributeVideo | DocumentAttributeAudio | DocumentAttributeFilename | DocumentAttributeHasStickers | DocumentAttributeCustomEmoji
TypeDraftMessage = DraftMessageEmpty | DraftMessage
TypeEmailVerification = EmailVerificationCode | EmailVerificationGoogle | EmailVerificationApple
TypeEmailVerifyPurpose = EmailVerifyPurposeLoginSetup | EmailVerifyPurposeLoginChange | EmailVerifyPurposePassport
TypeEmojiGroup = EmojiGroup | EmojiGroupGreeting | EmojiGroupPremium
TypeEmojiKeyword = EmojiKeyword | EmojiKeywordDeleted
TypeEmojiKeywordsDifference = EmojiKeywordsDifference
TypeEmojiLanguage = EmojiLanguage
TypeEmojiList = EmojiListNotModified | EmojiList
TypeEmojiStatus = EmojiStatusEmpty | EmojiStatus | EmojiStatusUntil
TypeEmojiURL = EmojiURL
TypeEncryptedChat = EncryptedChatEmpty | EncryptedChatWaiting | EncryptedChatRequested | EncryptedChat | EncryptedChatDiscarded
TypeEncryptedFile = EncryptedFileEmpty | EncryptedFile
TypeEncryptedMessage = EncryptedMessage | EncryptedMessageService
TypeExportedChatlistInvite = ExportedChatlistInvite
TypeExportedContactToken = ExportedContactToken
TypeExportedMessageLink = ExportedMessageLink
TypeExportedStoryLink = ExportedStoryLink
TypeFactCheck = FactCheck
TypeFileHash = FileHash
TypeFolder = Folder
TypeFolderPeer = FolderPeer
TypeForumTopic = ForumTopicDeleted | ForumTopic
TypeFoundStory = FoundStory
TypeFutureSalt = FutureSalt
TypeFutureSalts = FutureSalts
TypeGame = Game
TypeGeoPoint = GeoPointEmpty | GeoPoint
TypeGeoPointAddress = GeoPointAddress
TypeGlobalPrivacySettings = GlobalPrivacySettings
TypeGroupCall = GroupCallDiscarded | GroupCall
TypeGroupCallParticipant = GroupCallParticipant
TypeGroupCallParticipantVideo = GroupCallParticipantVideo
TypeGroupCallParticipantVideoSourceGroup = GroupCallParticipantVideoSourceGroup
TypeGroupCallStreamChannel = GroupCallStreamChannel
TypeHighScore = HighScore
TypeHttpWait = HttpWait
TypeImportedContact = ImportedContact
TypeInlineBotSwitchPM = InlineBotSwitchPM
TypeInlineBotWebView = InlineBotWebView
TypeInlineQueryPeerType = InlineQueryPeerTypeSameBotPM | InlineQueryPeerTypePM | InlineQueryPeerTypeChat | InlineQueryPeerTypeMegagroup | InlineQueryPeerTypeBroadcast | InlineQueryPeerTypeBotPM
TypeInputAppEvent = InputAppEvent
TypeInputBotApp = InputBotAppID | InputBotAppShortName
TypeInputBotInlineMessage = InputBotInlineMessageMediaAuto | InputBotInlineMessageText | InputBotInlineMessageMediaGeo | InputBotInlineMessageMediaVenue | InputBotInlineMessageMediaContact | InputBotInlineMessageGame | InputBotInlineMessageMediaInvoice | InputBotInlineMessageMediaWebPage
TypeInputBotInlineMessageID = InputBotInlineMessageID | InputBotInlineMessageID64
TypeInputBotInlineResult = InputBotInlineResult | InputBotInlineResultPhoto | InputBotInlineResultDocument | InputBotInlineResultGame
TypeInputBusinessAwayMessage = InputBusinessAwayMessage
TypeInputBusinessBotRecipients = InputBusinessBotRecipients
TypeInputBusinessChatLink = InputBusinessChatLink
TypeInputBusinessGreetingMessage = InputBusinessGreetingMessage
TypeInputBusinessIntro = InputBusinessIntro
TypeInputBusinessRecipients = InputBusinessRecipients
TypeInputChannel = InputChannelEmpty | InputChannel | InputChannelFromMessage
TypeInputChatPhoto = InputChatPhotoEmpty | InputChatUploadedPhoto | InputChatPhoto
TypeInputChatlist = InputChatlistDialogFilter
TypeInputCheckPasswordSRP = InputCheckPasswordEmpty | InputCheckPasswordSRP
TypeInputClientProxy = InputClientProxy
TypeInputCollectible = InputCollectibleUsername | InputCollectiblePhone
TypeInputDialogPeer = InputDialogPeer | InputDialogPeerFolder
TypeInputDocument = InputDocumentEmpty | InputDocument
TypeInputFileLocation = InputFileLocation | InputEncryptedFileLocation | InputDocumentFileLocation | InputSecureFileLocation | InputTakeoutFileLocation | InputPhotoFileLocation | InputPhotoLegacyFileLocation | InputPeerPhotoFileLocation | InputStickerSetThumb | InputGroupCallStream
TypeInputEncryptedChat = InputEncryptedChat
TypeInputEncryptedFile = InputEncryptedFileEmpty | InputEncryptedFileUploaded | InputEncryptedFile | InputEncryptedFileBigUploaded
TypeInputFile = InputFile | InputFileBig | InputFileStoryDocument
TypeInputFolderPeer = InputFolderPeer
TypeInputGame = InputGameID | InputGameShortName
TypeInputGeoPoint = InputGeoPointEmpty | InputGeoPoint
TypeInputGroupCall = InputGroupCall
TypeInputInvoice = InputInvoiceMessage | InputInvoiceSlug | InputInvoicePremiumGiftCode | InputInvoiceStars | InputInvoiceChatInviteSubscription | InputInvoiceStarGift
TypeKeyboardButton = KeyboardButton | KeyboardButtonUrl | KeyboardButtonCallback | KeyboardButtonRequestPhone | KeyboardButtonRequestGeoLocation | KeyboardButtonSwitchInline | KeyboardButtonGame | KeyboardButtonBuy | KeyboardButtonUrlAuth | InputKeyboardButtonUrlAuth | KeyboardButtonRequestPoll | InputKeyboardButtonUserProfile | KeyboardButtonUserProfile | KeyboardButtonWebView | KeyboardButtonSimpleWebView | KeyboardButtonRequestPeer | InputKeyboardButtonRequestPeer | KeyboardButtonCopy
TypeMediaArea = MediaAreaVenue | InputMediaAreaVenue | MediaAreaGeoPoint | MediaAreaSuggestedReaction | MediaAreaChannelPost | InputMediaAreaChannelPost | MediaAreaUrl | MediaAreaWeather
TypeInputMedia = InputMediaEmpty | InputMediaUploadedPhoto | InputMediaPhoto | InputMediaGeoPoint | InputMediaContact | InputMediaUploadedDocument | InputMediaDocument | InputMediaVenue | InputMediaPhotoExternal | InputMediaDocumentExternal | InputMediaGame | InputMediaInvoice | InputMediaGeoLive | InputMediaPoll | InputMediaDice | InputMediaStory | InputMediaWebPage | InputMediaPaidMedia
TypeInputMessage = InputMessageID | InputMessageReplyTo | InputMessagePinned | InputMessageCallbackQuery
TypeMessageEntity = MessageEntityUnknown | MessageEntityMention | MessageEntityHashtag | MessageEntityBotCommand | MessageEntityUrl | MessageEntityEmail | MessageEntityBold | MessageEntityItalic | MessageEntityCode | MessageEntityPre | MessageEntityTextUrl | MessageEntityMentionName | InputMessageEntityMentionName | MessageEntityPhone | MessageEntityCashtag | MessageEntityUnderline | MessageEntityStrike | MessageEntityBankCard | MessageEntitySpoiler | MessageEntityCustomEmoji | MessageEntityBlockquote
TypeMessagesFilter = InputMessagesFilterEmpty | InputMessagesFilterPhotos | InputMessagesFilterVideo | InputMessagesFilterPhotoVideo | InputMessagesFilterDocument | InputMessagesFilterUrl | InputMessagesFilterGif | InputMessagesFilterVoice | InputMessagesFilterMusic | InputMessagesFilterChatPhotos | InputMessagesFilterPhoneCalls | InputMessagesFilterRoundVoice | InputMessagesFilterRoundVideo | InputMessagesFilterMyMentions | InputMessagesFilterGeo | InputMessagesFilterContacts | InputMessagesFilterPinned
TypeInputNotifyPeer = InputNotifyPeer | InputNotifyUsers | InputNotifyChats | InputNotifyBroadcasts | InputNotifyForumTopic
TypeInputPaymentCredentials = InputPaymentCredentialsSaved | InputPaymentCredentials | InputPaymentCredentialsApplePay | InputPaymentCredentialsGooglePay
TypeInputPeer = InputPeerEmpty | InputPeerSelf | InputPeerChat | InputPeerUser | InputPeerChannel | InputPeerUserFromMessage | InputPeerChannelFromMessage
TypeInputPeerNotifySettings = InputPeerNotifySettings
TypeInputPhoneCall = InputPhoneCall
TypeInputContact = InputPhoneContact
TypeInputPhoto = InputPhotoEmpty | InputPhoto
TypeInputPrivacyKey = InputPrivacyKeyStatusTimestamp | InputPrivacyKeyChatInvite | InputPrivacyKeyPhoneCall | InputPrivacyKeyPhoneP2P | InputPrivacyKeyForwards | InputPrivacyKeyProfilePhoto | InputPrivacyKeyPhoneNumber | InputPrivacyKeyAddedByPhone | InputPrivacyKeyVoiceMessages | InputPrivacyKeyAbout | InputPrivacyKeyBirthday | InputPrivacyKeyStarGiftsAutoSave
TypeInputPrivacyRule = InputPrivacyValueAllowContacts | InputPrivacyValueAllowAll | InputPrivacyValueAllowUsers | InputPrivacyValueDisallowContacts | InputPrivacyValueDisallowAll | InputPrivacyValueDisallowUsers | InputPrivacyValueAllowChatParticipants | InputPrivacyValueDisallowChatParticipants | InputPrivacyValueAllowCloseFriends | InputPrivacyValueAllowPremium | InputPrivacyValueAllowBots | InputPrivacyValueDisallowBots
TypeInputQuickReplyShortcut = InputQuickReplyShortcut | InputQuickReplyShortcutId
TypeInputReplyTo = InputReplyToMessage | InputReplyToStory
TypeReportReason = InputReportReasonSpam | InputReportReasonViolence | InputReportReasonPornography | InputReportReasonChildAbuse | InputReportReasonOther | InputReportReasonCopyright | InputReportReasonGeoIrrelevant | InputReportReasonFake | InputReportReasonIllegalDrugs | InputReportReasonPersonalDetails
TypeInputSecureFile = InputSecureFileUploaded | InputSecureFile
TypeInputSecureValue = InputSecureValue
TypeInputSingleMedia = InputSingleMedia
TypeInputStarsTransaction = InputStarsTransaction
TypeInputStickerSet = InputStickerSetEmpty | InputStickerSetID | InputStickerSetShortName | InputStickerSetAnimatedEmoji | InputStickerSetDice | InputStickerSetAnimatedEmojiAnimations | InputStickerSetPremiumGifts | InputStickerSetEmojiGenericAnimations | InputStickerSetEmojiDefaultStatuses | InputStickerSetEmojiDefaultTopicIcons | InputStickerSetEmojiChannelDefaultStatuses
TypeInputStickerSetItem = InputStickerSetItem
TypeInputStickeredMedia = InputStickeredMediaPhoto | InputStickeredMediaDocument
TypeInputStorePaymentPurpose = InputStorePaymentPremiumSubscription | InputStorePaymentGiftPremium | InputStorePaymentPremiumGiftCode | InputStorePaymentPremiumGiveaway | InputStorePaymentStarsTopup | InputStorePaymentStarsGift | InputStorePaymentStarsGiveaway
TypeInputTheme = InputTheme | InputThemeSlug
TypeInputThemeSettings = InputThemeSettings
TypeInputUser = InputUserEmpty | InputUserSelf | InputUser | InputUserFromMessage
TypeInputWallPaper = InputWallPaper | InputWallPaperSlug | InputWallPaperNoFile
TypeInputWebDocument = InputWebDocument
TypeInputWebFileLocation = InputWebFileLocation | InputWebFileGeoPointLocation | InputWebFileAudioAlbumThumbLocation
TypeInvoice = Invoice
TypeIpPort = IpPort | IpPortSecret
TypeJSONValue = JsonNull | JsonBool | JsonNumber | JsonString | JsonArray | JsonObject
TypeJSONObjectValue = JsonObjectValue
TypeKeyboardButtonRow = KeyboardButtonRow
TypeLabeledPrice = LabeledPrice
TypeLangPackDifference = LangPackDifference
TypeLangPackLanguage = LangPackLanguage
TypeLangPackString = LangPackString | LangPackStringPluralized | LangPackStringDeleted
TypeMaskCoords = MaskCoords
TypeMediaAreaCoordinates = MediaAreaCoordinates
TypeMessage = MessageEmpty | Message | MessageService
TypeMessageAction = MessageActionEmpty | MessageActionChatCreate | MessageActionChatEditTitle | MessageActionChatEditPhoto | MessageActionChatDeletePhoto | MessageActionChatAddUser | MessageActionChatDeleteUser | MessageActionChatJoinedByLink | MessageActionChannelCreate | MessageActionChatMigrateTo | MessageActionChannelMigrateFrom | MessageActionPinMessage | MessageActionHistoryClear | MessageActionGameScore | MessageActionPaymentSentMe | MessageActionPaymentSent | MessageActionPhoneCall | MessageActionScreenshotTaken | MessageActionCustomAction | MessageActionBotAllowed | MessageActionSecureValuesSentMe | MessageActionSecureValuesSent | MessageActionContactSignUp | MessageActionGeoProximityReached | MessageActionGroupCall | MessageActionInviteToGroupCall | MessageActionSetMessagesTTL | MessageActionGroupCallScheduled | MessageActionSetChatTheme | MessageActionChatJoinedByRequest | MessageActionWebViewDataSentMe | MessageActionWebViewDataSent | MessageActionGiftPremium | MessageActionTopicCreate | MessageActionTopicEdit | MessageActionSuggestProfilePhoto | MessageActionRequestedPeer | MessageActionSetChatWallPaper | MessageActionGiftCode | MessageActionGiveawayLaunch | MessageActionGiveawayResults | MessageActionBoostApply | MessageActionRequestedPeerSentMe | MessageActionPaymentRefunded | MessageActionGiftStars | MessageActionPrizeStars | MessageActionStarGift
TypeMessageExtendedMedia = MessageExtendedMediaPreview | MessageExtendedMedia
TypeMessageFwdHeader = MessageFwdHeader
TypeMessageMedia = MessageMediaEmpty | MessageMediaPhoto | MessageMediaGeo | MessageMediaContact | MessageMediaUnsupported | MessageMediaDocument | MessageMediaWebPage | MessageMediaVenue | MessageMediaGame | MessageMediaInvoice | MessageMediaGeoLive | MessageMediaPoll | MessageMediaDice | MessageMediaStory | MessageMediaGiveaway | MessageMediaGiveawayResults | MessageMediaPaidMedia
TypeMessagePeerReaction = MessagePeerReaction
TypeMessagePeerVote = MessagePeerVote | MessagePeerVoteInputOption | MessagePeerVoteMultiple
TypeMessageRange = MessageRange
TypeMessageReactions = MessageReactions
TypeMessageReactor = MessageReactor
TypeMessageReplies = MessageReplies
TypeMessageReplyHeader = MessageReplyHeader | MessageReplyStoryHeader
TypeMessageReportOption = MessageReportOption
TypeMessageViews = MessageViews
TypeMissingInvitee = MissingInvitee
TypeMsgDetailedInfo = MsgDetailedInfo | MsgNewDetailedInfo
TypeMsgResendReq = MsgResendReq
TypeMsgsAck = MsgsAck
TypeMsgsAllInfo = MsgsAllInfo
TypeMsgsStateInfo = MsgsStateInfo
TypeMsgsStateReq = MsgsStateReq
TypeMyBoost = MyBoost
TypeNearestDc = NearestDc
TypeNewSession = NewSessionCreated
TypeNotificationSound = NotificationSoundDefault | NotificationSoundNone | NotificationSoundLocal | NotificationSoundRingtone
TypeNotifyPeer = NotifyPeer | NotifyUsers | NotifyChats | NotifyBroadcasts | NotifyForumTopic
TypeOutboxReadDate = OutboxReadDate
TypeP_Q_inner_data = PQInnerData | PQInnerDataDc | PQInnerDataTemp | PQInnerDataTempDc
TypePage = Page
TypePageBlock = PageBlockUnsupported | PageBlockTitle | PageBlockSubtitle | PageBlockAuthorDate | PageBlockHeader | PageBlockSubheader | PageBlockParagraph | PageBlockPreformatted | PageBlockFooter | PageBlockDivider | PageBlockAnchor | PageBlockList | PageBlockBlockquote | PageBlockPullquote | PageBlockPhoto | PageBlockVideo | PageBlockCover | PageBlockEmbed | PageBlockEmbedPost | PageBlockCollage | PageBlockSlideshow | PageBlockChannel | PageBlockAudio | PageBlockKicker | PageBlockTable | PageBlockOrderedList | PageBlockDetails | PageBlockRelatedArticles | PageBlockMap
TypePageCaption = PageCaption
TypePageListItem = PageListItemText | PageListItemBlocks
TypePageListOrderedItem = PageListOrderedItemText | PageListOrderedItemBlocks
TypePageRelatedArticle = PageRelatedArticle
TypePageTableCell = PageTableCell
TypePageTableRow = PageTableRow
TypePasswordKdfAlgo = PasswordKdfAlgoUnknown | PasswordKdfAlgoSHA256SHA256PBKDF2HMACSHA512iter100000SHA256ModPow
TypePaymentCharge = PaymentCharge
TypePaymentFormMethod = PaymentFormMethod
TypePaymentRequestedInfo = PaymentRequestedInfo
TypePaymentSavedCredentials = PaymentSavedCredentialsCard
TypePeerBlocked = PeerBlocked
TypePeer = PeerUser | PeerChat | PeerChannel
TypePeerColor = PeerColor
TypePeerLocated = PeerLocated | PeerSelfLocated
TypePeerNotifySettings = PeerNotifySettings
TypePeerSettings = PeerSettings
TypePeerStories = PeerStories
TypePhoneCall = PhoneCallEmpty | PhoneCallWaiting | PhoneCallRequested | PhoneCallAccepted | PhoneCall | PhoneCallDiscarded
TypePhoneCallDiscardReason = PhoneCallDiscardReasonMissed | PhoneCallDiscardReasonDisconnect | PhoneCallDiscardReasonHangup | PhoneCallDiscardReasonBusy
TypePhoneCallProtocol = PhoneCallProtocol
TypePhoneConnection = PhoneConnection | PhoneConnectionWebrtc
TypePhoto = PhotoEmpty | Photo
TypePhotoSize = PhotoSizeEmpty | PhotoSize | PhotoCachedSize | PhotoStrippedSize | PhotoSizeProgressive | PhotoPathSize
TypePoll = Poll
TypePollAnswer = PollAnswer
TypePollAnswerVoters = PollAnswerVoters
TypePollResults = PollResults
TypePong = Pong
TypePopularContact = PopularContact
TypePostAddress = PostAddress
TypePostInteractionCounters = PostInteractionCountersMessage | PostInteractionCountersStory
TypePremiumGiftCodeOption = PremiumGiftCodeOption
TypePremiumGiftOption = PremiumGiftOption
TypePremiumSubscriptionOption = PremiumSubscriptionOption
TypePrepaidGiveaway = PrepaidGiveaway | PrepaidStarsGiveaway
TypePrivacyKey = PrivacyKeyStatusTimestamp | PrivacyKeyChatInvite | PrivacyKeyPhoneCall | PrivacyKeyPhoneP2P | PrivacyKeyForwards | PrivacyKeyProfilePhoto | PrivacyKeyPhoneNumber | PrivacyKeyAddedByPhone | PrivacyKeyVoiceMessages | PrivacyKeyAbout | PrivacyKeyBirthday | PrivacyKeyStarGiftsAutoSave
TypePrivacyRule = PrivacyValueAllowContacts | PrivacyValueAllowAll | PrivacyValueAllowUsers | PrivacyValueDisallowContacts | PrivacyValueDisallowAll | PrivacyValueDisallowUsers | PrivacyValueAllowChatParticipants | PrivacyValueDisallowChatParticipants | PrivacyValueAllowCloseFriends | PrivacyValueAllowPremium | PrivacyValueAllowBots | PrivacyValueDisallowBots
TypePublicForward = PublicForwardMessage | PublicForwardStory
TypeQuickReply = QuickReply
TypeReactionCount = ReactionCount
TypeReaction = ReactionEmpty | ReactionEmoji | ReactionCustomEmoji | ReactionPaid
TypeReactionNotificationsFrom = ReactionNotificationsFromContacts | ReactionNotificationsFromAll
TypeReactionsNotifySettings = ReactionsNotifySettings
TypeReadParticipantDate = ReadParticipantDate
TypeReceivedNotifyMessage = ReceivedNotifyMessage
TypeRecentMeUrl = RecentMeUrlUnknown | RecentMeUrlUser | RecentMeUrlChat | RecentMeUrlChatInvite | RecentMeUrlStickerSet
TypeReplyMarkup = ReplyKeyboardHide | ReplyKeyboardForceReply | ReplyKeyboardMarkup | ReplyInlineMarkup
TypeReportResult = ReportResultChooseOption | ReportResultAddComment | ReportResultReported
TypeRequestPeerType = RequestPeerTypeUser | RequestPeerTypeChat | RequestPeerTypeBroadcast
TypeRequestedPeer = RequestedPeerUser | RequestedPeerChat | RequestedPeerChannel
TypeResPQ = ResPQ
TypeRestrictionReason = RestrictionReason
TypeRpcDropAnswer = RpcAnswerUnknown | RpcAnswerDroppedRunning | RpcAnswerDropped
TypeRpcError = RpcError
TypeSavedDialog = SavedDialog
TypeSavedContact = SavedPhoneContact
TypeSavedReactionTag = SavedReactionTag
TypeSearchResultsPosition = SearchResultPosition
TypeSearchResultsCalendarPeriod = SearchResultsCalendarPeriod
TypeSecureCredentialsEncrypted = SecureCredentialsEncrypted
TypeSecureData = SecureData
TypeSecureFile = SecureFileEmpty | SecureFile
TypeSecurePasswordKdfAlgo = SecurePasswordKdfAlgoUnknown | SecurePasswordKdfAlgoPBKDF2HMACSHA512iter100000 | SecurePasswordKdfAlgoSHA512
TypeSecurePlainData = SecurePlainPhone | SecurePlainEmail
TypeSecureRequiredType = SecureRequiredType | SecureRequiredTypeOneOf
TypeSecureSecretSettings = SecureSecretSettings
TypeSecureValue = SecureValue
TypeSecureValueError = SecureValueErrorData | SecureValueErrorFrontSide | SecureValueErrorReverseSide | SecureValueErrorSelfie | SecureValueErrorFile | SecureValueErrorFiles | SecureValueError | SecureValueErrorTranslationFile | SecureValueErrorTranslationFiles
TypeSecureValueHash = SecureValueHash
TypeSecureValueType = SecureValueTypePersonalDetails | SecureValueTypePassport | SecureValueTypeDriverLicense | SecureValueTypeIdentityCard | SecureValueTypeInternalPassport | SecureValueTypeAddress | SecureValueTypeUtilityBill | SecureValueTypeBankStatement | SecureValueTypeRentalAgreement | SecureValueTypePassportRegistration | SecureValueTypeTemporaryRegistration | SecureValueTypePhone | SecureValueTypeEmail
TypeSendAsPeer = SendAsPeer
TypeSendMessageAction = SendMessageTypingAction | SendMessageCancelAction | SendMessageRecordVideoAction | SendMessageUploadVideoAction | SendMessageRecordAudioAction | SendMessageUploadAudioAction | SendMessageUploadPhotoAction | SendMessageUploadDocumentAction | SendMessageGeoLocationAction | SendMessageChooseContactAction | SendMessageGamePlayAction | SendMessageRecordRoundAction | SendMessageUploadRoundAction | SpeakingInGroupCallAction | SendMessageHistoryImportAction | SendMessageChooseStickerAction | SendMessageEmojiInteraction | SendMessageEmojiInteractionSeen
TypeServer_DH_inner_data = ServerDHInnerData
TypeServer_DH_Params = ServerDHParamsFail | ServerDHParamsOk
TypeShippingOption = ShippingOption
TypeSmsJob = SmsJob
TypeSponsoredMessage = SponsoredMessage
TypeSponsoredMessageReportOption = SponsoredMessageReportOption
TypeStarGift = StarGift
TypeStarsGiftOption = StarsGiftOption
TypeStarsGiveawayOption = StarsGiveawayOption
TypeStarsGiveawayWinnersOption = StarsGiveawayWinnersOption
TypeStarsRevenueStatus = StarsRevenueStatus
TypeStarsSubscription = StarsSubscription
TypeStarsSubscriptionPricing = StarsSubscriptionPricing
TypeStarsTopupOption = StarsTopupOption
TypeStarsTransaction = StarsTransaction
TypeStarsTransactionPeer = StarsTransactionPeerUnsupported | StarsTransactionPeerAppStore | StarsTransactionPeerPlayMarket | StarsTransactionPeerPremiumBot | StarsTransactionPeerFragment | StarsTransactionPeer | StarsTransactionPeerAds | StarsTransactionPeerAPI
TypeStatsAbsValueAndPrev = StatsAbsValueAndPrev
TypeStatsDateRangeDays = StatsDateRangeDays
TypeStatsGraph = StatsGraphAsync | StatsGraphError | StatsGraph
TypeStatsGroupTopAdmin = StatsGroupTopAdmin
TypeStatsGroupTopInviter = StatsGroupTopInviter
TypeStatsGroupTopPoster = StatsGroupTopPoster
TypeStatsPercentValue = StatsPercentValue
TypeStatsURL = StatsURL
TypeStickerKeyword = StickerKeyword
TypeStickerPack = StickerPack
TypeStickerSet = StickerSet
TypeStickerSetCovered = StickerSetCovered | StickerSetMultiCovered | StickerSetFullCovered | StickerSetNoCovered
TypeStoriesStealthMode = StoriesStealthMode
TypeStoryFwdHeader = StoryFwdHeader
TypeStoryItem = StoryItemDeleted | StoryItemSkipped | StoryItem
TypeStoryReaction = StoryReaction | StoryReactionPublicForward | StoryReactionPublicRepost
TypeStoryView = StoryView | StoryViewPublicForward | StoryViewPublicRepost
TypeStoryViews = StoryViews
TypeRichText = TextEmpty | TextPlain | TextBold | TextItalic | TextUnderline | TextStrike | TextFixed | TextUrl | TextEmail | TextConcat | TextSubscript | TextSuperscript | TextMarked | TextPhone | TextImage | TextAnchor
TypeTextWithEntities = TextWithEntities
TypeTheme = Theme
TypeThemeSettings = ThemeSettings
TypeTimezone = Timezone
TypeTlsBlock = TlsBlockString | TlsBlockRandom | TlsBlockZero | TlsBlockDomain | TlsBlockGrease | TlsBlockPublicKey | TlsBlockScope
TypeTlsClientHello = TlsClientHello
TypeTopPeer = TopPeer
TypeTopPeerCategory = TopPeerCategoryBotsPM | TopPeerCategoryBotsInline | TopPeerCategoryCorrespondents | TopPeerCategoryGroups | TopPeerCategoryChannels | TopPeerCategoryPhoneCalls | TopPeerCategoryForwardUsers | TopPeerCategoryForwardChats | TopPeerCategoryBotsApp
TypeTopPeerCategoryPeers = TopPeerCategoryPeers
TypeUpdate = UpdateNewMessage | UpdateMessageID | UpdateDeleteMessages | UpdateUserTyping | UpdateChatUserTyping | UpdateChatParticipants | UpdateUserStatus | UpdateUserName | UpdateNewAuthorization | UpdateNewEncryptedMessage | UpdateEncryptedChatTyping | UpdateEncryption | UpdateEncryptedMessagesRead | UpdateChatParticipantAdd | UpdateChatParticipantDelete | UpdateDcOptions | UpdateNotifySettings | UpdateServiceNotification | UpdatePrivacy | UpdateUserPhone | UpdateReadHistoryInbox | UpdateReadHistoryOutbox | UpdateWebPage | UpdateReadMessagesContents | UpdateChannelTooLong | UpdateChannel | UpdateNewChannelMessage | UpdateReadChannelInbox | UpdateDeleteChannelMessages | UpdateChannelMessageViews | UpdateChatParticipantAdmin | UpdateNewStickerSet | UpdateStickerSetsOrder | UpdateStickerSets | UpdateSavedGifs | UpdateBotInlineQuery | UpdateBotInlineSend | UpdateEditChannelMessage | UpdateBotCallbackQuery | UpdateEditMessage | UpdateInlineBotCallbackQuery | UpdateReadChannelOutbox | UpdateDraftMessage | UpdateReadFeaturedStickers | UpdateRecentStickers | UpdateConfig | UpdatePtsChanged | UpdateChannelWebPage | UpdateDialogPinned | UpdatePinnedDialogs | UpdateBotWebhookJSON | UpdateBotWebhookJSONQuery | UpdateBotShippingQuery | UpdateBotPrecheckoutQuery | UpdatePhoneCall | UpdateLangPackTooLong | UpdateLangPack | UpdateFavedStickers | UpdateChannelReadMessagesContents | UpdateContactsReset | UpdateChannelAvailableMessages | UpdateDialogUnreadMark | UpdateMessagePoll | UpdateChatDefaultBannedRights | UpdateFolderPeers | UpdatePeerSettings | UpdatePeerLocated | UpdateNewScheduledMessage | UpdateDeleteScheduledMessages | UpdateTheme | UpdateGeoLiveViewed | UpdateLoginToken | UpdateMessagePollVote | UpdateDialogFilter | UpdateDialogFilterOrder | UpdateDialogFilters | UpdatePhoneCallSignalingData | UpdateChannelMessageForwards | UpdateReadChannelDiscussionInbox | UpdateReadChannelDiscussionOutbox | UpdatePeerBlocked | UpdateChannelUserTyping | UpdatePinnedMessages | UpdatePinnedChannelMessages | UpdateChat | UpdateGroupCallParticipants | UpdateGroupCall | UpdatePeerHistoryTTL | UpdateChatParticipant | UpdateChannelParticipant | UpdateBotStopped | UpdateGroupCallConnection | UpdateBotCommands | UpdatePendingJoinRequests | UpdateBotChatInviteRequester | UpdateMessageReactions | UpdateAttachMenuBots | UpdateWebViewResultSent | UpdateBotMenuButton | UpdateSavedRingtones | UpdateTranscribedAudio | UpdateReadFeaturedEmojiStickers | UpdateUserEmojiStatus | UpdateRecentEmojiStatuses | UpdateRecentReactions | UpdateMoveStickerSetToTop | UpdateMessageExtendedMedia | UpdateChannelPinnedTopic | UpdateChannelPinnedTopics | UpdateUser | UpdateAutoSaveSettings | UpdateStory | UpdateReadStories | UpdateStoryID | UpdateStoriesStealthMode | UpdateSentStoryReaction | UpdateBotChatBoost | UpdateChannelViewForumAsMessages | UpdatePeerWallpaper | UpdateBotMessageReaction | UpdateBotMessageReactions | UpdateSavedDialogPinned | UpdatePinnedSavedDialogs | UpdateSavedReactionTags | UpdateSmsJob | UpdateQuickReplies | UpdateNewQuickReply | UpdateDeleteQuickReply | UpdateQuickReplyMessage | UpdateDeleteQuickReplyMessages | UpdateBotBusinessConnect | UpdateBotNewBusinessMessage | UpdateBotEditBusinessMessage | UpdateBotDeleteBusinessMessage | UpdateNewStoryReaction | UpdateBroadcastRevenueTransactions | UpdateStarsBalance | UpdateBusinessBotCallbackQuery | UpdateStarsRevenueStatus | UpdateBotPurchasedPaidMedia | UpdatePaidReactionPrivacy | UpdateBotSubscriptionExpire
TypeUpdates = UpdatesTooLong | UpdateShortMessage | UpdateShortChatMessage | UpdateShort | UpdatesCombined | Updates | UpdateShortSentMessage
TypeUrlAuthResult = UrlAuthResultRequest | UrlAuthResultAccepted | UrlAuthResultDefault
TypeUser = UserEmpty | User
TypeUserFull = UserFull
TypeUserProfilePhoto = UserProfilePhotoEmpty | UserProfilePhoto
TypeUserStarGift = UserStarGift
TypeUserStatus = UserStatusEmpty | UserStatusOnline | UserStatusOffline | UserStatusRecently | UserStatusLastWeek | UserStatusLastMonth
TypeUsername = Username
TypeVideoSize = VideoSize | VideoSizeEmojiMarkup | VideoSizeStickerMarkup
TypeWallPaper = WallPaper | WallPaperNoFile
TypeWallPaperSettings = WallPaperSettings
TypeWebAuthorization = WebAuthorization
TypeWebDocument = WebDocument | WebDocumentNoProxy
TypeWebPage = WebPageEmpty | WebPagePending | WebPage | WebPageNotModified
TypeWebPageAttribute = WebPageAttributeTheme | WebPageAttributeStory | WebPageAttributeStickerSet
TypeWebViewMessageSent = WebViewMessageSent
TypeWebViewResult = WebViewResultUrl
