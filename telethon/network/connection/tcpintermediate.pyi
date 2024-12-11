from .connection import Connection as Connection, PacketCodec as PacketCodec
from _typeshed import Incomplete

class IntermediatePacketCodec(PacketCodec):
    tag: bytes
    obfuscate_tag = tag
    def encode_packet(self, data): ...
    async def read_packet(self, reader): ...

class RandomizedIntermediatePacketCodec(IntermediatePacketCodec):
    tag: Incomplete
    obfuscate_tag: bytes
    def encode_packet(self, data): ...
    async def read_packet(self, reader): ...

class ConnectionTcpIntermediate(Connection):
    packet_codec = IntermediatePacketCodec
