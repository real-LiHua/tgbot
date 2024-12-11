from ._commit_api import CommitOperationAdd as CommitOperationAdd
from .utils import build_hf_headers as build_hf_headers, fix_hf_endpoint_in_url as fix_hf_endpoint_in_url, get_session as get_session, hf_raise_for_status as hf_raise_for_status, http_backoff as http_backoff, logging as logging, tqdm as tqdm, validate_hf_hub_args as validate_hf_hub_args
from .utils._lfs import SliceFileObj as SliceFileObj
from .utils.sha import sha256 as sha256, sha_fileobj as sha_fileobj
from _typeshed import Incomplete
from dataclasses import dataclass
from huggingface_hub import constants as constants
from typing import BinaryIO, Iterable, TypedDict

logger: Incomplete
OID_REGEX: Incomplete
LFS_MULTIPART_UPLOAD_COMMAND: str
LFS_HEADERS: Incomplete

@dataclass
class UploadInfo:
    sha256: bytes
    size: int
    sample: bytes
    @classmethod
    def from_path(cls, path: str): ...
    @classmethod
    def from_bytes(cls, data: bytes): ...
    @classmethod
    def from_fileobj(cls, fileobj: BinaryIO): ...
    def __init__(self, sha256, size, sample) -> None: ...

def post_lfs_batch_info(upload_infos: Iterable[UploadInfo], token: str | None, repo_type: str, repo_id: str, revision: str | None = None, endpoint: str | None = None, headers: dict[str, str] | None = None) -> tuple[list[dict], list[dict]]: ...

class PayloadPartT(TypedDict):
    partNumber: int
    etag: str

class CompletionPayloadT(TypedDict):
    oid: str
    parts: list[PayloadPartT]

def lfs_upload(operation: CommitOperationAdd, lfs_batch_action: dict, token: str | None = None, headers: dict[str, str] | None = None, endpoint: str | None = None) -> None: ...
