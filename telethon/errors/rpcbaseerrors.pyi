from ..tl import functions as functions
from _typeshed import Incomplete

class RPCError(Exception):
    code: Incomplete
    message: Incomplete
    request: Incomplete
    def __init__(self, request, message, code: Incomplete | None = None) -> None: ...
    def __reduce__(self): ...

class InvalidDCError(RPCError):
    code: int
    message: str

class BadRequestError(RPCError):
    code: int
    message: str

class UnauthorizedError(RPCError):
    code: int
    message: str

class ForbiddenError(RPCError):
    code: int
    message: str

class NotFoundError(RPCError):
    code: int
    message: str

class AuthKeyError(RPCError):
    code: int
    message: str

class FloodError(RPCError):
    code: int
    message: str

class ServerError(RPCError):
    code: int
    message: str

class TimedOutError(RPCError):
    code: int
    message: str
BotTimeout = TimedOutError
base_errors: Incomplete
