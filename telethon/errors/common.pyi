from ..tl import TLRequest as TLRequest
from _typeshed import Incomplete

class ReadCancelledError(Exception):
    def __init__(self) -> None: ...

class TypeNotFoundError(Exception):
    invalid_constructor_id: Incomplete
    remaining: Incomplete
    def __init__(self, invalid_constructor_id, remaining) -> None: ...

class InvalidChecksumError(Exception):
    checksum: Incomplete
    valid_checksum: Incomplete
    def __init__(self, checksum, valid_checksum) -> None: ...

class InvalidBufferError(BufferError):
    payload: Incomplete
    code: Incomplete
    def __init__(self, payload) -> None: ...

class AuthKeyNotFound(Exception):
    def __init__(self) -> None: ...

class SecurityError(Exception):
    def __init__(self, *args) -> None: ...

class CdnFileTamperedError(SecurityError):
    def __init__(self) -> None: ...

class AlreadyInConversationError(Exception):
    def __init__(self) -> None: ...

class BadMessageError(Exception):
    ErrorMessages: Incomplete
    code: Incomplete
    def __init__(self, request, code) -> None: ...

class MultiError(Exception):
    exceptions: Incomplete
    results: Incomplete
    requests: Incomplete
    def __new__(cls, exceptions, result, requests): ...
