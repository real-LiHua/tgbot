from json import loads
from tempfile import mkstemp

from dotenv import load_dotenv
from openai import AsyncOpenAI
from ruamel.yaml import YAML
from telethon import TelegramClient, events, functions, types

from .data import ChatData
from .tools import tools

# Load environment variables from a .env file
load_dotenv()

with open("config.yaml") as file:
    config = YAML().load(file)


async def invoke_model(name: str, **arguments):
    """
    Invoke the specified model with the given arguments.

    Args:
        name (str): The name of the model to invoke.
        **arguments (dict): The arguments to pass to the model.

    Returns:
        The response from the model.
    """
    for lm in config.get(name, []):
        print(lm)
        for auth in lm.auth:
            if auth.get("base_url", "").startswith("https://duckduckgo.com/duckchat"):
                # TODO: 白嫖 duckchat
                pass
            client: AsyncOpenAI = AsyncOpenAI(
                base_url=auth.get("base_url"),
                api_key=auth.get("api_key"),
            )
            match name:
                case "completions":
                    callback = client.chat.completions
                case _:
                    callback = getattr(client, name)
            try:
                arguments["model"] = lm.get("model")
                return await callback.create(**arguments)
            except Exception as e:
                print(e)


async def init(bot: TelegramClient, data: ChatData):
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
        used_functions = []
        next = "send_message"
        while next:
            response = await invoke_model(
                "completions",
                messages=(await data.get_data(event.chat_id))
                + [{"role": "user", "content": str(event.original_update)}],
                max_tokens=1000,
                tools=tools,
            )
            print(response)
            if not response or not response.choices:
                await event.reply("模型无响应")
                return
            message = response.choices[0].message
            if not message.tool_calls:
                res = await event.reply(message.content)
                await data.assistant(res)
                return
            func = message.tool_calls[0].function
            args = loads(func.arguments)
            if "next_function" in args:
                next = args["next_function"]
                del args["next_function"]
            else:
                next = None
            match func.name:
                case "SendReactionRequest":
                    res = await bot(
                        functions.messages.SendReactionRequest(
                            event.chat_id,
                            args["msg_id"],
                            reaction=args.get("reaction")
                            and [types.ReactionEmoji(emoticon=args["reaction"])],
                        ),
                    )
                    await data.tool(event, message.tool_calls[0].id, res)
                case "UploadProfilePhotoRequest":
                    if isinstance(args.get("file"), int):
                        _, name = mkstemp()
                        file = used_functions[args["file"]][1]
                        match file.__class__.__name__:
                            case "JpegImageFile":
                                file.save(f"{name}.jpg")
                                args["file"] = f"{name}.jpg"
                    res = await bot(
                        functions.photos.UploadProfilePhotoRequest(
                            file=await bot.upload_file(args["file"])
                        )
                    )
                case "SetBotInfoRequest":
                    res = await bot(functions.bots.SetBotInfoRequest(**args))
                case "SearXNG":
                    res = None
                case _:
                    try:
                        callback = getattr(bot, func.name)
                        entity = args.get("entity")
                        if entity:
                            del args["entity"]
                        else:
                            entity = event.chat_id
                        if isinstance(args.get("file"), int):
                            _, name = mkstemp()
                            file = used_functions[args["file"]][1]
                            match file.__class__.__name__:
                                case "JpegImageFile":
                                    file.save(f"{name}.jpg")
                                    args["file"] = f"{name}.jpg"
                        if args.get("user"):
                            args["user"] = await bot.get_input_entity(args["user"])
                        res = await callback(entity, **args)
                    except AttributeError:
                        res = await invoke_model(func.name, **args)
            if res:
                await data.tool(event, message.tool_calls[0].id, res)
