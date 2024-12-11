import abc
from .._login import NOTEBOOK_LOGIN_PASSWORD_HTML as NOTEBOOK_LOGIN_PASSWORD_HTML, NOTEBOOK_LOGIN_TOKEN_HTML_END as NOTEBOOK_LOGIN_TOKEN_HTML_END, NOTEBOOK_LOGIN_TOKEN_HTML_START as NOTEBOOK_LOGIN_TOKEN_HTML_START, auth_list as auth_list, auth_switch as auth_switch, login as login, logout as logout, notebook_login as notebook_login
from ..utils import get_stored_tokens as get_stored_tokens, get_token as get_token, logging as logging
from ._cli_utils import ANSI as ANSI
from _typeshed import Incomplete
from argparse import _SubParsersAction
from huggingface_hub.commands import BaseHuggingfaceCLICommand as BaseHuggingfaceCLICommand
from huggingface_hub.constants import ENDPOINT as ENDPOINT, REPO_TYPES as REPO_TYPES, REPO_TYPES_URL_PREFIXES as REPO_TYPES_URL_PREFIXES, SPACES_SDK_TYPES as SPACES_SDK_TYPES
from huggingface_hub.hf_api import HfApi as HfApi

logger: Incomplete

class UserCommands(BaseHuggingfaceCLICommand, metaclass=abc.ABCMeta):
    @staticmethod
    def register_subcommand(parser: _SubParsersAction): ...

class BaseUserCommand:
    args: Incomplete
    def __init__(self, args) -> None: ...

class LoginCommand(BaseUserCommand):
    def run(self) -> None: ...

class LogoutCommand(BaseUserCommand):
    def run(self) -> None: ...

class AuthSwitchCommand(BaseUserCommand):
    def run(self) -> None: ...

class AuthListCommand(BaseUserCommand):
    def run(self) -> None: ...

class WhoamiCommand(BaseUserCommand):
    def run(self) -> None: ...

class RepoCreateCommand(BaseUserCommand):
    def run(self) -> None: ...
