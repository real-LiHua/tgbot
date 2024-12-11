from . import constants as constants
from .errors import EntryNotFoundError as EntryNotFoundError
from .utils import SoftTemporaryDirectory as SoftTemporaryDirectory, logging as logging, validate_hf_hub_args as validate_hf_hub_args
from _typeshed import Incomplete
from huggingface_hub.file_download import hf_hub_download as hf_hub_download
from huggingface_hub.hf_api import upload_file as upload_file
from huggingface_hub.repocard_data import CardData as CardData, DatasetCardData as DatasetCardData, EvalResult as EvalResult, ModelCardData as ModelCardData, SpaceCardData as SpaceCardData, eval_results_to_model_index as eval_results_to_model_index, model_index_to_eval_results as model_index_to_eval_results
from huggingface_hub.utils import get_session as get_session, is_jinja_available as is_jinja_available, yaml_dump as yaml_dump
from pathlib import Path
from typing import Any

logger: Incomplete
TEMPLATE_MODELCARD_PATH: Incomplete
TEMPLATE_DATASETCARD_PATH: Incomplete
REGEX_YAML_BLOCK: Incomplete

class RepoCard:
    card_data_class = CardData
    default_template_path = TEMPLATE_MODELCARD_PATH
    repo_type: str
    ignore_metadata_errors: Incomplete
    def __init__(self, content: str, ignore_metadata_errors: bool = False) -> None: ...
    @property
    def content(self): ...
    text: Incomplete
    data: Incomplete
    @content.setter
    def content(self, content: str): ...
    def save(self, filepath: Path | str): ...
    @classmethod
    def load(cls, repo_id_or_path: str | Path, repo_type: str | None = None, token: str | None = None, ignore_metadata_errors: bool = False): ...
    def validate(self, repo_type: str | None = None): ...
    def push_to_hub(self, repo_id: str, token: str | None = None, repo_type: str | None = None, commit_message: str | None = None, commit_description: str | None = None, revision: str | None = None, create_pr: bool | None = None, parent_commit: str | None = None): ...
    @classmethod
    def from_template(cls, card_data: CardData, template_path: str | None = None, template_str: str | None = None, **template_kwargs): ...

class ModelCard(RepoCard):
    card_data_class = ModelCardData
    default_template_path = TEMPLATE_MODELCARD_PATH
    repo_type: str
    @classmethod
    def from_template(cls, card_data: ModelCardData, template_path: str | None = None, template_str: str | None = None, **template_kwargs): ...

class DatasetCard(RepoCard):
    card_data_class = DatasetCardData
    default_template_path = TEMPLATE_DATASETCARD_PATH
    repo_type: str
    @classmethod
    def from_template(cls, card_data: DatasetCardData, template_path: str | None = None, template_str: str | None = None, **template_kwargs): ...

class SpaceCard(RepoCard):
    card_data_class = SpaceCardData
    default_template_path = TEMPLATE_MODELCARD_PATH
    repo_type: str

def metadata_load(local_path: str | Path) -> dict | None: ...
def metadata_save(local_path: str | Path, data: dict) -> None: ...
def metadata_eval_result(*, model_pretty_name: str, task_pretty_name: str, task_id: str, metrics_pretty_name: str, metrics_id: str, metrics_value: Any, dataset_pretty_name: str, dataset_id: str, metrics_config: str | None = None, metrics_verified: bool = False, dataset_config: str | None = None, dataset_split: str | None = None, dataset_revision: str | None = None, metrics_verification_token: str | None = None) -> dict: ...
def metadata_update(repo_id: str, metadata: dict, *, repo_type: str | None = None, overwrite: bool = False, token: str | None = None, commit_message: str | None = None, commit_description: str | None = None, revision: str | None = None, create_pr: bool = False, parent_commit: str | None = None) -> str: ...
