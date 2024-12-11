from ...tl.tlobject import TLObject as TLObject
from ...tl.types import TypeAvailableEffect as TypeAvailableEffect, TypeAvailableReaction as TypeAvailableReaction, TypeBotApp as TypeBotApp, TypeBotInlineResult as TypeBotInlineResult, TypeChat as TypeChat, TypeChatAdminWithInvites as TypeChatAdminWithInvites, TypeChatFull as TypeChatFull, TypeChatInviteImporter as TypeChatInviteImporter, TypeDialog as TypeDialog, TypeDialogFilter as TypeDialogFilter, TypeDocument as TypeDocument, TypeEmojiGroup as TypeEmojiGroup, TypeEncryptedFile as TypeEncryptedFile, TypeExportedChatInvite as TypeExportedChatInvite, TypeForumTopic as TypeForumTopic, TypeHighScore as TypeHighScore, TypeInlineBotSwitchPM as TypeInlineBotSwitchPM, TypeInlineBotWebView as TypeInlineBotWebView, TypeInlineQueryPeerType as TypeInlineQueryPeerType, TypeMessage as TypeMessage, TypeMessagePeerReaction as TypeMessagePeerReaction, TypeMessagePeerVote as TypeMessagePeerVote, TypeMessageViews as TypeMessageViews, TypeMessagesFilter as TypeMessagesFilter, TypeMissingInvitee as TypeMissingInvitee, TypePeerSettings as TypePeerSettings, TypeQuickReply as TypeQuickReply, TypeReaction as TypeReaction, TypeSavedDialog as TypeSavedDialog, TypeSavedReactionTag as TypeSavedReactionTag, TypeSearchResultsCalendarPeriod as TypeSearchResultsCalendarPeriod, TypeSearchResultsPosition as TypeSearchResultsPosition, TypeSponsoredMessage as TypeSponsoredMessage, TypeStickerKeyword as TypeStickerKeyword, TypeStickerPack as TypeStickerPack, TypeStickerSet as TypeStickerSet, TypeStickerSetCovered as TypeStickerSetCovered, TypeTextWithEntities as TypeTextWithEntities, TypeUpdates as TypeUpdates, TypeUser as TypeUser, TypeWebPage as TypeWebPage
from ...tl.types.updates import TypeState as TypeState
from _typeshed import Incomplete
from datetime import datetime

