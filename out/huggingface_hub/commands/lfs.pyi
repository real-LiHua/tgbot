import abc
from ..utils import get_session as get_session, hf_raise_for_status as hf_raise_for_status, logging as logging
from ..utils._lfs import SliceFileObj as SliceFileObj
from _typeshed import Incomplete
from argparse import _SubParsersAction
from huggingface_hub.commands import BaseHuggingfaceCLICommand as BaseHuggingfaceCLICommand
from huggingface_hub.lfs import LFS_MULTIPART_UPLOAD_COMMAND as LFS_MULTIPART_UPLOAD_COMMAND

logger: Incomplete

class LfsCommands(BaseHuggingfaceCLICommand, metaclass=abc.ABCMeta):
    @staticmethod
    def register_subcommand(parser: _SubParsersAction): ...

class LfsEnableCommand:
    args: Incomplete
    def __init__(self, args) -> None: ...
    def run(self) -> None: ...

def write_msg(msg: dict): ...
def read_msg() -> dict | None: ...

class LfsUploadCommand:
    args: Incomplete
    def __init__(self, args) -> None: ...
    def run(self) -> None: ...
