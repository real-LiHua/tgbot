from .base import BaseInferenceType as BaseInferenceType
from dataclasses import dataclass
from typing import Any

@dataclass
class DepthEstimationInput(BaseInferenceType):
    inputs: Any
    parameters: dict[str, Any] | None = ...
    def __init__(self, inputs, parameters=...) -> None: ...

@dataclass
class DepthEstimationOutput(BaseInferenceType):
    depth: Any
    predicted_depth: Any
    def __init__(self, depth, predicted_depth) -> None: ...
