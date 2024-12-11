from ..helpers import add_surrogate as add_surrogate, del_surrogate as del_surrogate, strip_text as strip_text, within_surrogate as within_surrogate
from ..tl import TLObject as TLObject
from ..tl.types import MessageEntityBlockquote as MessageEntityBlockquote, MessageEntityBold as MessageEntityBold, MessageEntityCode as MessageEntityCode, MessageEntityEmail as MessageEntityEmail, MessageEntityItalic as MessageEntityItalic, MessageEntityMentionName as MessageEntityMentionName, MessageEntityPre as MessageEntityPre, MessageEntityStrike as MessageEntityStrike, MessageEntityTextUrl as MessageEntityTextUrl, MessageEntityUnderline as MessageEntityUnderline, MessageEntityUrl as MessageEntityUrl, TypeMessageEntity as TypeMessageEntity
from _typeshed import Incomplete
from html.parser import HTMLParser
from typing import Iterable

class HTMLToTelegramParser(HTMLParser):
    text: str
    entities: Incomplete
    def __init__(self) -> None: ...
    def handle_starttag(self, tag, attrs) -> None: ...
    def handle_data(self, text) -> None: ...
    def handle_endtag(self, tag) -> None: ...

def parse(html: str) -> tuple[str, list[TypeMessageEntity]]: ...

ENTITY_TO_FORMATTER: Incomplete

def unparse(text: str, entities: Iterable[TypeMessageEntity]) -> str: ...
