import logging
from json import loads
from tempfile import mkstemp

from aiohttp import ClientSession
from httpx import AsyncClient
from openai import AsyncAssistantEventHandler, AsyncAzureOpenAI, AsyncOpenAI
from telethon import TelegramClient, events, functions, types

from .. import CONFIG
from .data import ChatData
from .tools import tools

tor = CONFIG.get("tor", dict())
tor_proxy = tor.get("proxy", "socks5://127.0.0.1:9050") if tor else None
tor_proxy_auth = tor.get("proxy_auth")


async def invoke_model(name: str, **arguments):
    """
    Invoke the specified model with the given arguments.

    Args:
        name (str): The name of the model to invoke.
        **arguments (dict): The arguments to pass to the model.

    Returns:
        The response from the model.
    """
    use_tools = bool(arguments.get("tools"))
    for lm in CONFIG.get(name, []):
        if use_tools and not lm.get("tool"):
            continue
        for auth in lm.get("auth", []):
            if auth.get("base_url", "").startswith("https://duckduckgo.com/duckchat"):
                # TODO: Implement DuckDuckGo DuckChat API integration
                pass
            if proxy := auth.get("proxy"):
                http_client = AsyncClient(proxy=proxy)
                del auth["proxy"]
            else:
                http_client = None
            client: AsyncAzureOpenAI | AsyncOpenAI
            if auth.get("azure_endpoint"):
                client = AsyncAzureOpenAI(http_client=http_client, **auth)
            else:
                client = AsyncOpenAI(
                    http_client=http_client,
                    **auth,
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
                logging.error(f"Error invoking model {name}: {e}")


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
        for count in range(2):
            response = await invoke_model(
                "completions",
                messages=(await data.get_data(event.chat_id))
                + [{"role": "user", "content": str(event.original_update)}],
                max_tokens=1000,
                tools=tools,
            )
            logging.debug(response)
            if not response or not response.choices:
                await event.reply("模型无响应")
                return
            message = response.choices[0].message
            if not message.tool_calls:
                res = await event.reply(message.content)
                await data.assistant(res)
                return
            for tool in message.tool_calls:
                func = tool.function
                args = loads(func.arguments)
                try:
                    match func.name:
                        case "SendReactionRequest":
                            res = await bot(
                                functions.messages.SendReactionRequest(
                                    event.chat_id,
                                    args["msg_id"],
                                    reaction=args.get("reaction")
                                    and [
                                        types.ReactionEmoji(emoticon=args["reaction"])
                                    ],
                                ),
                            )
                        case "UploadProfilePhotoRequest":
                            # FIXME: Handle different file types and ensure proper file handling
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
                            # TODO: Implement SearXNG search functionality
                            res = None
                            args["format"] = "json"
                            async with ClientSession() as session:
                                async with session.get(
                                    "https://searx.space/data/instances.json"
                                ) as response:
                                    searxng = await response.json()
                                    for url, info in searxng["instances"].items():
                                        if info["network_type"] == "tor":
                                            if not tor:
                                                continue
                                        async with session.get(
                                            url,
                                            params=args,
                                            proxy=tor_proxy,
                                            proxy_auth=tor_proxy_auth,
                                        ) as r:
                                            if r.status != 200:
                                                continue
                                            res = await r.json()
                        case _:
                            try:
                                callback = getattr(bot, func.name)
                                entity = args.get("entity")
                                if entity:
                                    del args["entity"]
                                else:
                                    entity = event.chat_id
                                # FIXME: Handle different file types and ensure proper file handling
                                if isinstance(args.get("file"), int):
                                    _, name = mkstemp()
                                    file = used_functions[args["file"]][1]
                                    match file.__class__.__name__:
                                        case "JpegImageFile":
                                            file.save(f"{name}.jpg")
                                            args["file"] = f"{name}.jpg"
                                    if args.get("user"):
                                        args["user"] = await bot.get_input_entity(
                                            args["user"]
                                        )
                                res = await callback(entity, **args)
                            except AttributeError:
                                res = await invoke_model(func.name, **args)
                    if res:
                        await data.tool(event, tool.id, res)
                except Exception as e:
                    logging.error(e)
