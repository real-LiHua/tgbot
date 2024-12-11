from .base import BaseInferenceType as BaseInferenceType
from dataclasses import dataclass
from typing import Any

@dataclass
class ZeroShotImageClassificationInputData(BaseInferenceType):
    candidate_labels: list[str]
    image: Any
    def __init__(self, candidate_labels, image) -> None: ...

@dataclass
class ZeroShotImageClassificationParameters(BaseInferenceType):
    hypothesis_template: str | None = ...
    def __init__(self, hypothesis_template=...) -> None: ...

@dataclass
class ZeroShotImageClassificationInput(BaseInferenceType):
    inputs: ZeroShotImageClassificationInputData
    parameters: ZeroShotImageClassificationParameters | None = ...
    def __init__(self, inputs, parameters=...) -> None: ...

@dataclass
class ZeroShotImageClassificationOutputElement(BaseInferenceType):
    label: str
    score: float
    def __init__(self, label, score) -> None: ...
