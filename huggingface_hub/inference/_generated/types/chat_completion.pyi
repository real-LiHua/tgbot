from .base import BaseInferenceType as BaseInferenceType
from _typeshed import Incomplete
from dataclasses import dataclass
from typing import Any

@dataclass
class ChatCompletionInputURL(BaseInferenceType):
    url: str
    def __init__(self, url) -> None: ...

ChatCompletionInputMessageChunkType: Incomplete

@dataclass
class ChatCompletionInputMessageChunk(BaseInferenceType):
    type: ChatCompletionInputMessageChunkType
    image_url: ChatCompletionInputURL | None = ...
    text: str | None = ...
    def __init__(self, type, image_url=..., text=...) -> None: ...

@dataclass
class ChatCompletionInputMessage(BaseInferenceType):
    content: list[ChatCompletionInputMessageChunk] | str
    role: str
    name: str | None = ...
    def __init__(self, content, role, name=...) -> None: ...

ChatCompletionInputGrammarTypeType: Incomplete

@dataclass
class ChatCompletionInputGrammarType(BaseInferenceType):
    type: ChatCompletionInputGrammarTypeType
    value: Any
    def __init__(self, type, value) -> None: ...

@dataclass
class ChatCompletionInputStreamOptions(BaseInferenceType):
    include_usage: bool
    def __init__(self, include_usage) -> None: ...

@dataclass
class ChatCompletionInputFunctionName(BaseInferenceType):
    name: str
    def __init__(self, name) -> None: ...

@dataclass
class ChatCompletionInputToolType(BaseInferenceType):
    function: ChatCompletionInputFunctionName | None = ...
    def __init__(self, function=...) -> None: ...

@dataclass
class ChatCompletionInputFunctionDefinition(BaseInferenceType):
    arguments: Any
    name: str
    description: str | None = ...
    def __init__(self, arguments, name, description=...) -> None: ...

@dataclass
class ToolElement(BaseInferenceType):
    function: ChatCompletionInputFunctionDefinition
    type: str
    def __init__(self, function, type) -> None: ...

@dataclass
class ChatCompletionInput(BaseInferenceType):
    messages: list[ChatCompletionInputMessage]
    frequency_penalty: float | None = ...
    logit_bias: list[float] | None = ...
    logprobs: bool | None = ...
    max_tokens: int | None = ...
    model: str | None = ...
    n: int | None = ...
    presence_penalty: float | None = ...
    response_format: ChatCompletionInputGrammarType | None = ...
    seed: int | None = ...
    stop: list[str] | None = ...
    stream: bool | None = ...
    stream_options: ChatCompletionInputStreamOptions | None = ...
    temperature: float | None = ...
    tool_choice: ChatCompletionInputToolType | str | None = ...
    tool_prompt: str | None = ...
    tools: list[ToolElement] | None = ...
    top_logprobs: int | None = ...
    top_p: float | None = ...
    def __init__(self, messages, frequency_penalty=..., logit_bias=..., logprobs=..., max_tokens=..., model=..., n=..., presence_penalty=..., response_format=..., seed=..., stop=..., stream=..., stream_options=..., temperature=..., tool_choice=..., tool_prompt=..., tools=..., top_logprobs=..., top_p=...) -> None: ...

@dataclass
class ChatCompletionOutputTopLogprob(BaseInferenceType):
    logprob: float
    token: str
    def __init__(self, logprob, token) -> None: ...

@dataclass
class ChatCompletionOutputLogprob(BaseInferenceType):
    logprob: float
    token: str
    top_logprobs: list[ChatCompletionOutputTopLogprob]
    def __init__(self, logprob, token, top_logprobs) -> None: ...

@dataclass
class ChatCompletionOutputLogprobs(BaseInferenceType):
    content: list[ChatCompletionOutputLogprob]
    def __init__(self, content) -> None: ...

@dataclass
class ChatCompletionOutputFunctionDefinition(BaseInferenceType):
    arguments: Any
    name: str
    description: str | None = ...
    def __init__(self, arguments, name, description=...) -> None: ...

@dataclass
class ChatCompletionOutputToolCall(BaseInferenceType):
    function: ChatCompletionOutputFunctionDefinition
    id: str
    type: str
    def __init__(self, function, id, type) -> None: ...

@dataclass
class ChatCompletionOutputMessage(BaseInferenceType):
    role: str
    content: str | None = ...
    tool_calls: list[ChatCompletionOutputToolCall] | None = ...
    def __init__(self, role, content=..., tool_calls=...) -> None: ...

@dataclass
class ChatCompletionOutputComplete(BaseInferenceType):
    finish_reason: str
    index: int
    message: ChatCompletionOutputMessage
    logprobs: ChatCompletionOutputLogprobs | None = ...
    def __init__(self, finish_reason, index, message, logprobs=...) -> None: ...

@dataclass
class ChatCompletionOutputUsage(BaseInferenceType):
    completion_tokens: int
    prompt_tokens: int
    total_tokens: int
    def __init__(self, completion_tokens, prompt_tokens, total_tokens) -> None: ...

@dataclass
class ChatCompletionOutput(BaseInferenceType):
    choices: list[ChatCompletionOutputComplete]
    created: int
    id: str
    model: str
    system_fingerprint: str
    usage: ChatCompletionOutputUsage
    def __init__(self, choices, created, id, model, system_fingerprint, usage) -> None: ...

@dataclass
class ChatCompletionStreamOutputFunction(BaseInferenceType):
    arguments: str
    name: str | None = ...
    def __init__(self, arguments, name=...) -> None: ...

@dataclass
class ChatCompletionStreamOutputDeltaToolCall(BaseInferenceType):
    function: ChatCompletionStreamOutputFunction
    id: str
    index: int
    type: str
    def __init__(self, function, id, index, type) -> None: ...

@dataclass
class ChatCompletionStreamOutputDelta(BaseInferenceType):
    role: str
    content: str | None = ...
    tool_calls: ChatCompletionStreamOutputDeltaToolCall | None = ...
    def __init__(self, role, content=..., tool_calls=...) -> None: ...

@dataclass
class ChatCompletionStreamOutputTopLogprob(BaseInferenceType):
    logprob: float
    token: str
    def __init__(self, logprob, token) -> None: ...

@dataclass
class ChatCompletionStreamOutputLogprob(BaseInferenceType):
    logprob: float
    token: str
    top_logprobs: list[ChatCompletionStreamOutputTopLogprob]
    def __init__(self, logprob, token, top_logprobs) -> None: ...

@dataclass
class ChatCompletionStreamOutputLogprobs(BaseInferenceType):
    content: list[ChatCompletionStreamOutputLogprob]
    def __init__(self, content) -> None: ...

@dataclass
class ChatCompletionStreamOutputChoice(BaseInferenceType):
    delta: ChatCompletionStreamOutputDelta
    index: int
    finish_reason: str | None = ...
    logprobs: ChatCompletionStreamOutputLogprobs | None = ...
    def __init__(self, delta, index, finish_reason=..., logprobs=...) -> None: ...

@dataclass
class ChatCompletionStreamOutputUsage(BaseInferenceType):
    completion_tokens: int
    prompt_tokens: int
    total_tokens: int
    def __init__(self, completion_tokens, prompt_tokens, total_tokens) -> None: ...

@dataclass
class ChatCompletionStreamOutput(BaseInferenceType):
    choices: list[ChatCompletionStreamOutputChoice]
    created: int
    id: str
    model: str
    system_fingerprint: str
    usage: ChatCompletionStreamOutputUsage | None = ...
    def __init__(self, choices, created, id, model, system_fingerprint, usage=...) -> None: ...
