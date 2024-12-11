from .base import BaseInferenceType as BaseInferenceType
from dataclasses import dataclass

@dataclass
class ObjectDetectionParameters(BaseInferenceType):
    threshold: float | None = ...
    def __init__(self, threshold=...) -> None: ...

@dataclass
class ObjectDetectionInput(BaseInferenceType):
    inputs: str
    parameters: ObjectDetectionParameters | None = ...
    def __init__(self, inputs, parameters=...) -> None: ...

@dataclass
class ObjectDetectionBoundingBox(BaseInferenceType):
    xmax: int
    xmin: int
    ymax: int
    ymin: int
    def __init__(self, xmax, xmin, ymax, ymin) -> None: ...

@dataclass
class ObjectDetectionOutputElement(BaseInferenceType):
    box: ObjectDetectionBoundingBox
    label: str
    score: float
    def __init__(self, box, label, score) -> None: ...
