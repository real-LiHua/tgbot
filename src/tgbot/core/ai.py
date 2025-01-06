from argparse import ArgumentError

from dotenv import load_dotenv
from huggingface_hub import AsyncInferenceClient
from telethon import TelegramClient, events

from .cli import callback
from .data import ChatData
from .tools import tools
from aiohttp.client_exceptions import ClientResponseError
# Load environment variables from a .env file
load_dotenv()


async def init(bot: TelegramClient, data: ChatData, config: dict[str, list[dict]]):
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
        for llm in config["chat_completion"]:
            client = AsyncInferenceClient(
                model=llm.get("model") if llm.get("base_url") else None,
                base_url=llm.get("base_url"),
                api_key=llm.get("api_key"),
            )
            try:
                response = await client.chat_completion(
                    data.get_data(event.chat_id),
                    max_tokens=1000,
                    tool_choice="auto",
                    tools=tools,
                )
            except ClientResponseError:
                pass
            print(response)
            break
        assistant = response.choices[0].message.content or ""
        try:
            await callback(assistant, event)
        except ArgumentError:
            await event.reply(assistant)
        return assistant
