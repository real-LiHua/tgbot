from .base import BaseInferenceType as BaseInferenceType
from dataclasses import dataclass

@dataclass
class ZeroShotClassificationInputData(BaseInferenceType):
    candidate_labels: list[str]
    text: str
    def __init__(self, candidate_labels, text) -> None: ...

@dataclass
class ZeroShotClassificationParameters(BaseInferenceType):
    hypothesis_template: str | None = ...
    multi_label: bool | None = ...
    def __init__(self, hypothesis_template=..., multi_label=...) -> None: ...

@dataclass
class ZeroShotClassificationInput(BaseInferenceType):
    inputs: ZeroShotClassificationInputData
    parameters: ZeroShotClassificationParameters | None = ...
    def __init__(self, inputs, parameters=...) -> None: ...

@dataclass
class ZeroShotClassificationOutputElement(BaseInferenceType):
    label: str
    score: float
    def __init__(self, label, score) -> None: ...
