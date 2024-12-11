from . import constants as constants
from .errors import EntryNotFoundError as EntryNotFoundError, HfHubHTTPError as HfHubHTTPError
from .file_download import hf_hub_download as hf_hub_download
from .hf_api import HfApi as HfApi
from .repocard import ModelCard as ModelCard, ModelCardData as ModelCardData
from .utils import SoftTemporaryDirectory as SoftTemporaryDirectory, is_jsonable as is_jsonable, is_safetensors_available as is_safetensors_available, is_simple_optional_type as is_simple_optional_type, is_torch_available as is_torch_available, logging as logging, unwrap_simple_optional_type as unwrap_simple_optional_type, validate_hf_hub_args as validate_hf_hub_args
from _typeshed import DataclassInstance, Incomplete
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Callable, TypeVar

logger: Incomplete
T = TypeVar('T', bound='ModelHubMixin')
ARGS_T = TypeVar('ARGS_T')
ENCODER_T = Callable[[ARGS_T], Any]
DECODER_T = Callable[[Any], ARGS_T]
CODER_T = tuple[ENCODER_T, DECODER_T]
DEFAULT_MODEL_CARD: str

@dataclass
class MixinInfo:
    model_card_template: str
    model_card_data: ModelCardData
    repo_url: str | None = ...
    docs_url: str | None = ...
    def __init__(self, model_card_template, model_card_data, repo_url=..., docs_url=...) -> None: ...

class ModelHubMixin:
    def __init_subclass__(cls, *, repo_url: str | None = None, docs_url: str | None = None, model_card_template: str = ..., language: list[str] | None = None, library_name: str | None = None, license: str | None = None, license_name: str | None = None, license_link: str | None = None, pipeline_tag: str | None = None, tags: list[str] | None = None, coders: dict[type, CODER_T] | None = None, languages: list[str] | None = None) -> None: ...
    def __new__(cls, *args, **kwargs) -> ModelHubMixin: ...
    def save_pretrained(self, save_directory: str | Path, *, config: dict | DataclassInstance | None = None, repo_id: str | None = None, push_to_hub: bool = False, model_card_kwargs: dict[str, Any] | None = None, **push_to_hub_kwargs) -> str | None: ...
    @classmethod
    def from_pretrained(cls, pretrained_model_name_or_path: str | Path, *, force_download: bool = False, resume_download: bool | None = None, proxies: dict | None = None, token: str | bool | None = None, cache_dir: str | Path | None = None, local_files_only: bool = False, revision: str | None = None, **model_kwargs) -> T: ...
    def push_to_hub(self, repo_id: str, *, config: dict | DataclassInstance | None = None, commit_message: str = 'Push model using huggingface_hub.', private: bool = False, token: str | None = None, branch: str | None = None, create_pr: bool | None = None, allow_patterns: list[str] | str | None = None, ignore_patterns: list[str] | str | None = None, delete_patterns: list[str] | str | None = None, model_card_kwargs: dict[str, Any] | None = None) -> str: ...
    def generate_model_card(self, *args, **kwargs) -> ModelCard: ...

class PyTorchModelHubMixin(ModelHubMixin):
    def __init_subclass__(cls, *args, tags: list[str] | None = None, **kwargs) -> None: ...
