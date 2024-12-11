from .. import hints as hints
from ..tl import custom as custom, functions as functions, types as types
from .telegramclient import TelegramClient as TelegramClient

class BotMethods:
    async def inline_query(self, bot: hints.EntityLike, query: str, *, entity: hints.EntityLike = None, offset: str = None, geo_point: types.GeoPoint = None) -> custom.InlineResults: ...
