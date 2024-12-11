from .base import BaseInferenceType as BaseInferenceType
from _typeshed import Incomplete
from dataclasses import dataclass
from typing import Any

SummarizationTruncationStrategy: Incomplete

@dataclass
class SummarizationParameters(BaseInferenceType):
    clean_up_tokenization_spaces: bool | None = ...
    generate_parameters: dict[str, Any] | None = ...
    truncation: SummarizationTruncationStrategy | None = ...
    def __init__(self, clean_up_tokenization_spaces=..., generate_parameters=..., truncation=...) -> None: ...

@dataclass
class SummarizationInput(BaseInferenceType):
    inputs: str
    parameters: SummarizationParameters | None = ...
    def __init__(self, inputs, parameters=...) -> None: ...

@dataclass
class SummarizationOutput(BaseInferenceType):
    summary_text: str
    def __init__(self, summary_text) -> None: ...
