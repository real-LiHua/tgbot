from aiogram.utils.keyboard import ReplyKeyboardBuilder


def main_menu_kb() -> ReplyKeyboardBuilder:
    builder = ReplyKeyboardBuilder()
    builder.button(text="💬 对话")
    builder.button(text="🔄 重置")
    builder.adjust(2)
    return builder
