import os

from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN: str = os.environ["BOT_TOKEN"]

AI_PROVIDER: str = os.environ.get("AI_PROVIDER", "openai")
AI_MODEL_ID: str | None = os.environ.get("AI_MODEL_ID") or None
