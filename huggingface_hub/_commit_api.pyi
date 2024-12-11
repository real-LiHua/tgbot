from . import constants as constants
from .errors import EntryNotFoundError as EntryNotFoundError
from .file_download import hf_hub_url as hf_hub_url
from .hf_api import RepoFile as RepoFile
from .lfs import UploadInfo as UploadInfo, lfs_upload as lfs_upload, post_lfs_batch_info as post_lfs_batch_info
from .utils import FORBIDDEN_FOLDERS as FORBIDDEN_FOLDERS, chunk_iterable as chunk_iterable, get_session as get_session, hf_raise_for_status as hf_raise_for_status, logging as logging, sha as sha, tqdm_stream_file as tqdm_stream_file, validate_hf_hub_args as validate_hf_hub_args
from _typeshed import Incomplete
from dataclasses import dataclass
from pathlib import Path
from typing import BinaryIO, Iterator, Literal

logger: Incomplete
UploadMode: Incomplete
FETCH_LFS_BATCH_SIZE: int

@dataclass
class CommitOperationDelete:
    path_in_repo: str
    is_folder: bool | Literal['auto'] = ...
    def __post_init__(self) -> None: ...
    def __init__(self, path_in_repo, is_folder=...) -> None: ...

@dataclass
class CommitOperationCopy:
    src_path_in_repo: str
    path_in_repo: str
    src_revision: str | None = ...
    def __post_init__(self) -> None: ...
    def __init__(self, src_path_in_repo, path_in_repo, src_revision=...) -> None: ...

@dataclass
class CommitOperationAdd:
    path_in_repo: str
    path_or_fileobj: str | Path | bytes | BinaryIO
    upload_info: UploadInfo = ...
    def __post_init__(self) -> None: ...
    def as_file(self, with_tqdm: bool = False) -> Iterator[BinaryIO]: ...
    def b64content(self) -> bytes: ...
    def __init__(self, path_in_repo, path_or_fileobj) -> None: ...
CommitOperation = CommitOperationAdd | CommitOperationCopy | CommitOperationDelete
