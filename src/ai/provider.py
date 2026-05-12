import ai

from src.config import AI_MODEL_ID, AI_PROVIDER


def get_model() -> ai.Model:
    provider = AI_PROVIDER.lower()

    if provider == "openai":
        return ai.openai(AI_MODEL_ID or "gpt-4o-mini")
    elif provider == "anthropic":
        return ai.anthropic(AI_MODEL_ID or "claude-sonnet-4")
    elif provider == "ai_gateway":
        return ai.ai_gateway(AI_MODEL_ID or "openai/gpt-4o-mini")
    else:
        raise ValueError(f"Unknown AI provider: {provider}")
