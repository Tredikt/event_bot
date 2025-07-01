import asyncio

from aiogram import Router, F
from aiogram.enums import ChatAction
from aiogram.types import CallbackQuery, InputMediaPhoto

from core.utils.answer_choices import photo_id
from core.utils.enums import Variables
from core.utils.animate_waiting_message import animate_next_question_loading, send_staged_question

router = Router(name="gavrikov_router")


@router.callback_query(F.data == "gavrikov_start")
async def gavrikov_callback_handler(call: CallbackQuery, variables: Variables):
    user_id = call.from_user.id
    await call.message.delete()

    # Эффект "печатает..."
    await variables.bot.send_chat_action(chat_id=user_id, action=ChatAction.TYPING)
    await asyncio.sleep(1)

    # Фото
    photo = "AgACAgIAAxkBAAIIvmhj35aEvWcbKb9PoB-Pd2v2mLbfAAKJ-jEb-3ARSzztszhCRW-dAQADAgADeQADNgQ"
    await call.message.answer_photo(photo=photo)

    await variables.bot.send_chat_action(chat_id=user_id, action=ChatAction.TYPING)
    await asyncio.sleep(1)

    # Кнопки по одной
    buttons = {
        "1 Вариант": "gavrikov_pictures",
        "2 Вариант": "gavrikov_pictures",
        "3 Вариант": "gavrikov_pictures",
        "4 Вариант": "gavrikov_pictures",
    }

    await send_staged_buttons(
        call=call,
        variables=variables,
        text="Выбери свой вариант:",
        buttons_data=buttons
    )


@router.callback_query(F.data == "gavrikov_pictures")
async def gavrikov_pictures(call: CallbackQuery, variables):
    user_id = call.from_user.id

    await variables.bot.send_chat_action(chat_id=user_id, action=ChatAction.TYPING)
    await asyncio.sleep(1)

    text = "Круто, сейчас посмотрим, сколько таких же как ты"
    await call.message.edit_text(text=text)