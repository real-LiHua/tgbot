import enum
from . import constants as constants
from ._commit_api import CommitOperationAdd as CommitOperationAdd, UploadInfo as UploadInfo
from ._local_folder import LocalUploadFileMetadata as LocalUploadFileMetadata, LocalUploadFilePaths as LocalUploadFilePaths, get_local_upload_paths as get_local_upload_paths, read_upload_metadata as read_upload_metadata
from .constants import DEFAULT_REVISION as DEFAULT_REVISION, REPO_TYPES as REPO_TYPES
from .hf_api import HfApi as HfApi
from .utils import DEFAULT_IGNORE_PATTERNS as DEFAULT_IGNORE_PATTERNS, filter_repo_objects as filter_repo_objects, tqdm as tqdm
from .utils.sha import sha_fileobj as sha_fileobj
from _typeshed import Incomplete
from pathlib import Path

logger: Incomplete
WAITING_TIME_IF_NO_TASKS: int
MAX_NB_REGULAR_FILES_PER_COMMIT: int
MAX_NB_LFS_FILES_PER_COMMIT: int

def upload_large_folder_internal(api: HfApi, repo_id: str, folder_path: str | Path, *, repo_type: str, revision: str | None = None, private: bool = False, allow_patterns: list[str] | str | None = None, ignore_patterns: list[str] | str | None = None, num_workers: int | None = None, print_report: bool = True, print_report_every: int = 60): ...

class WorkerJob(enum.Enum):
    SHA256 = ...
    GET_UPLOAD_MODE = ...
    PREUPLOAD_LFS = ...
    COMMIT = ...
    WAIT = ...
JOB_ITEM_T = tuple[LocalUploadFilePaths, LocalUploadFileMetadata]

class LargeUploadStatus:
    items: Incomplete
    queue_sha256: Incomplete
    queue_get_upload_mode: Incomplete
    queue_preupload_lfs: Incomplete
    queue_commit: Incomplete
    lock: Incomplete
    nb_workers_sha256: int
    nb_workers_get_upload_mode: int
    nb_workers_preupload_lfs: int
    nb_workers_commit: int
    nb_workers_waiting: int
    last_commit_attempt: Incomplete
    def __init__(self, items: list[JOB_ITEM_T]) -> None: ...
    def current_report(self) -> str: ...
    def is_done(self) -> bool: ...

class HackyCommitOperationAdd(CommitOperationAdd):
    path_or_fileobj: Incomplete
    def __post_init__(self) -> None: ...
