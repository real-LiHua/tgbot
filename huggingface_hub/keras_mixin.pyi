from . import constants as constants
from .hf_api import HfApi as HfApi
from .utils import SoftTemporaryDirectory as SoftTemporaryDirectory, logging as logging, validate_hf_hub_args as validate_hf_hub_args
from .utils._typing import CallableT as CallableT
from _typeshed import Incomplete
from huggingface_hub import ModelHubMixin as ModelHubMixin, snapshot_download as snapshot_download
from huggingface_hub.utils import get_tf_version as get_tf_version, is_graphviz_available as is_graphviz_available, is_pydot_available as is_pydot_available, is_tf_available as is_tf_available, yaml_dump as yaml_dump
from pathlib import Path
from typing import Any

logger: Incomplete
keras: Incomplete

def save_pretrained_keras(model, save_directory: str | Path, config: dict[str, Any] | None = None, include_optimizer: bool = False, plot_model: bool = True, tags: list | str | None = None, **model_save_kwargs): ...
def from_pretrained_keras(*args, **kwargs) -> KerasModelHubMixin: ...
def push_to_hub_keras(model, repo_id: str, *, config: dict | None = None, commit_message: str = 'Push Keras model using huggingface_hub.', private: bool = False, api_endpoint: str | None = None, token: str | None = None, branch: str | None = None, create_pr: bool | None = None, allow_patterns: list[str] | str | None = None, ignore_patterns: list[str] | str | None = None, delete_patterns: list[str] | str | None = None, log_dir: str | None = None, include_optimizer: bool = False, tags: list | str | None = None, plot_model: bool = True, **model_save_kwargs): ...

class KerasModelHubMixin(ModelHubMixin): ...
