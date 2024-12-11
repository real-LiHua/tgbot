from ...tl.tlobject import TLObject as TLObject, TLRequest as TLRequest
from ...tl.types import TypeInputFolderPeer as TypeInputFolderPeer
from _typeshed import Incomplete
from datetime import datetime as datetime

class EditPeerFoldersRequest(TLRequest):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    folder_peers: Incomplete
    def __init__(self, folder_peers: list['TypeInputFolderPeer']) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...
