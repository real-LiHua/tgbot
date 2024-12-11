from .base import BaseInferenceType as BaseInferenceType
from _typeshed import Incomplete
from dataclasses import dataclass

ImageClassificationOutputTransform: Incomplete

@dataclass
class ImageClassificationParameters(BaseInferenceType):
    function_to_apply: ImageClassificationOutputTransform | None = ...
    top_k: int | None = ...
    def __init__(self, function_to_apply=..., top_k=...) -> None: ...

@dataclass
class ImageClassificationInput(BaseInferenceType):
    inputs: str
    parameters: ImageClassificationParameters | None = ...
    def __init__(self, inputs, parameters=...) -> None: ...

@dataclass
class ImageClassificationOutputElement(BaseInferenceType):
    label: str
    score: float
    def __init__(self, label, score) -> None: ...
