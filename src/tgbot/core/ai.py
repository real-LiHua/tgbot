from dotenv import load_dotenv
from huggingface_hub import AsyncInferenceClient, ChatCompletionOutputFunctionDefinition
from telethon import TelegramClient, events, functions, types

from .data import ChatData
from .tools import tool_names, tools

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
        print(data.get_data(event.chat_id))
        used_functions = []
        next = "send_message"
        while next and next in tool_names:
            for lm in config["chat_completion"]:
                client = AsyncInferenceClient(
                    model=lm.get("model") if not lm.get("base_url") else None,
                    base_url=lm.get("base_url"),
                    api_key=lm.get("api_key"),
                )
                try:
                    response = await client.chat_completion(
                        data.get_data(event.chat_id),
                        max_tokens=1000,
                        tools=tools,
                        tool_prompt=(
                            f"已使用过的函数及结果为： {used_functions}" if used_functions else None
                        ),
                    )
                except Exception as e:
                    print(e)
                    continue
                break
            message = response.choices[0].message
            if not message.tool_calls:
                res = await event.reply(message)
                data.assistant(res)
                return
            print(message.tool_calls)
            func: ChatCompletionOutputFunctionDefinition = message.tool_calls[
                0
            ].function
            if "next_function" in func.arguments:
                next = func.arguments["next_function"]
                del func.arguments["next_function"]
            else:
                next = None
            match func.name:
                case "SendReactionRequest":
                    res = await bot(
                        functions.messages.SendReactionRequest(
                            event.chat_id,
                            func.arguments["msg_id"],
                            reaction=func.arguments.get("reaction")
                            and [
                                types.ReactionEmoji(emoticon=func.arguments["reaction"])
                            ],
                        ),
                    )
                    used_functions.append((func, res))
                case _:
                    try:
                        callback = getattr(bot, func.name)
                        res = await callback(event.chat_id, **func.arguments)
                        used_functions.append((func, res))
                        data.assistant(res)
                    except AttributeError:
                        for lm in config[func.name]:
                            client = AsyncInferenceClient(
                                model=(
                                    lm.get("model") if not lm.get("base_url") else None
                                ),
                                base_url=lm.get("base_url"),
                                api_key=lm.get("api_key"),
                            )
                            callback = getattr(client, func.name)
                            try:
                                res = await callback(**func.arguments)
                                used_functions.append((func, res))
                                data.assistant(res)
                                if res:
                                    print(res)
                                    break
                            except Exception as e:
                                print(e)
