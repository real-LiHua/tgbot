from argparse import ArgumentError

from dotenv import load_dotenv

from huggingface_hub import AsyncInferenceClient
from telethon import TelegramClient, events

from .cli import callback
from .data import Data

# Load environment variables from a .env file
load_dotenv()

# Initialize the Hugging Face Async Inference Client
client = AsyncInferenceClient()


async def init(bot: TelegramClient, data: Data):
    """
    Initialize the bot with an event handler for AI responses.

    Args:
        bot (TelegramClient): The Telegram client instance.
        data (Data): The data instance containing chat data.
    """
    @bot.on(events.NewMessage(pattern="/ai", forwards=False))
    async def handler(event: events.NewMessage.Event):
        """
        Handle new messages with the /ai command.

        Args:
            event (events.NewMessage.Event): The new message event.
        """
        response = await client.chat_completion(
            data.get_data(event.chat_id),
            model="Qwen/Qwen2.5-72B-Instruct",
            max_tokens=1000,
        )
        assistant = response.choices[0].message.content or ""
        try:
            await callback(assistant, event)
        except ArgumentError:
            await event.reply(assistant)
        return assistant
