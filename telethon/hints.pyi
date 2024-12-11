import datetime
import typing
from . import helpers as helpers
from .tl import custom as custom, types as types
from _typeshed import Incomplete

Phone = str
Username = str
PeerID = int
Entity = types.User | types.Chat | types.Channel
FullEntity = types.UserFull | types.messages.ChatFull | types.ChatFull | types.ChannelFull
EntityLike: Incomplete
EntitiesLike = EntityLike | typing.Sequence[EntityLike]
ButtonLike: Incomplete
MarkupLike: Incomplete
TotalList = helpers.TotalList
DateLike = float | datetime.datetime | datetime.date | datetime.timedelta | None
LocalPath = str
ExternalUrl = str
BotFileID = str
FileLike: Incomplete
OutFileLike = str | type[bytes] | typing.BinaryIO
OutFileLike = str | typing.BinaryIO
MessageLike = str | types.Message
MessageIDLike: Incomplete
ProgressCallback = typing.Callable[[int, int], None]
