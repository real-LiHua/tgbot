from _typeshed import Incomplete
from typing import Callable, Generator, Iterable, TypeVar

T = TypeVar('T')
DEFAULT_IGNORE_PATTERNS: Incomplete
FORBIDDEN_FOLDERS: Incomplete

def filter_repo_objects(items: Iterable[T], *, allow_patterns: list[str] | str | None = None, ignore_patterns: list[str] | str | None = None, key: Callable[[T], str] | None = None) -> Generator[T, None, None]: ...
