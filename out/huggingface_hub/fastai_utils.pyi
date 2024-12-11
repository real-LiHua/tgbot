from .utils import logging as logging, validate_hf_hub_args as validate_hf_hub_args
from _typeshed import Incomplete
from huggingface_hub import constants as constants, snapshot_download as snapshot_download
from huggingface_hub.hf_api import HfApi as HfApi
from huggingface_hub.utils import SoftTemporaryDirectory as SoftTemporaryDirectory, get_fastai_version as get_fastai_version, get_fastcore_version as get_fastcore_version, get_python_version as get_python_version

logger: Incomplete
README_TEMPLATE: str
PYPROJECT_TEMPLATE: Incomplete

def from_pretrained_fastai(repo_id: str, revision: str | None = None): ...
def push_to_hub_fastai(learner, *, repo_id: str, commit_message: str = 'Push FastAI model using huggingface_hub.', private: bool = False, token: str | None = None, config: dict | None = None, branch: str | None = None, create_pr: bool | None = None, allow_patterns: list[str] | str | None = None, ignore_patterns: list[str] | str | None = None, delete_patterns: list[str] | str | None = None, api_endpoint: str | None = None): ...
