import asyncio

from aiogram import Router, F
from aiogram.enums import ChatAction
from aiogram.types import CallbackQuery

from core.utils.enums import Variables


router = Router(name="gavrikov_router")


@router.callback_query(F.data == "gavrikov_start")
async def gavrikov_callback_handler(call: CallbackQuery, variables: Variables):
    user_id = call.from_user.id

    await call.message.delete()

    await variables.bot.send_chat_action(chat_id=user_id, action=ChatAction.TYPING)
    await asyncio.sleep(1)

    photo = "AgACAgIAAxkBAAIL_GhoYIq9tKqZCIaXcLsX7faQR_I2AAKZ9jEb7Eg5S0j6L_xGf7ilAQADAgADeQADNgQ"
    await call.message.answer_photo(
        photo=photo, 
        caption="Выбери свой вариант",
        reply_markup=await variables.keyboards.menu.gavrikov_start()
    )


@router.callback_query(F.data.startswith("gavrikov_pictures"))
async def gavrikov_pictures(call: CallbackQuery, variables: Variables):
    user_id = call.from_user.id

    await variables.bot.send_chat_action(chat_id=user_id, action=ChatAction.TYPING)
    await asyncio.sleep(1)

    text = "Круто, сейчас посмотрим, сколько таких же как ты"
    await call.message.edit_caption(caption=text)