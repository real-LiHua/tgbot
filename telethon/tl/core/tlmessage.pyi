from .. import TLObject as TLObject
from _typeshed import Incomplete

class TLMessage(TLObject):
    SIZE_OVERHEAD: int
    msg_id: Incomplete
    seq_no: Incomplete
    obj: Incomplete
    def __init__(self, msg_id, seq_no, obj) -> None: ...
    def to_dict(self): ...
