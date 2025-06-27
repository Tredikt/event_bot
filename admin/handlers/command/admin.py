from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

from core.utils.enums import Variables
from settings import config


router = Router(name="admin_command")


@router.message(Command(commands=["admin"]))
async def admin_command_handler(message: Message, variables: Variables):
    user_id = str(message.from_user.id)
    username = message.from_user.username
    admins = config.ADMINS.split(",")
    admins_usernames = config.ADMINS_USERNAMES.split(",")

    if user_id in admins or username in admins_usernames:
        sent_message = await message.answer(
            text="Админ-панель:",
            reply_markup=await variables.keyboards.admin.menu()
        )
        variables.keyboards.admin.set_admin_message_id(sent_message.message_id)
