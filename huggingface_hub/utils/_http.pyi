import requests
from . import logging as logging
from .. import constants as constants
from ..errors import BadRequestError as BadRequestError, DisabledRepoError as DisabledRepoError, EntryNotFoundError as EntryNotFoundError, GatedRepoError as GatedRepoError, HfHubHTTPError as HfHubHTTPError, RepositoryNotFoundError as RepositoryNotFoundError, RevisionNotFoundError as RevisionNotFoundError
from ._fixes import JSONDecodeError as JSONDecodeError
from ._lfs import SliceFileObj as SliceFileObj
from ._typing import HTTP_METHOD_T as HTTP_METHOD_T
from _typeshed import Incomplete
from huggingface_hub.errors import OfflineModeIsEnabled as OfflineModeIsEnabled
from requests import Response as Response
from requests.adapters import HTTPAdapter
from requests.models import PreparedRequest as PreparedRequest

logger: Incomplete
X_AMZN_TRACE_ID: str
X_REQUEST_ID: str
REPO_API_REGEX: Incomplete

class UniqueRequestIdAdapter(HTTPAdapter):
    X_AMZN_TRACE_ID: str
    def add_headers(self, request, **kwargs) -> None: ...
    def send(self, request: PreparedRequest, *args, **kwargs) -> Response: ...

class OfflineAdapter(HTTPAdapter):
    def send(self, request: PreparedRequest, *args, **kwargs) -> Response: ...

BACKEND_FACTORY_T: Incomplete

def configure_http_backend(backend_factory: BACKEND_FACTORY_T = ...) -> None: ...
def get_session() -> requests.Session: ...
def reset_sessions() -> None: ...
def http_backoff(method: HTTP_METHOD_T, url: str, *, max_retries: int = 5, base_wait_time: float = 1, max_wait_time: float = 8, retry_on_exceptions: type[Exception] | tuple[type[Exception], ...] = ..., retry_on_status_codes: int | tuple[int, ...] = ..., **kwargs) -> Response: ...
def fix_hf_endpoint_in_url(url: str, endpoint: str | None) -> str: ...
def hf_raise_for_status(response: Response, endpoint_name: str | None = None) -> None: ...
