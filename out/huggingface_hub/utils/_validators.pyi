from ._typing import CallableT as CallableT
from _typeshed import Incomplete
from huggingface_hub.errors import HFValidationError as HFValidationError
from typing import Any

REPO_ID_REGEX: Incomplete

def validate_hf_hub_args(fn: CallableT) -> CallableT: ...
def validate_repo_id(repo_id: str) -> None: ...
def smoothly_deprecate_use_auth_token(fn_name: str, has_token: bool, kwargs: dict[str, Any]) -> dict[str, Any]: ...
