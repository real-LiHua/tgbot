from dotenv import load_dotenv
from huggingface_hub import AsyncInferenceClient, ChatCompletionOutputFunctionDefinition
from telethon import TelegramClient, events, functions, types

from .data import ChatData
from .tools import tools

# Load environment variables from a .env file
load_dotenv()


async def init(bot: TelegramClient, data: ChatData, config: dict[str, list[dict]]):
    """
    Initialize the bot with an event handler for AI responses.

    Args:
        bot (TelegramClient): The Telegram client instance.
        data (Data): The data instance containing chat data.
        config (dict[str, list[dict]]): The configuration dictionary containing model details.
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
                model=llm.get("model") if not llm.get("base_url") else None,
                base_url=llm.get("base_url"),
                api_key=llm.get("api_key"),
            )
            try:
                response = await client.chat_completion(
                    data.get_data(event.chat_id),
                    max_tokens=1000,
                    tools=tools,
                    tool_prompt="允许需要使用多个函数"
                )
            except Exception as e:
                print(e)
                continue
            break
        message = response.choices[0].message
        if not message.tool_calls:
            await event.reply(message)
            return
        print(message.tool_calls)
        func: ChatCompletionOutputFunctionDefinition = message.tool_calls[0].function
        #next = func.arguments.get("next_function")
        #del func.arguments["next_function"]
        #print(next)
        try:
            callback = getattr(bot, func.name)
            await callback(event.chat_id, **func.arguments)
        except AttributeError:
            if func.name == "SendReactionRequest":
                await bot(
                    functions.messages.SendReactionRequest(
                        event.chat_id,
                        func.arguments["msg_id"],
                        reaction=(
                            [types.ReactionEmoji(emoticon=func.arguments["reaction"])]
                            if func.arguments.get("reaction")
                            else None
                        ),
                    )
                )
