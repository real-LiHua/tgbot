from .inlineresult import InlineResult as InlineResult
from _typeshed import Incomplete

class InlineResults(list):
    result: Incomplete
    query_id: Incomplete
    cache_time: Incomplete
    users: Incomplete
    gallery: Incomplete
    next_offset: Incomplete
    switch_pm: Incomplete
    def __init__(self, client, original, *, entity: Incomplete | None = None) -> None: ...
    def results_valid(self): ...
