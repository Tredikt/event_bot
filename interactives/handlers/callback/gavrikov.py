from aiogram import Router, F
from aiogram.types import CallbackQuery, InputMediaPhoto

from core.utils.answer_choices import photo_id
from core.utils.enums import Variables

router = Router(name="gavrikov_router")


@router.callback_query(F.data == "gavrikov_start")
async def gavrikov_callback_handler(call: CallbackQuery, variables: Variables):
    text = "Выбери свой вариант"
    photo = "AgACAgIAAxkBAAIF02hjAp83NCaRS2VGhZ_8oriUz6ZQAAKJ-jEb-3ARS70AAeF4i2X_UAEAAwIAA3kAAzYE"

    # Отправляем медиагруппу (альбом)
    await call.message.answer_photo(
        photo=photo
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