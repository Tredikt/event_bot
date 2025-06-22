from aiogram import Router, Bot
from aiogram.filters import Command
from aiogram.types import Message

from settings import config


admin_command_router = Router()


@admin_command_router.message(Command(commands=["admin"]))
async def admin_command_handler(update: Message, bot: Bot, variables):
    user_id = str(update.from_user.id)
    admins = config.ADMINS.split(",")

    if user_id in admins:
        text = "Админ-панель:"
        keyboard = await variables.keyboards.admin.menu()

        await update.answer(
            text=text,
            reply_markup=keyboard
        )
