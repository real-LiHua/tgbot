from typing import Iterable, TypeVar

T = TypeVar('T')

def chunk_iterable(iterable: Iterable[T], chunk_size: int) -> Iterable[Iterable[T]]: ...
