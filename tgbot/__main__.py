import logging
from os import getenv
from pathlib import Path

from dotenv import load_dotenv
from telegram import Update
from telegram.ext import (
    Application,
    ApplicationBuilder,
    CommandHandler,
    MessageHandler,
    PicklePersistence,
)
from telegram.ext.filters import ChatType

from . import command_handler, message_handler

load_dotenv()
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
)


application: Application = (
    ApplicationBuilder()
    .token(getenv("BOT_TOKEN"))
    # .http_version("2")
    .persistence(PicklePersistence(filepath=Path("site") / "", single_file=False))
    .build()
)

application.add_handler(CommandHandler("test", command_handler))
application.add_handler(MessageHandler(ChatType.SUPERGROUP, message_handler))
application.run_polling(allowed_updates=Update.ALL_TYPES)
