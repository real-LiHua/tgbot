from . import constants as constants
from .errors import GatedRepoError as GatedRepoError, LocalEntryNotFoundError as LocalEntryNotFoundError, RepositoryNotFoundError as RepositoryNotFoundError, RevisionNotFoundError as RevisionNotFoundError
from .file_download import REGEX_COMMIT_HASH as REGEX_COMMIT_HASH, hf_hub_download as hf_hub_download, repo_folder_name as repo_folder_name
from .hf_api import DatasetInfo as DatasetInfo, HfApi as HfApi, ModelInfo as ModelInfo, SpaceInfo as SpaceInfo
from .utils import OfflineModeIsEnabled as OfflineModeIsEnabled, filter_repo_objects as filter_repo_objects, logging as logging, validate_hf_hub_args as validate_hf_hub_args
from _typeshed import Incomplete
from pathlib import Path
from tqdm.auto import tqdm as base_tqdm
from typing import Literal

logger: Incomplete

def snapshot_download(repo_id: str, *, repo_type: str | None = None, revision: str | None = None, cache_dir: str | Path | None = None, local_dir: str | Path | None = None, library_name: str | None = None, library_version: str | None = None, user_agent: dict | str | None = None, proxies: dict | None = None, etag_timeout: float = ..., force_download: bool = False, token: bool | str | None = None, local_files_only: bool = False, allow_patterns: list[str] | str | None = None, ignore_patterns: list[str] | str | None = None, max_workers: int = 8, tqdm_class: base_tqdm | None = None, headers: dict[str, str] | None = None, endpoint: str | None = None, local_dir_use_symlinks: bool | Literal['auto'] = 'auto', resume_download: bool | None = None) -> str: ...
