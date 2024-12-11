from ...crypto import AESModeCTR as AESModeCTR
from .connection import ObfuscatedConnection as ObfuscatedConnection
from .tcpabridged import AbridgedPacketCodec as AbridgedPacketCodec
from _typeshed import Incomplete

class ObfuscatedIO:
    header: Incomplete
    def __init__(self, connection) -> None: ...
    @staticmethod
    def init_header(packet_codec): ...
    async def readexactly(self, n): ...
    def write(self, data) -> None: ...

class ConnectionTcpObfuscated(ObfuscatedConnection):
    obfuscated_io = ObfuscatedIO
    packet_codec = AbridgedPacketCodec
