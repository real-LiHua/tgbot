from tempfile import mkstemp

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

    async def invoke_model(name: str, **arguments):
        """
        Invoke the specified model with the given arguments.

        Args:
            name (str): The name of the model to invoke.
            **arguments (dict): The arguments to pass to the model.

        Returns:
            The response from the model.
        """
        for lm in config.get(name, []) + [dict()]:
            client = AsyncInferenceClient(
                model=(lm.get("model") if not lm.get("base_url") else None),
                base_url=lm.get("base_url"),
                api_key=lm.get("api_key"),
            )
            callback = getattr(client, name)
            try:
                return await callback(**arguments)
            except Exception as e:
                print(e)

    @bot.on(events.NewMessage(pattern="/ai", forwards=False))
    async def handler(event: events.NewMessage.Event):
        """
        Handle new messages with the /ai command.

        Args:
            event (events.NewMessage.Event): The new message event.
        """
        used_functions = []
        next = "send_message"
        while next and next in tool_names:
            response = await invoke_model(
                "chat_completion",
                messages=(await data.get_data(event.chat_id))
                + [{"role": "user", "content": str(event.original_update)}],
                max_tokens=1000,
                tools=tools,
                tool_prompt=(
                    f"请仔细考虑是否需要调用该函数，是否选择正确，是否多余？已使用的函数及其结果的列表为(格式：[(函数,结果),...])： {used_functions}"
                    if used_functions
                    else None
                ),
            )
            message = response.choices[0].message
            if not message.tool_calls:
                res = await event.reply(message)
                await data.assistant(res)
                return
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
                case "UploadProfilePhotoRequest":
                    if isinstance(func.arguments.get("file"), int):
                        _, name = mkstemp()
                        file = used_functions[func.arguments["file"]][1]
                        match file.__class__.__name__:
                            case "JpegImageFile":
                                file.save(f"{name}.jpg")
                                func.arguments["file"] = f"{name}.jpg"
                    await bot(
                        functions.photos.UploadProfilePhotoRequest(
                            file=await bot.upload_file(func.arguments["file"])
                        )
                    )
                case "SetBotInfoRequest":
                    await bot(functions.bots.SetBotInfoRequest(**func.arguments))
                case _:
                    try:
                        callback = getattr(bot, func.name)
                        entity = func.arguments.get("entity")
                        if entity:
                            del func.arguments["entity"]
                        else:
                            entity = event.chat_id
                        if isinstance(func.arguments.get("file"), int):
                            _, name = mkstemp()
                            file = used_functions[func.arguments["file"]][1]
                            match file.__class__.__name__:
                                case "JpegImageFile":
                                    file.save(f"{name}.jpg")
                                    func.arguments["file"] = f"{name}.jpg"
                        if func.arguments.get("user"):
                            func.arguments["user"] = await bot.get_input_entity(
                                func.arguments["user"]
                            )
                        res = await callback(entity, **func.arguments)
                        used_functions.append((func, res))
                    except AttributeError:
                        res = await invoke_model(func.name, **func.arguments)
                        used_functions.append((func, res))
