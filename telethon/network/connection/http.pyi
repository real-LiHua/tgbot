from .connection import Connection as Connection, PacketCodec as PacketCodec
from _typeshed import Incomplete

SSL_PORT: int

class HttpPacketCodec(PacketCodec):
    tag: Incomplete
    obfuscate_tag: Incomplete
    def encode_packet(self, data): ...
    async def read_packet(self, reader): ...

class ConnectionHttp(Connection):
    packet_codec = HttpPacketCodec
    async def connect(self, timeout: Incomplete | None = None, ssl: Incomplete | None = None) -> None: ...
