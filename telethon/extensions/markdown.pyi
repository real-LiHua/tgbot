from ..helpers import add_surrogate as add_surrogate, del_surrogate as del_surrogate, strip_text as strip_text, within_surrogate as within_surrogate
from ..tl import TLObject as TLObject
from ..tl.types import MessageEntityBold as MessageEntityBold, MessageEntityCode as MessageEntityCode, MessageEntityItalic as MessageEntityItalic, MessageEntityMentionName as MessageEntityMentionName, MessageEntityPre as MessageEntityPre, MessageEntityStrike as MessageEntityStrike, MessageEntityTextUrl as MessageEntityTextUrl
from _typeshed import Incomplete

DEFAULT_DELIMITERS: Incomplete
DEFAULT_URL_RE: Incomplete
DEFAULT_URL_FORMAT: str

def overlap(a, b, x, y): ...
def parse(message, delimiters: Incomplete | None = None, url_re: Incomplete | None = None): ...
def unparse(text, entities, delimiters: Incomplete | None = None, url_fmt: Incomplete | None = None): ...
