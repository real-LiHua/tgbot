from .. import helpers as helpers, utils as utils
from ..tl import types as types
from .telegramclient import TelegramClient as TelegramClient

class MessageParseMethods:
    @property
    def parse_mode(self): ...
    @parse_mode.setter
    def parse_mode(self, mode: str): ...
