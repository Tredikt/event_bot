import asyncio

from aiogram import Router, F
from aiogram.enums import ChatAction
from aiogram.types import CallbackQuery

from core.utils.enums import Variables


router = Router(name="gavrikov_router")


@router.callback_query(F.data == "gavrikov_start")
async def gavrikov_callback_handler(call: CallbackQuery, variables: Variables, current_speaker: str):
    user_id = call.from_user.id
    if current_speaker != call.data.split("_")[1]:
        kb = await variables.keyboards.menu.get_empty_keyboard()
        await call.message.edit_reply_markup(reply_markup=kb)
        await call.answer(show_alert=True, text="Данный спикер уже не выступает. Невозможно начать данный интерактив")
        return
    else:
        await call.answer()
        await call.message.delete()
        await asyncio.sleep(1)

    await variables.bot.send_chat_action(chat_id=user_id, action=ChatAction.TYPING)
    await asyncio.sleep(1)

    photo = "AgACAgIAAxkBAAIL_GhoYIq9tKqZCIaXcLsX7faQR_I2AAKZ9jEb7Eg5S0j6L_xGf7ilAQADAgADeQADNgQ"
    await call.message.answer_photo(
        photo=photo, 
        caption="📍 <b>Вопрос для разогрева\n\nКто понимает, откуда берутся все эти цифры и как формируются начисления?</b>",
        reply_markup=await variables.keyboards.menu.gavrikov_start()
    )


@router.callback_query(F.data.startswith("gavrikov_pictures"))
async def gavrikov_pictures(call: CallbackQuery, variables: Variables):
    user_id = call.from_user.id

    await variables.bot.send_chat_action(chat_id=user_id, action=ChatAction.TYPING)
    await asyncio.sleep(1)

    text = "Круто, сейчас посмотрим, сколько таких же как ты"
    await call.message.edit_caption(caption=text)