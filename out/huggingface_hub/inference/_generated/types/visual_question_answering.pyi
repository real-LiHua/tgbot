from .base import BaseInferenceType as BaseInferenceType
from dataclasses import dataclass
from typing import Any

@dataclass
class VisualQuestionAnsweringInputData(BaseInferenceType):
    image: Any
    question: Any
    def __init__(self, image, question) -> None: ...

@dataclass
class VisualQuestionAnsweringParameters(BaseInferenceType):
    top_k: int | None = ...
    def __init__(self, top_k=...) -> None: ...

@dataclass
class VisualQuestionAnsweringInput(BaseInferenceType):
    inputs: VisualQuestionAnsweringInputData
    parameters: VisualQuestionAnsweringParameters | None = ...
    def __init__(self, inputs, parameters=...) -> None: ...

@dataclass
class VisualQuestionAnsweringOutputElement(BaseInferenceType):
    label: Any
    score: float
    answer: str | None = ...
    def __init__(self, label, score, answer=...) -> None: ...
