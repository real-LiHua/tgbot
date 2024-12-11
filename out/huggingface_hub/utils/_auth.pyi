from .. import constants as constants
from ._runtime import is_colab_enterprise as is_colab_enterprise, is_google_colab as is_google_colab
from _typeshed import Incomplete

logger: Incomplete

def get_token() -> str | None: ...
def get_stored_tokens() -> dict[str, str]: ...
