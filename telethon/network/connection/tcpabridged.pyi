from .connection import Connection as Connection, PacketCodec as PacketCodec

class AbridgedPacketCodec(PacketCodec):
    tag: bytes
    obfuscate_tag: bytes
    def encode_packet(self, data): ...
    async def read_packet(self, reader): ...

class ConnectionTcpAbridged(Connection):
    packet_codec = AbridgedPacketCodec
