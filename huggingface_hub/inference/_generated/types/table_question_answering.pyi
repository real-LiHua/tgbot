from .base import BaseInferenceType as BaseInferenceType
from dataclasses import dataclass
from typing import Any

@dataclass
class TableQuestionAnsweringInputData(BaseInferenceType):
    question: str
    table: dict[str, list[str]]
    def __init__(self, question, table) -> None: ...

@dataclass
class TableQuestionAnsweringInput(BaseInferenceType):
    inputs: TableQuestionAnsweringInputData
    parameters: dict[str, Any] | None = ...
    def __init__(self, inputs, parameters=...) -> None: ...

@dataclass
class TableQuestionAnsweringOutputElement(BaseInferenceType):
    answer: str
    cells: list[str]
    coordinates: list[list[int]]
    aggregator: str | None = ...
    def __init__(self, answer, cells, coordinates, aggregator=...) -> None: ...
