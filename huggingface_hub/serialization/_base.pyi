from .. import logging as logging
from _typeshed import Incomplete
from dataclasses import dataclass
from typing import Any, Callable, TypeVar

TensorT = TypeVar('TensorT')
TensorSizeFn_T = Callable[[TensorT], int]
StorageIDFn_T = Callable[[TensorT], Any | None]
MAX_SHARD_SIZE: str
SIZE_UNITS: Incomplete
logger: Incomplete

@dataclass
class StateDictSplit:
    is_sharded: bool = ...
    metadata: dict[str, Any]
    filename_to_tensors: dict[str, list[str]]
    tensor_to_filename: dict[str, str]
    def __post_init__(self) -> None: ...
    def __init__(self, metadata, filename_to_tensors, tensor_to_filename) -> None: ...

def split_state_dict_into_shards_factory(state_dict: dict[str, TensorT], *, get_storage_size: TensorSizeFn_T, filename_pattern: str, get_storage_id: StorageIDFn_T = ..., max_shard_size: int | str = ...) -> StateDictSplit: ...
def parse_size_to_int(size_as_str: str) -> int: ...
