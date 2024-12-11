from ._cli_utils import ANSI as ANSI
from _typeshed import Incomplete
from argparse import Namespace, _SubParsersAction
from huggingface_hub import logging as logging
from huggingface_hub.commands import BaseHuggingfaceCLICommand as BaseHuggingfaceCLICommand
from huggingface_hub.hf_api import HfApi as HfApi
from huggingface_hub.utils import disable_progress_bars as disable_progress_bars

logger: Incomplete

class UploadLargeFolderCommand(BaseHuggingfaceCLICommand):
    @staticmethod
    def register_subcommand(parser: _SubParsersAction): ...
    repo_id: Incomplete
    local_path: Incomplete
    repo_type: Incomplete
    revision: Incomplete
    private: Incomplete
    include: Incomplete
    exclude: Incomplete
    api: Incomplete
    num_workers: Incomplete
    no_report: Incomplete
    no_bars: Incomplete
    def __init__(self, args: Namespace) -> None: ...
    def run(self) -> None: ...
