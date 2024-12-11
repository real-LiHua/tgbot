from ..constants import ENDPOINT as ENDPOINT
from ..utils import build_hf_headers as build_hf_headers, get_session as get_session, hf_raise_for_status as hf_raise_for_status, is_aiohttp_available as is_aiohttp_available, is_numpy_available as is_numpy_available, is_pillow_available as is_pillow_available
from ._generated.types import ChatCompletionStreamOutput as ChatCompletionStreamOutput, TextGenerationStreamOutput as TextGenerationStreamOutput
from _typeshed import Incomplete
from aiohttp import ClientResponse as ClientResponse, ClientSession as ClientSession
from dataclasses import dataclass
from huggingface_hub.errors import GenerationError as GenerationError, IncompleteGenerationError as IncompleteGenerationError, OverloadedError as OverloadedError, TextGenerationError as TextGenerationError, UnknownError as UnknownError, ValidationError as ValidationError
from pathlib import Path
from requests import HTTPError as HTTPError
from typing import BinaryIO, NoReturn

UrlT = str
PathT = str | Path
BinaryT = bytes | BinaryIO
ContentT = BinaryT | PathT | UrlT
TASKS_EXPECTING_IMAGES: Incomplete
logger: Incomplete

@dataclass
class ModelStatus:
    loaded: bool
    state: str
    compute_type: dict
    framework: str
    def __init__(self, loaded, state, compute_type, framework) -> None: ...

def raise_text_generation_error(http_error: HTTPError) -> NoReturn: ...
