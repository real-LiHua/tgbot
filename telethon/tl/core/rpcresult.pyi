from .. import TLObject as TLObject
from ..types import RpcError as RpcError
from .gzippacked import GzipPacked as GzipPacked
from _typeshed import Incomplete

class RpcResult(TLObject):
    CONSTRUCTOR_ID: int
    req_msg_id: Incomplete
    body: Incomplete
    error: Incomplete
    def __init__(self, req_msg_id, body, error) -> None: ...
    @classmethod
    def from_reader(cls, reader): ...
    def to_dict(self): ...
