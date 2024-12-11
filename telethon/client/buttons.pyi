from .. import hints as hints, utils as utils
from ..tl import custom as custom, types as types

class ButtonMethods:
    @staticmethod
    def build_reply_markup(buttons: hints.MarkupLike | None, inline_only: bool = False) -> types.TypeReplyMarkup | None: ...
