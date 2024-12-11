from .base import BaseInferenceType as BaseInferenceType
from dataclasses import dataclass
from typing import Any

@dataclass
class ZeroShotObjectDetectionInputData(BaseInferenceType):
    candidate_labels: list[str]
    image: Any
    def __init__(self, candidate_labels, image) -> None: ...

@dataclass
class ZeroShotObjectDetectionInput(BaseInferenceType):
    inputs: ZeroShotObjectDetectionInputData
    parameters: dict[str, Any] | None = ...
    def __init__(self, inputs, parameters=...) -> None: ...

@dataclass
class ZeroShotObjectDetectionBoundingBox(BaseInferenceType):
    xmax: int
    xmin: int
    ymax: int
    ymin: int
    def __init__(self, xmax, xmin, ymax, ymin) -> None: ...

@dataclass
class ZeroShotObjectDetectionOutputElement(BaseInferenceType):
    box: ZeroShotObjectDetectionBoundingBox
    label: str
    score: float
    def __init__(self, box, label, score) -> None: ...
