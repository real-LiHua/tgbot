from .hf_api import CommitInfo as CommitInfo, CommitOperationAdd as CommitOperationAdd, DEFAULT_IGNORE_PATTERNS as DEFAULT_IGNORE_PATTERNS, HfApi as HfApi
from .utils import filter_repo_objects as filter_repo_objects
from _typeshed import Incomplete
from concurrent.futures import Future
from dataclasses import dataclass
from io import BytesIO
from pathlib import Path

logger: Incomplete

@dataclass(frozen=True)
class _FileToUpload:
    local_path: Path
    path_in_repo: str
    size_limit: int
    last_modified: float
    def __init__(self, local_path, path_in_repo, size_limit, last_modified) -> None: ...

class CommitScheduler:
    api: Incomplete
    folder_path: Incomplete
    path_in_repo: Incomplete
    allow_patterns: Incomplete
    ignore_patterns: Incomplete
    repo_id: Incomplete
    repo_type: Incomplete
    revision: Incomplete
    token: Incomplete
    last_uploaded: Incomplete
    lock: Incomplete
    every: Incomplete
    squash_history: Incomplete
    def __init__(self, *, repo_id: str, folder_path: str | Path, every: int | float = 5, path_in_repo: str | None = None, repo_type: str | None = None, revision: str | None = None, private: bool = False, token: str | None = None, allow_patterns: list[str] | str | None = None, ignore_patterns: list[str] | str | None = None, squash_history: bool = False, hf_api: HfApi | None = None) -> None: ...
    def stop(self) -> None: ...
    def trigger(self) -> Future: ...
    def push_to_hub(self) -> CommitInfo | None: ...

class PartialFileIO(BytesIO):
    def __init__(self, file_path: str | Path, size_limit: int) -> None: ...
    def __del__(self) -> None: ...
    def __len__(self) -> int: ...
    def __getattribute__(self, name: str): ...
    def tell(self) -> int: ...
    def seek(self, __offset: int, /, __whence: int = ...) -> int: ...
    def read(self, /, __size: int | None = -1) -> bytes: ...
