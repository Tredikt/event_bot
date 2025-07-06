from aiogram import Bot
from aiogram.utils.keyboard import InlineKeyboardBuilder

from core.db_class import DBClass
from core.models import Messages
from core.utils.enums import Variables


async def delete_keyboard(bot: Bot, db: DBClass, messages: list[Messages], all_: bool = False):
    empty_keyboard = InlineKeyboardBuilder().as_markup()
    for message in messages:
        try:
            await bot.edit_message_reply_markup(
                chat_id=message.chat_id,
                message_id=message.message_id,
                reply_markup=empty_keyboard
            )
        except Exception as e:
            print("Ошибка при удалении клавиатуры:", e)
            continue
    if all_:
        await db.messages.delete_all()