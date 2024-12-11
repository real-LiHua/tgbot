from ...tl.tlobject import TLObject as TLObject
from ...tl.types import TypeChat as TypeChat, TypeContact as TypeContact, TypeContactBirthday as TypeContactBirthday, TypeImportedContact as TypeImportedContact, TypePeer as TypePeer, TypePeerBlocked as TypePeerBlocked, TypePopularContact as TypePopularContact, TypeTopPeerCategoryPeers as TypeTopPeerCategoryPeers, TypeUser as TypeUser
from _typeshed import Incomplete
from datetime import datetime as datetime

class Blocked(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    blocked: Incomplete
    chats: Incomplete
    users: Incomplete
    def __init__(self, blocked: list['TypePeerBlocked'], chats: list['TypeChat'], users: list['TypeUser']) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class BlockedSlice(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    count: Incomplete
    blocked: Incomplete
    chats: Incomplete
    users: Incomplete
    def __init__(self, count: int, blocked: list['TypePeerBlocked'], chats: list['TypeChat'], users: list['TypeUser']) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class ContactBirthdays(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    contacts: Incomplete
    users: Incomplete
    def __init__(self, contacts: list['TypeContactBirthday'], users: list['TypeUser']) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class Contacts(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    contacts: Incomplete
    saved_count: Incomplete
    users: Incomplete
    def __init__(self, contacts: list['TypeContact'], saved_count: int, users: list['TypeUser']) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class ContactsNotModified(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class Found(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    my_results: Incomplete
    results: Incomplete
    chats: Incomplete
    users: Incomplete
    def __init__(self, my_results: list['TypePeer'], results: list['TypePeer'], chats: list['TypeChat'], users: list['TypeUser']) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class ImportedContacts(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    imported: Incomplete
    popular_invites: Incomplete
    retry_contacts: Incomplete
    users: Incomplete
    def __init__(self, imported: list['TypeImportedContact'], popular_invites: list['TypePopularContact'], retry_contacts: list[int], users: list['TypeUser']) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class ResolvedPeer(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    peer: Incomplete
    chats: Incomplete
    users: Incomplete
    def __init__(self, peer: TypePeer, chats: list['TypeChat'], users: list['TypeUser']) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class TopPeers(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    categories: Incomplete
    chats: Incomplete
    users: Incomplete
    def __init__(self, categories: list['TypeTopPeerCategoryPeers'], chats: list['TypeChat'], users: list['TypeUser']) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class TopPeersDisabled(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class TopPeersNotModified(TLObject):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...
