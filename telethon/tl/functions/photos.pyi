from ...tl.tlobject import TLObject as TLObject, TLRequest as TLRequest
from ...tl.types import TypeInputFile as TypeInputFile, TypeInputPhoto as TypeInputPhoto, TypeInputUser as TypeInputUser, TypeVideoSize as TypeVideoSize
from _typeshed import Incomplete
from datetime import datetime as datetime

class DeletePhotosRequest(TLRequest):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    id: Incomplete
    def __init__(self, id: list['TypeInputPhoto']) -> None: ...
    async def resolve(self, client, utils) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...
    @staticmethod
    def read_result(reader): ...

class GetUserPhotosRequest(TLRequest):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    user_id: Incomplete
    offset: Incomplete
    max_id: Incomplete
    limit: Incomplete
    def __init__(self, user_id: TypeInputUser, offset: int, max_id: int, limit: int) -> None: ...
    async def resolve(self, client, utils) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class UpdateProfilePhotoRequest(TLRequest):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    id: Incomplete
    fallback: Incomplete
    bot: Incomplete
    def __init__(self, id: TypeInputPhoto, fallback: bool | None = None, bot: TypeInputUser | None = None) -> None: ...
    async def resolve(self, client, utils) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class UploadContactProfilePhotoRequest(TLRequest):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    user_id: Incomplete
    suggest: Incomplete
    save: Incomplete
    file: Incomplete
    video: Incomplete
    video_start_ts: Incomplete
    video_emoji_markup: Incomplete
    def __init__(self, user_id: TypeInputUser, suggest: bool | None = None, save: bool | None = None, file: TypeInputFile | None = None, video: TypeInputFile | None = None, video_start_ts: float | None = None, video_emoji_markup: TypeVideoSize | None = None) -> None: ...
    async def resolve(self, client, utils) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...

class UploadProfilePhotoRequest(TLRequest):
    CONSTRUCTOR_ID: int
    SUBCLASS_OF_ID: int
    fallback: Incomplete
    bot: Incomplete
    file: Incomplete
    video: Incomplete
    video_start_ts: Incomplete
    video_emoji_markup: Incomplete
    def __init__(self, fallback: bool | None = None, bot: TypeInputUser | None = None, file: TypeInputFile | None = None, video: TypeInputFile | None = None, video_start_ts: float | None = None, video_emoji_markup: TypeVideoSize | None = None) -> None: ...
    async def resolve(self, client, utils) -> None: ...
    def to_dict(self): ...
    @classmethod
    def from_reader(cls, reader): ...
