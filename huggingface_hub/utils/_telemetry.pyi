from . import build_hf_headers as build_hf_headers, get_session as get_session, hf_raise_for_status as hf_raise_for_status
from .. import constants as constants, logging as logging
from _typeshed import Incomplete

logger: Incomplete

def send_telemetry(topic: str, *, library_name: str | None = None, library_version: str | None = None, user_agent: dict | str | None = None) -> None: ...
