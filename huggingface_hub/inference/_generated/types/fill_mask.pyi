from .base import BaseInferenceType as BaseInferenceType
from dataclasses import dataclass
from typing import Any

@dataclass
class FillMaskParameters(BaseInferenceType):
    targets: list[str] | None = ...
    top_k: int | None = ...
    def __init__(self, targets=..., top_k=...) -> None: ...

@dataclass
class FillMaskInput(BaseInferenceType):
    inputs: str
    parameters: FillMaskParameters | None = ...
    def __init__(self, inputs, parameters=...) -> None: ...

@dataclass
class FillMaskOutputElement(BaseInferenceType):
    score: float
    sequence: str
    token: int
    token_str: Any
    fill_mask_output_token_str: str | None = ...
    def __init__(self, score, sequence, token, token_str, fill_mask_output_token_str=...) -> None: ...
