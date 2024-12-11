from ... import helpers as helpers, utils as utils
from ...tl import types as types
from .chatgetter import ChatGetter as ChatGetter
from .sendergetter import SenderGetter as SenderGetter
from _typeshed import Incomplete

class Forward(ChatGetter, SenderGetter):
    original_fwd: Incomplete
    def __init__(self, client, original, entities) -> None: ...
