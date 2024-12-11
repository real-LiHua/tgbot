import subprocess
from .logging import get_logger as get_logger
from _typeshed import Incomplete
from io import StringIO
from pathlib import Path
from typing import Generator, IO

logger: Incomplete

def capture_output() -> Generator[StringIO, None, None]: ...
def run_subprocess(command: str | list[str], folder: str | Path | None = None, check: bool = True, **kwargs) -> subprocess.CompletedProcess: ...
def run_interactive_subprocess(command: str | list[str], folder: str | Path | None = None, **kwargs) -> Generator[tuple[IO[str], IO[str]], None, None]: ...
