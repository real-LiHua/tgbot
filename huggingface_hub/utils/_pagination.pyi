from . import get_session as get_session, hf_raise_for_status as hf_raise_for_status, logging as logging
from _typeshed import Incomplete
from typing import Iterable

logger: Incomplete

def paginate(path: str, params: dict, headers: dict) -> Iterable: ...
