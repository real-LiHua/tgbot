from aiogram import Router, types
from aiogram.filters import CommandStart

router = Router(name="start")


@router.message(CommandStart())
async def handle_start(message: types.Message) -> None:
    await message.answer(
        f"你好，{message.from_user.full_name}！我是一个AI助手，随时为你服务。"
    )
