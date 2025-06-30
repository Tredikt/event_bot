from aiogram import Router, F
from aiogram.types import CallbackQuery, InputMediaPhoto

from core.utils.enums import Variables

router = Router(name="gavrikov_router")


@router.callback_query(F.data == "gavrikov_start")
async def gavrikov_callback_handler(call: CallbackQuery, variables: Variables):
    text = "Выбери свой вариант"


    # Отправляем медиагруппу (альбом)
    await call.message.answer_photo(
        photo="AgACAgIAAxkBAAIItGhhVXEv4ZHmKka3kXYFDdf5VnyvAAIw-DEb-3AJSwLndVBuCXCZAQADAgADeQADNgQ"
    )

    # Затем отправляем сообщение с кнопками
    await call.message.answer(
        text=text,
        reply_markup=await variables.keyboards.menu.gavrikov_start()
    )


@router.callback_query(F.data == "gavrikov_pictures")
async def gavrikov_pictures(call: CallbackQuery, variables: Variables):
    text="Круто, сейчас посмотрим, сколько такихже как ты"
    await call.message.edit_text(
        text=text
    )