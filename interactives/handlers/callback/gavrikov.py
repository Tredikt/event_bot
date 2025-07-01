import asyncio

from aiogram import Router, F
from aiogram.enums import ChatAction
from aiogram.types import CallbackQuery, InputMediaPhoto

from core.utils.answer_choices import photo_id
from core.utils.enums import Variables

router = Router(name="gavrikov_router")


@router.callback_query(F.data == "gavrikov_start")
async def gavrikov_callback_handler(call: CallbackQuery, variables):
    user_id = call.from_user.id

    # Удаляем старое сообщение
    await call.message.delete()

    # Показываем "печатает..." перед фото
    await variables.bot.send_chat_action(chat_id=user_id, action=ChatAction.TYPING)
    await asyncio.sleep(1)

    # Отправляем фото
    # photo = "AgACAgIAAxkBAAIF02hjAp83NCaRS2VGhZ_8oriUz6ZQAAKJ-jEb-3ARS70AAeF4i2X_UAEAAwIAA3kAAzYE"
    photo = "AgACAgIAAxkBAAIIvmhj35aEvWcbKb9PoB-Pd2v2mLbfAAKJ-jEb-3ARSzztszhCRW-dAQADAgADeQADNgQ"
    await call.message.answer_photo(photo=photo)

    # Ещё раз "печатает..." перед кнопками
    await variables.bot.send_chat_action(chat_id=user_id, action=ChatAction.TYPING)
    await asyncio.sleep(1)

    # Сообщение и клавиатура
    text = "Выбери свой вариант"
    keyboard = await variables.keyboards.menu.gavrikov_start()
    await call.message.answer(text=text, reply_markup=keyboard)


@router.callback_query(F.data == "gavrikov_pictures")
async def gavrikov_pictures(call: CallbackQuery, variables):
    user_id = call.from_user.id

    await variables.bot.send_chat_action(chat_id=user_id, action=ChatAction.TYPING)
    await asyncio.sleep(1)

    text = "Круто, сейчас посмотрим, сколько таких же как ты"
    await call.message.edit_text(text=text)