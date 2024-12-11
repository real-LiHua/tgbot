from ..errors import InvalidBufferError as InvalidBufferError
from ..extensions import BinaryReader as BinaryReader
from .mtprotostate import MTProtoState as MTProtoState

class MTProtoPlainSender:
    def __init__(self, connection, *, loggers) -> None: ...
    async def send(self, request): ...
