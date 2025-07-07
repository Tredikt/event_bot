from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import Message, BufferedInputFile
from aiogram.enums import ChatAction

from core.utils.enums import Variables
from admin.services.analytics_service import AnalyticsService
from settings import config


router = Router(name="admin_command_router")


@router.message(Command("admin"))
async def admin_message_handler(message: Message, variables: Variables):
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


@router.message(Command("get_excel"))
async def admin_get_excel(message: Message, variables: Variables):
    """Команда для генерации Excel аналитики"""
    user_id = str(message.from_user.id)
    username = message.from_user.username
    admins = config.ADMINS.split(",")
    admins_usernames = config.ADMINS_USERNAMES.split(",")

    if user_id in admins or username in admins_usernames:
        # Показываем индикатор загрузки
        await variables.bot.send_chat_action(chat_id=message.chat.id, action=ChatAction.UPLOAD_DOCUMENT)
        
        try:
            # Генерируем Excel файл
            analytics_service = AnalyticsService()
            excel_data = await analytics_service.generate_analytics_excel(variables)
            
            # Создаем файл для отправки
            from datetime import datetime
            filename = f"analytics_technobars_{datetime.now().strftime('%Y%m%d_%H%M%S')}.xlsx"
            excel_file = BufferedInputFile(
                file=excel_data,
                filename=filename
            )
            
            # Отправляем файл
            await message.answer_document(
                document=excel_file,
                caption="📊 Аналитика ТЕХНОБАРС\n\nСгенерирован Excel файл с полной аналитикой по всем интерактивам и пользователям."
            )
            
        except Exception as e:
            await message.answer(f"❌ Ошибка при генерации Excel: {str(e)}")
            print(f"Ошибка генерации Excel: {e}")


@router.message(Command("get_photo_id"))
async def get_photo_id(message: Message, variables: Variables):
    """Команда для получения ID фотографий"""
    user_id = str(message.from_user.id)
    username = message.from_user.username
    admins = config.ADMINS.split(",")
    admins_usernames = config.ADMINS_USERNAMES.split(",")

    if user_id in admins or username in admins_usernames:
        await message.answer(
            "Отправьте фото, чтобы получить его file_id"
        )


@router.message(F.photo)
async def photo_handler(message: Message, variables: Variables):
    """Обработчик фотографий для получения file_id"""
    user_id = str(message.from_user.id)
    username = message.from_user.username
    admins = config.ADMINS.split(",")
    admins_usernames = config.ADMINS_USERNAMES.split(",")

    if user_id in admins or username in admins_usernames:
        photo_id = message.photo[-1].file_id
        await message.reply(
            f"📷 ID этой фотографии:\n<code>{photo_id}</code>\n\n"
            f"Теперь вы можете использовать этот ID в коде бота для отправки этой фотографии."
        )
