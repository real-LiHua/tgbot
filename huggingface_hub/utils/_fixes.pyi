from . import logging as logging
from .. import constants as constants
from _typeshed import Incomplete
from filelock import BaseFileLock as BaseFileLock
from pathlib import Path
from typing import Callable, Generator

logger: Incomplete
yaml_dump: Callable[..., str]

def SoftTemporaryDirectory(suffix: str | None = None, prefix: str | None = None, dir: Path | str | None = None, **kwargs) -> Generator[Path, None, None]: ...
def WeakFileLock(lock_file: str | Path) -> Generator[BaseFileLock, None, None]: ...
