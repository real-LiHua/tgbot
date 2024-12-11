from ...crypto import AESModeCTR as AESModeCTR
from .connection import ObfuscatedConnection as ObfuscatedConnection
from .tcpabridged import AbridgedPacketCodec as AbridgedPacketCodec
from .tcpintermediate import IntermediatePacketCodec as IntermediatePacketCodec, RandomizedIntermediatePacketCodec as RandomizedIntermediatePacketCodec
from _typeshed import Incomplete

class MTProxyIO:
    header: Incomplete
    def __init__(self, connection) -> None: ...
    @staticmethod
    def init_header(secret, dc_id, packet_codec): ...
    async def readexactly(self, n): ...
    def write(self, data) -> None: ...

class TcpMTProxy(ObfuscatedConnection):
    packet_codec: Incomplete
    obfuscated_io = MTProxyIO
    def __init__(self, ip, port, dc_id, *, loggers, proxy: Incomplete | None = None, local_addr: Incomplete | None = None) -> None: ...
    @staticmethod
    def address_info(proxy_info): ...
    @staticmethod
    def normalize_secret(secret): ...

class ConnectionTcpMTProxyAbridged(TcpMTProxy):
    packet_codec = AbridgedPacketCodec

class ConnectionTcpMTProxyIntermediate(TcpMTProxy):
    packet_codec = IntermediatePacketCodec

class ConnectionTcpMTProxyRandomizedIntermediate(TcpMTProxy):
    packet_codec = RandomizedIntermediatePacketCodec