class AffectedFoundMessages(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    pts: Incomplete
    pts_count: Incomplete
    offset: Incomplete
    messages: Incomplete
    def __init__(self, pts: int, pts_count: int, offset: int, messages: list[int]) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class AffectedHistory(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    pts: Incomplete
    pts_count: Incomplete
    offset: Incomplete
    def __init__(self, pts: int, pts_count: int, offset: int) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class AffectedMessages(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    pts: Incomplete
    pts_count: Incomplete
    def __init__(self, pts: int, pts_count: int) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class AllStickers(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    hash: Incomplete
    sets: Incomplete
    def __init__(self, hash: int, sets: list['TypeStickerSet']) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class AllStickersNotModified(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class ArchivedStickers(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    count: Incomplete
    sets: Incomplete
    def __init__(self, count: int, sets: list['TypeStickerSetCovered']) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class AvailableEffects(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    hash: Incomplete
    effects: Incomplete
    documents: Incomplete
    def __init__(self, hash: int, effects: list['TypeAvailableEffect'], documents: list['TypeDocument']) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class AvailableEffectsNotModified(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class AvailableReactions(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    hash: Incomplete
    reactions: Incomplete
    def __init__(self, hash: int, reactions: list['TypeAvailableReaction']) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class AvailableReactionsNotModified(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class BotApp(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    app: Incomplete
    inactive: Incomplete
    request_write_access: Incomplete
    has_settings: Incomplete
    def __init__(self, app: TypeBotApp, inactive: bool | None = None, request_write_access: bool | None = None, has_settings: bool | None = None) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class BotCallbackAnswer(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    cache_time: Incomplete
    alert: Incomplete
    has_url: Incomplete
    native_ui: Incomplete
    message: Incomplete
    url: Incomplete
    def __init__(self, cache_time: int, alert: bool | None = None, has_url: bool | None = None, native_ui: bool | None = None, message: str | None = None, url: str | None = None) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class BotPreparedInlineMessage(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    id: Incomplete
    expire_date: Incomplete
    def __init__(self, id: str, expire_date: datetime | None) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class BotResults(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    query_id: Incomplete
    results: Incomplete
    cache_time: Incomplete
    users: Incomplete
    gallery: Incomplete
    next_offset: Incomplete
    switch_pm: Incomplete
    switch_webview: Incomplete
    def __init__(self, query_id: int, results: list['TypeBotInlineResult'], cache_time: int, users: list['TypeUser'], gallery: bool | None = None, next_offset: str | None = None, switch_pm: TypeInlineBotSwitchPM | None = None, switch_webview: TypeInlineBotWebView | None = None) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class ChannelMessages(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    pts: Incomplete
    count: Incomplete
    messages: Incomplete
    topics: Incomplete
    chats: Incomplete
    users: Incomplete
    inexact: Incomplete
    offset_id_offset: Incomplete
    def __init__(self, pts: int, count: int, messages: list['TypeMessage'], topics: list['TypeForumTopic'], chats: list['TypeChat'], users: list['TypeUser'], inexact: bool | None = None, offset_id_offset: int | None = None) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class ChatAdminsWithInvites(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    admins: Incomplete
    users: Incomplete
    def __init__(self, admins: list['TypeChatAdminWithInvites'], users: list['TypeUser']) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class ChatFull(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    full_chat: Incomplete
    chats: Incomplete
    users: Incomplete
    def __init__(self, full_chat: TypeChatFull, chats: list['TypeChat'], users: list['TypeUser']) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class ChatInviteImporters(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    count: Incomplete
    importers: Incomplete
    users: Incomplete
    def __init__(self, count: int, importers: list['TypeChatInviteImporter'], users: list['TypeUser']) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class Chats(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    chats: Incomplete
    def __init__(self, chats: list['TypeChat']) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class ChatsSlice(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    count: Incomplete
    chats: Incomplete
    def __init__(self, count: int, chats: list['TypeChat']) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class CheckedHistoryImportPeer(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    confirm_text: Incomplete
    def __init__(self, confirm_text: str) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class DhConfig(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    g: Incomplete
    p: Incomplete
    version: Incomplete
    random: Incomplete
    def __init__(self, g: int, p: bytes, version: int, random: bytes) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class DhConfigNotModified(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    random: Incomplete
    def __init__(self, random: bytes) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class DialogFilters(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    filters: Incomplete
    tags_enabled: Incomplete
    def __init__(self, filters: list['TypeDialogFilter'], tags_enabled: bool | None = None) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class Dialogs(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    dialogs: Incomplete
    messages: Incomplete
    chats: Incomplete
    users: Incomplete
    def __init__(self, dialogs: list['TypeDialog'], messages: list['TypeMessage'], chats: list['TypeChat'], users: list['TypeUser']) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class DialogsNotModified(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    count: Incomplete
    def __init__(self, count: int) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class DialogsSlice(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    count: Incomplete
    dialogs: Incomplete
    messages: Incomplete
    chats: Incomplete
    users: Incomplete
    def __init__(self, count: int, dialogs: list['TypeDialog'], messages: list['TypeMessage'], chats: list['TypeChat'], users: list['TypeUser']) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class DiscussionMessage(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    messages: Incomplete
    unread_count: Incomplete
    chats: Incomplete
    users: Incomplete
    max_id: Incomplete
    read_inbox_max_id: Incomplete
    read_outbox_max_id: Incomplete
    def __init__(self, messages: list['TypeMessage'], unread_count: int, chats: list['TypeChat'], users: list['TypeUser'], max_id: int | None = None, read_inbox_max_id: int | None = None, read_outbox_max_id: int | None = None) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class EmojiGroups(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    hash: Incomplete
    groups: Incomplete
    def __init__(self, hash: int, groups: list['TypeEmojiGroup']) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class EmojiGroupsNotModified(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class ExportedChatInvite(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    invite: Incomplete
    users: Incomplete
    def __init__(self, invite: TypeExportedChatInvite, users: list['TypeUser']) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class ExportedChatInviteReplaced(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    invite: Incomplete
    new_invite: Incomplete
    users: Incomplete
    def __init__(self, invite: TypeExportedChatInvite, new_invite: TypeExportedChatInvite, users: list['TypeUser']) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class ExportedChatInvites(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    count: Incomplete
    invites: Incomplete
    users: Incomplete
    def __init__(self, count: int, invites: list['TypeExportedChatInvite'], users: list['TypeUser']) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class FavedStickers(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    hash: Incomplete
    packs: Incomplete
    stickers: Incomplete
    def __init__(self, hash: int, packs: list['TypeStickerPack'], stickers: list['TypeDocument']) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class FavedStickersNotModified(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class FeaturedStickers(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    hash: Incomplete
    count: Incomplete
    sets: Incomplete
    unread: Incomplete
    premium: Incomplete
    def __init__(self, hash: int, count: int, sets: list['TypeStickerSetCovered'], unread: list[int], premium: bool | None = None) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class FeaturedStickersNotModified(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    count: Incomplete
    def __init__(self, count: int) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class ForumTopics(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    count: Incomplete
    topics: Incomplete
    messages: Incomplete
    chats: Incomplete
    users: Incomplete
    pts: Incomplete
    order_by_create_date: Incomplete
    def __init__(self, count: int, topics: list['TypeForumTopic'], messages: list['TypeMessage'], chats: list['TypeChat'], users: list['TypeUser'], pts: int, order_by_create_date: bool | None = None) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class FoundStickerSets(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    hash: Incomplete
    sets: Incomplete
    def __init__(self, hash: int, sets: list['TypeStickerSetCovered']) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class FoundStickerSetsNotModified(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class HighScores(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    scores: Incomplete
    users: Incomplete
    def __init__(self, scores: list['TypeHighScore'], users: list['TypeUser']) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class HistoryImport(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    id: Incomplete
    def __init__(self, id: int) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class HistoryImportParsed(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    pm: Incomplete
    group: Incomplete
    title: Incomplete
    def __init__(self, pm: bool | None = None, group: bool | None = None, title: str | None = None) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class InactiveChats(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    dates: Incomplete
    chats: Incomplete
    users: Incomplete
    def __init__(self, dates: list[int], chats: list['TypeChat'], users: list['TypeUser']) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class InvitedUsers(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    updates: Incomplete
    missing_invitees: Incomplete
    def __init__(self, updates: TypeUpdates, missing_invitees: list['TypeMissingInvitee']) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class MessageEditData(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    caption: Incomplete
    def __init__(self, caption: bool | None = None) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class MessageReactionsList(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    count: Incomplete
    reactions: Incomplete
    chats: Incomplete
    users: Incomplete
    next_offset: Incomplete
    def __init__(self, count: int, reactions: list['TypeMessagePeerReaction'], chats: list['TypeChat'], users: list['TypeUser'], next_offset: str | None = None) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class MessageViews(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    views: Incomplete
    chats: Incomplete
    users: Incomplete
    def __init__(self, views: list['TypeMessageViews'], chats: list['TypeChat'], users: list['TypeUser']) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class Messages(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    messages: Incomplete
    chats: Incomplete
    users: Incomplete
    def __init__(self, messages: list['TypeMessage'], chats: list['TypeChat'], users: list['TypeUser']) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class MessagesNotModified(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    count: Incomplete
    def __init__(self, count: int) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class MessagesSlice(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    count: Incomplete
    messages: Incomplete
    chats: Incomplete
    users: Incomplete
    inexact: Incomplete
    next_rate: Incomplete
    offset_id_offset: Incomplete
    def __init__(self, count: int, messages: list['TypeMessage'], chats: list['TypeChat'], users: list['TypeUser'], inexact: bool | None = None, next_rate: int | None = None, offset_id_offset: int | None = None) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class MyStickers(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    count: Incomplete
    sets: Incomplete
    def __init__(self, count: int, sets: list['TypeStickerSetCovered']) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class PeerDialogs(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    dialogs: Incomplete
    messages: Incomplete
    chats: Incomplete
    users: Incomplete
    state: Incomplete
    def __init__(self, dialogs: list['TypeDialog'], messages: list['TypeMessage'], chats: list['TypeChat'], users: list['TypeUser'], state: TypeState) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class PeerSettings(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    settings: Incomplete
    chats: Incomplete
    users: Incomplete
    def __init__(self, settings: TypePeerSettings, chats: list['TypeChat'], users: list['TypeUser']) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class PreparedInlineMessage(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    query_id: Incomplete
    result: Incomplete
    peer_types: Incomplete
    cache_time: Incomplete
    users: Incomplete
    def __init__(self, query_id: int, result: TypeBotInlineResult, peer_types: list['TypeInlineQueryPeerType'], cache_time: int, users: list['TypeUser']) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class QuickReplies(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    quick_replies: Incomplete
    messages: Incomplete
    chats: Incomplete
    users: Incomplete
    def __init__(self, quick_replies: list['TypeQuickReply'], messages: list['TypeMessage'], chats: list['TypeChat'], users: list['TypeUser']) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class QuickRepliesNotModified(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class Reactions(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    hash: Incomplete
    reactions: Incomplete
    def __init__(self, hash: int, reactions: list['TypeReaction']) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class ReactionsNotModified(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class RecentStickers(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    hash: Incomplete
    packs: Incomplete
    stickers: Incomplete
    dates: Incomplete
    def __init__(self, hash: int, packs: list['TypeStickerPack'], stickers: list['TypeDocument'], dates: list[int]) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class RecentStickersNotModified(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class SavedDialogs(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    dialogs: Incomplete
    messages: Incomplete
    chats: Incomplete
    users: Incomplete
    def __init__(self, dialogs: list['TypeSavedDialog'], messages: list['TypeMessage'], chats: list['TypeChat'], users: list['TypeUser']) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class SavedDialogsNotModified(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    count: Incomplete
    def __init__(self, count: int) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class SavedDialogsSlice(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    count: Incomplete
    dialogs: Incomplete
    messages: Incomplete
    chats: Incomplete
    users: Incomplete
    def __init__(self, count: int, dialogs: list['TypeSavedDialog'], messages: list['TypeMessage'], chats: list['TypeChat'], users: list['TypeUser']) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class SavedGifs(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    hash: Incomplete
    gifs: Incomplete
    def __init__(self, hash: int, gifs: list['TypeDocument']) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class SavedGifsNotModified(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class SavedReactionTags(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    tags: Incomplete
    hash: Incomplete
    def __init__(self, tags: list['TypeSavedReactionTag'], hash: int) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class SavedReactionTagsNotModified(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class SearchCounter(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    filter: Incomplete
    count: Incomplete
    inexact: Incomplete
    def __init__(self, filter: TypeMessagesFilter, count: int, inexact: bool | None = None) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class SearchResultsCalendar(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    count: Incomplete
    min_date: Incomplete
    min_msg_id: Incomplete
    periods: Incomplete
    messages: Incomplete
    chats: Incomplete
    users: Incomplete
    inexact: Incomplete
    offset_id_offset: Incomplete
    def __init__(self, count: int, min_date: datetime | None, min_msg_id: int, periods: list['TypeSearchResultsCalendarPeriod'], messages: list['TypeMessage'], chats: list['TypeChat'], users: list['TypeUser'], inexact: bool | None = None, offset_id_offset: int | None = None) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class SearchResultsPositions(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    count: Incomplete
    positions: Incomplete
    def __init__(self, count: int, positions: list['TypeSearchResultsPosition']) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class SentEncryptedFile(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    date: Incomplete
    file: Incomplete
    def __init__(self, date: datetime | None, file: TypeEncryptedFile) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class SentEncryptedMessage(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    date: Incomplete
    def __init__(self, date: datetime | None) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class SponsoredMessages(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    messages: Incomplete
    chats: Incomplete
    users: Incomplete
    posts_between: Incomplete
    def __init__(self, messages: list['TypeSponsoredMessage'], chats: list['TypeChat'], users: list['TypeUser'], posts_between: int | None = None) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class SponsoredMessagesEmpty(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class StickerSet(TLObject):
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

class StickerSetInstallResultArchive(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    sets: Incomplete
    def __init__(self, sets: list['TypeStickerSetCovered']) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class StickerSetInstallResultSuccess(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class StickerSetNotModified(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class Stickers(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    hash: Incomplete
    stickers: Incomplete
    def __init__(self, hash: int, stickers: list['TypeDocument']) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class StickersNotModified(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class TranscribedAudio(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    transcription_id: Incomplete
    text: Incomplete
    pending: Incomplete
    trial_remains_num: Incomplete
    trial_remains_until_date: Incomplete
    def __init__(self, transcription_id: int, text: str, pending: bool | None = None, trial_remains_num: int | None = None, trial_remains_until_date: datetime | None = None) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class TranslateResult(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    result: Incomplete
    def __init__(self, result: list['TypeTextWithEntities']) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class VotesList(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    count: Incomplete
    votes: Incomplete
    chats: Incomplete
    users: Incomplete
    next_offset: Incomplete
    def __init__(self, count: int, votes: list['TypeMessagePeerVote'], chats: list['TypeChat'], users: list['TypeUser'], next_offset: str | None = None) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class WebPage(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    webpage: Incomplete
    chats: Incomplete
    users: Incomplete
    def __init__(self, webpage: TypeWebPage, chats: list['TypeChat'], users: list['TypeUser']) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...
