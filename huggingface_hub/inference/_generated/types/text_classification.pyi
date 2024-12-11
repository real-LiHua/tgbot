from .base import BaseInferenceType as BaseInferenceType
from _typeshed import Incomplete
from dataclasses import dataclass

TextClassificationOutputTransform: Incomplete

@dataclass
class TextClassificationParameters(BaseInferenceType):
    function_to_apply: TextClassificationOutputTransform | None = ...
    top_k: int | None = ...
    def __init__(self, function_to_apply=..., top_k=...) -> None: ...

@dataclass
class TextClassificationInput(BaseInferenceType):
    inputs: str
    parameters: TextClassificationParameters | None = ...
    def __init__(self, inputs, parameters=...) -> None: ...

@dataclass
class TextClassificationOutputElement(BaseInferenceType):
    label: str
    score: float
    def __init__(self, label, score) -> None: ...
