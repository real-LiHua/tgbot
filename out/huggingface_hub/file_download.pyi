from . import __version__ as __version__, constants as constants
from ._local_folder import get_local_download_paths as get_local_download_paths, read_download_metadata as read_download_metadata, write_download_metadata as write_download_metadata
from .constants import HUGGINGFACE_CO_URL_TEMPLATE as HUGGINGFACE_CO_URL_TEMPLATE, HUGGINGFACE_HUB_CACHE as HUGGINGFACE_HUB_CACHE
from .errors import EntryNotFoundError as EntryNotFoundError, FileMetadataError as FileMetadataError, GatedRepoError as GatedRepoError, LocalEntryNotFoundError as LocalEntryNotFoundError, RepositoryNotFoundError as RepositoryNotFoundError, RevisionNotFoundError as RevisionNotFoundError
from .utils import OfflineModeIsEnabled as OfflineModeIsEnabled, SoftTemporaryDirectory as SoftTemporaryDirectory, WeakFileLock as WeakFileLock, build_hf_headers as build_hf_headers, get_fastai_version as get_fastai_version, get_fastcore_version as get_fastcore_version, get_graphviz_version as get_graphviz_version, get_jinja_version as get_jinja_version, get_pydot_version as get_pydot_version, get_session as get_session, get_tf_version as get_tf_version, get_torch_version as get_torch_version, hf_raise_for_status as hf_raise_for_status, is_fastai_available as is_fastai_available, is_fastcore_available as is_fastcore_available, is_graphviz_available as is_graphviz_available, is_jinja_available as is_jinja_available, is_pydot_available as is_pydot_available, is_tf_available as is_tf_available, is_torch_available as is_torch_available, logging as logging, reset_sessions as reset_sessions, tqdm as tqdm, validate_hf_hub_args as validate_hf_hub_args
from .utils._typing import HTTP_METHOD_T as HTTP_METHOD_T
from .utils.sha import sha_fileobj as sha_fileobj
from _typeshed import Incomplete
from dataclasses import dataclass
from pathlib import Path
from typing import BinaryIO, Literal

logger: Incomplete
HEADER_FILENAME_PATTERN: Incomplete
REGEX_COMMIT_HASH: Incomplete
REGEX_SHA256: Incomplete

def are_symlinks_supported(cache_dir: str | Path | None = None) -> bool: ...

@dataclass(frozen=True)
class HfFileMetadata:
    commit_hash: str | None
    etag: str | None
    location: str
    size: int | None
    def __init__(self, commit_hash, etag, location, size) -> None: ...

def hf_hub_url(repo_id: str, filename: str, *, subfolder: str | None = None, repo_type: str | None = None, revision: str | None = None, endpoint: str | None = None) -> str: ...
def http_get(url: str, temp_file: BinaryIO, *, proxies: dict | None = None, resume_size: float = 0, headers: dict[str, str] | None = None, expected_size: int | None = None, displayed_filename: str | None = None, _nb_retries: int = 5, _tqdm_bar: tqdm | None = None) -> None: ...
def repo_folder_name(*, repo_id: str, repo_type: str) -> str: ...
def hf_hub_download(repo_id: str, filename: str, *, subfolder: str | None = None, repo_type: str | None = None, revision: str | None = None, library_name: str | None = None, library_version: str | None = None, cache_dir: str | Path | None = None, local_dir: str | Path | None = None, user_agent: dict | str | None = None, force_download: bool = False, proxies: dict | None = None, etag_timeout: float = ..., token: bool | str | None = None, local_files_only: bool = False, headers: dict[str, str] | None = None, endpoint: str | None = None, resume_download: bool | None = None, force_filename: str | None = None, local_dir_use_symlinks: bool | Literal['auto'] = 'auto') -> str: ...
def try_to_load_from_cache(repo_id: str, filename: str, cache_dir: str | Path | None = None, revision: str | None = None, repo_type: str | None = None) -> str | _CACHED_NO_EXIST_T | None: ...
def get_hf_file_metadata(url: str, token: bool | str | None = None, proxies: dict | None = None, timeout: float | None = ..., library_name: str | None = None, library_version: str | None = None, user_agent: dict | str | None = None, headers: dict[str, str] | None = None) -> HfFileMetadata: ...
