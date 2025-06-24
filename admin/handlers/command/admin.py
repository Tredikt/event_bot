from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

from core.utils.enums import Variables
from settings import config


router = Router(name="admin_command")


@router.message(Command(commands=["admin"]))
async def admin_command_handler(message: Message, variables: Variables):
    user_id = str(message.from_user.id)
    admins = config.ADMINS.split(",")

    if user_id in admins:
        sent_message = await message.answer(
            text="Админ-панель:",
            reply_markup=await variables.keyboards.admin.menu()
        )
        variables.keyboards.admin.set_admin_message_id(sent_message.message_id)
