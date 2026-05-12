from aiogram import Router, types
from aiogram.filters import Command

router = Router(name="ping")


@router.message(Command("ping"))
async def handle_ping(message: types.Message) -> None:
    await message.answer("pong")
