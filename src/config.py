import os

from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN: str = os.environ["BOT_TOKEN"]

AI_PROVIDER: str = os.environ.get("AI_PROVIDER", "openai")
AI_MODEL_ID: str | None = os.environ.get("AI_MODEL_ID") or None

DOCKER_AGENT_URL: str = os.environ.get("DOCKER_AGENT_URL", "http://localhost:8080")
BOT_TOOL_API_KEY: str = os.environ.get("BOT_TOOL_API_KEY", "")
