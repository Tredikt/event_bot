from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

from core.utils.enums import Variables
from settings import config


router = Router(name="admin_command")


@router.message(Command(commands=["admin"]))
async def admin_command_handler(message: Message, variables: Variables):
    user_id = str(message.from_user.id)
    print(f"Raw ADMINS from config: '{config.ADMINS}'")
    admins = [admin.strip() for admin in config.ADMINS.split(",")]
    print(f"Processed admins list: {admins}")
    print(f"Current user_id: {user_id}")

    if user_id in admins:
        sent_message = await message.answer(
            text="Админ-панель:",
            reply_markup=await variables.keyboards.admin.menu()
        )
        variables.keyboards.admin.set_admin_message_id(sent_message.message_id)
