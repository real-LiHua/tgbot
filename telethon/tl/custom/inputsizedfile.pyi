from ..types import InputFile as InputFile
from _typeshed import Incomplete

class InputSizedFile(InputFile):
    md5: Incomplete
    size: Incomplete
    def __init__(self, id_, parts, name, md5, size) -> None: ...
