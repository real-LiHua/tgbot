from _typeshed import Incomplete
from typing import Any, Callable, TypeVar

UNION_TYPES: list[Any]
HTTP_METHOD_T: Incomplete
CallableT = TypeVar('CallableT', bound=Callable)

def is_jsonable(obj: Any) -> bool: ...
def is_simple_optional_type(type_: type) -> bool: ...
def unwrap_simple_optional_type(optional_type: type) -> type: ...
