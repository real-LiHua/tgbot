from _typeshed import Incomplete
from dataclasses import dataclass

FILENAME_T = str
TENSOR_NAME_T = str
DTYPE_T: Incomplete

@dataclass
class TensorInfo:
    dtype: DTYPE_T
    shape: list[int]
    data_offsets: tuple[int, int]
    parameter_count: int = ...
    def __post_init__(self) -> None: ...
    def __init__(self, dtype, shape, data_offsets) -> None: ...

@dataclass
class SafetensorsFileMetadata:
    metadata: dict[str, str]
    tensors: dict[TENSOR_NAME_T, TensorInfo]
    parameter_count: dict[DTYPE_T, int] = ...
    def __post_init__(self) -> None: ...
    def __init__(self, metadata, tensors) -> None: ...

@dataclass
class SafetensorsRepoMetadata:
    metadata: dict | None
    sharded: bool
    weight_map: dict[TENSOR_NAME_T, FILENAME_T]
    files_metadata: dict[FILENAME_T, SafetensorsFileMetadata]
    parameter_count: dict[DTYPE_T, int] = ...
    def __post_init__(self) -> None: ...
    def __init__(self, metadata, sharded, weight_map, files_metadata) -> None: ...
