from . import logging as logging
from ..commands._cli_utils import tabulate as tabulate
from ..constants import HF_HUB_CACHE as HF_HUB_CACHE
from _typeshed import Incomplete
from dataclasses import dataclass
from huggingface_hub.errors import CacheNotFound as CacheNotFound, CorruptedCacheException as CorruptedCacheException
from pathlib import Path

logger: Incomplete
REPO_TYPE_T: Incomplete
FILES_TO_IGNORE: Incomplete

@dataclass(frozen=True)
class CachedFileInfo:
    file_name: str
    file_path: Path
    blob_path: Path
    size_on_disk: int
    blob_last_accessed: float
    blob_last_modified: float
    @property
    def blob_last_accessed_str(self) -> str: ...
    @property
    def blob_last_modified_str(self) -> str: ...
    @property
    def size_on_disk_str(self) -> str: ...
    def __init__(self, file_name, file_path, blob_path, size_on_disk, blob_last_accessed, blob_last_modified) -> None: ...

@dataclass(frozen=True)
class CachedRevisionInfo:
    commit_hash: str
    snapshot_path: Path
    size_on_disk: int
    files: frozenset[CachedFileInfo]
    refs: frozenset[str]
    last_modified: float
    @property
    def last_modified_str(self) -> str: ...
    @property
    def size_on_disk_str(self) -> str: ...
    @property
    def nb_files(self) -> int: ...
    def __init__(self, commit_hash, snapshot_path, size_on_disk, files, refs, last_modified) -> None: ...

@dataclass(frozen=True)
class CachedRepoInfo:
    repo_id: str
    repo_type: REPO_TYPE_T
    repo_path: Path
    size_on_disk: int
    nb_files: int
    revisions: frozenset[CachedRevisionInfo]
    last_accessed: float
    last_modified: float
    @property
    def last_accessed_str(self) -> str: ...
    @property
    def last_modified_str(self) -> str: ...
    @property
    def size_on_disk_str(self) -> str: ...
    @property
    def refs(self) -> dict[str, CachedRevisionInfo]: ...
    def __init__(self, repo_id, repo_type, repo_path, size_on_disk, nb_files, revisions, last_accessed, last_modified) -> None: ...

@dataclass(frozen=True)
class DeleteCacheStrategy:
    expected_freed_size: int
    blobs: frozenset[Path]
    refs: frozenset[Path]
    repos: frozenset[Path]
    snapshots: frozenset[Path]
    @property
    def expected_freed_size_str(self) -> str: ...
    def execute(self) -> None: ...
    def __init__(self, expected_freed_size, blobs, refs, repos, snapshots) -> None: ...

@dataclass(frozen=True)
class HFCacheInfo:
    size_on_disk: int
    repos: frozenset[CachedRepoInfo]
    warnings: list[CorruptedCacheException]
    @property
    def size_on_disk_str(self) -> str: ...
    def delete_revisions(self, *revisions: str) -> DeleteCacheStrategy: ...
    def export_as_table(self, *, verbosity: int = 0) -> str: ...
    def __init__(self, size_on_disk, repos, warnings) -> None: ...

def scan_cache_dir(cache_dir: str | Path | None = None) -> HFCacheInfo: ...
