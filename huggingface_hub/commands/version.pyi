from . import BaseHuggingfaceCLICommand as BaseHuggingfaceCLICommand
from _typeshed import Incomplete
from argparse import _SubParsersAction
from huggingface_hub import __version__ as __version__

class VersionCommand(BaseHuggingfaceCLICommand):
    args: Incomplete
    def __init__(self, args) -> None: ...
    @staticmethod
    def register_subcommand(parser: _SubParsersAction): ...
    def run(self) -> None: ...
