from .. import constants as constants
from ._auth import get_token as get_token
from ._runtime import get_fastai_version as get_fastai_version, get_fastcore_version as get_fastcore_version, get_hf_hub_version as get_hf_hub_version, get_python_version as get_python_version, get_tf_version as get_tf_version, get_torch_version as get_torch_version, is_fastai_available as is_fastai_available, is_fastcore_available as is_fastcore_available, is_tf_available as is_tf_available, is_torch_available as is_torch_available
from ._validators import validate_hf_hub_args as validate_hf_hub_args
from huggingface_hub.errors import LocalTokenNotFoundError as LocalTokenNotFoundError

def build_hf_headers(*, token: bool | str | None = None, is_write_action: bool = False, library_name: str | None = None, library_version: str | None = None, user_agent: dict | str | None = None, headers: dict[str, str] | None = None) -> dict[str, str]: ...
def get_token_to_send(token: bool | str | None) -> str | None: ...
