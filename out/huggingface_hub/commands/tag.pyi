import abc
from ..errors import HfHubHTTPError as HfHubHTTPError, RepositoryNotFoundError as RepositoryNotFoundError, RevisionNotFoundError as RevisionNotFoundError
from ._cli_utils import ANSI as ANSI
from _typeshed import Incomplete
from argparse import Namespace, _SubParsersAction
from huggingface_hub.commands import BaseHuggingfaceCLICommand as BaseHuggingfaceCLICommand
from huggingface_hub.constants import REPO_TYPES as REPO_TYPES
from huggingface_hub.hf_api import HfApi as HfApi

class TagCommands(BaseHuggingfaceCLICommand, metaclass=abc.ABCMeta):
    @staticmethod
    def register_subcommand(parser: _SubParsersAction): ...

def handle_commands(args: Namespace): ...

class TagCommand:
    args: Incomplete
    api: Incomplete
    repo_id: Incomplete
    repo_type: Incomplete
    def __init__(self, args: Namespace) -> None: ...

class TagCreateCommand(TagCommand):
    def run(self) -> None: ...

class TagListCommand(TagCommand):
    def run(self) -> None: ...

class TagDeleteCommand(TagCommand):
    def run(self) -> None: ...
