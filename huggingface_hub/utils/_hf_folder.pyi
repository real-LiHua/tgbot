from .. import constants as constants
from ._auth import get_token as get_token
from _typeshed import Incomplete

class HfFolder:
    path_token: Incomplete
    @classmethod
    def save_token(cls, token: str) -> None: ...
    @classmethod
    def get_token(cls) -> str | None: ...
    @classmethod
    def delete_token(cls) -> None: ...
