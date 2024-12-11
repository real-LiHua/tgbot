from ._commit_scheduler import CommitScheduler as CommitScheduler
from .errors import EntryNotFoundError as EntryNotFoundError
from .repocard import ModelCard as ModelCard
from .utils import experimental as experimental
from _typeshed import Incomplete
from tensorboardX import SummaryWriter

is_summary_writer_available: bool
SummaryWriter = object

class HFSummaryWriter(SummaryWriter):
    def __new__(cls, *args, **kwargs) -> HFSummaryWriter: ...
    scheduler: Incomplete
    repo_id: Incomplete
    repo_type: Incomplete
    repo_revision: Incomplete
    def __init__(self, repo_id: str, *, logdir: str | None = None, commit_every: int | float = 5, squash_history: bool = False, repo_type: str | None = None, repo_revision: str | None = None, repo_private: bool = False, path_in_repo: str | None = 'tensorboard', repo_allow_patterns: list[str] | str | None = '*.tfevents.*', repo_ignore_patterns: list[str] | str | None = None, token: str | None = None, **kwargs) -> None: ...
    def __exit__(self, exc_type: type[BaseException] | None, exc_val: BaseException | None, exc_tb: types.TracebackType | None) -> None: ...
