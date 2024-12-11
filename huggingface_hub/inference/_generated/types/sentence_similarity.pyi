from .base import BaseInferenceType as BaseInferenceType
from dataclasses import dataclass
from typing import Any

@dataclass
class SentenceSimilarityInputData(BaseInferenceType):
    sentences: list[str]
    source_sentence: str
    def __init__(self, sentences, source_sentence) -> None: ...

@dataclass
class SentenceSimilarityInput(BaseInferenceType):
    inputs: SentenceSimilarityInputData
    parameters: dict[str, Any] | None = ...
    def __init__(self, inputs, parameters=...) -> None: ...
