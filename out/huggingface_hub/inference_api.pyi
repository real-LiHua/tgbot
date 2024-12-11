from . import constants as constants
from .hf_api import HfApi as HfApi
from .utils import build_hf_headers as build_hf_headers, get_session as get_session, is_pillow_available as is_pillow_available, logging as logging, validate_hf_hub_args as validate_hf_hub_args
from _typeshed import Incomplete
from typing import Any

logger: Incomplete
ALL_TASKS: Incomplete

class InferenceApi:
    options: Incomplete
    headers: Incomplete
    task: Incomplete
    api_url: Incomplete
    def __init__(self, repo_id: str, task: str | None = None, token: str | None = None, gpu: bool = False) -> None: ...
    def __call__(self, inputs: str | dict | list[str] | list[list[str]] | None = None, params: dict | None = None, data: bytes | None = None, raw_response: bool = False) -> Any: ...
