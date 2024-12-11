from .base import BaseInferenceType as BaseInferenceType
from dataclasses import dataclass
from typing import Any

@dataclass
class AudioToAudioInput(BaseInferenceType):
    inputs: Any
    def __init__(self, inputs) -> None: ...

@dataclass
class AudioToAudioOutputElement(BaseInferenceType):
    blob: Any
    content_type: str
    label: str
    def __init__(self, blob, content_type, label) -> None: ...
