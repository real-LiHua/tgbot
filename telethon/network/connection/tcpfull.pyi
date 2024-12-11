from ...errors import InvalidBufferError as InvalidBufferError, InvalidChecksumError as InvalidChecksumError
from .connection import Connection as Connection, PacketCodec as PacketCodec
from _typeshed import Incomplete

class FullPacketCodec(PacketCodec):
    tag: Incomplete
    def __init__(self, connection) -> None: ...
    def encode_packet(self, data): ...
    async def read_packet(self, reader): ...

class ConnectionTcpFull(Connection):
    packet_codec = FullPacketCodec
