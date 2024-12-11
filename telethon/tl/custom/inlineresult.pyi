from .. import functions as functions, types as types
from ... import utils as utils
from _typeshed import Incomplete

class InlineResult:
    ARTICLE: str
    PHOTO: str
    GIF: str
    VIDEO: str
    VIDEO_GIF: str
    AUDIO: str
    DOCUMENT: str
    LOCATION: str
    VENUE: str
    CONTACT: str
    GAME: str
    result: Incomplete
    def __init__(self, client, original, query_id: Incomplete | None = None, *, entity: Incomplete | None = None) -> None: ...
    @property
    def type(self): ...
    @property
    def message(self): ...
    @property
    def title(self): ...
    @property
    def description(self): ...
    @property
    def url(self): ...
    @property
    def photo(self): ...
    @property
    def document(self): ...
    async def click(self, entity: Incomplete | None = None, reply_to: Incomplete | None = None, comment_to: Incomplete | None = None, silent: bool = False, clear_draft: bool = False, hide_via: bool = False, background: Incomplete | None = None): ...
    async def download_media(self, *args, **kwargs): ...
