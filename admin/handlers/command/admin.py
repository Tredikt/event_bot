from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import Message, CallbackQuery

from core.utils.enums import Variables
from settings import config


router = Router(name="admin_command")


@router.message(Command("get_photo_id"))
async def get_photo_id(message: Message):
    """Получить ID фотографии для использования в боте"""
    if not message.photo:
        await message.answer(
            "Отправьте фотографию с подписью /get_photo_id, чтобы получить её ID"
        )
        return
    
    photo_id = message.photo[-1].file_id
    await message.reply(
        f"ID этой фотографии:\n<code>{photo_id}</code>\n\n"
        f"Теперь вы можете использовать этот ID в коде бота для отправки этой фотографии."
    )


@router.message(Command("admin"))
async def admin_panel(message: Message, variables: Variables):
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
