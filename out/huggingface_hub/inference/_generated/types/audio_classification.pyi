from .base import BaseInferenceType as BaseInferenceType
from _typeshed import Incomplete
from dataclasses import dataclass

AudioClassificationOutputTransform: Incomplete

@dataclass
class AudioClassificationParameters(BaseInferenceType):
    function_to_apply: AudioClassificationOutputTransform | None = ...
    top_k: int | None = ...
    def __init__(self, function_to_apply=..., top_k=...) -> None: ...

@dataclass
class AudioClassificationInput(BaseInferenceType):
    inputs: str
    parameters: AudioClassificationParameters | None = ...
    def __init__(self, inputs, parameters=...) -> None: ...

@dataclass
class AudioClassificationOutputElement(BaseInferenceType):
    label: str
    score: float
    def __init__(self, label, score) -> None: ...
