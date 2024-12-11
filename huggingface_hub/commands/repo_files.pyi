import abc
from _typeshed import Incomplete
from argparse import _SubParsersAction
from huggingface_hub import logging as logging
from huggingface_hub.commands import BaseHuggingfaceCLICommand as BaseHuggingfaceCLICommand
from huggingface_hub.hf_api import HfApi as HfApi

logger: Incomplete

class DeleteFilesSubCommand:
    args: Incomplete
    repo_id: Incomplete
    repo_type: Incomplete
    revision: Incomplete
    api: Incomplete
    patterns: Incomplete
    commit_message: Incomplete
    commit_description: Incomplete
    create_pr: Incomplete
    token: Incomplete
    def __init__(self, args) -> None: ...
    def run(self) -> None: ...

class RepoFilesCommand(BaseHuggingfaceCLICommand, metaclass=abc.ABCMeta):
    @staticmethod
    def register_subcommand(parser: _SubParsersAction): ...
