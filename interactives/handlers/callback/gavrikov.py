from aiogram import Router, F
from aiogram.types import Message, CallbackQuery, InputMediaPhoto

from core.utils.enums import Variables

router = Router(name="gavrikov_callback_router")

@router.callback_query(F.data == "gavrikov")
async def gavrikov_start(call: CallbackQuery, variables: Variables):
    keyboard = await variables.keyboards.menu.gavrikov_start()

    media = [
        InputMediaPhoto(media="AgACAgIAAxkBAAMFaFcQ_bAajmdRRrRUPc1WLuF5uVcAAgLvMRukirlKyfZiVwEziscBAAMCAAN5AAM2BA"),
        InputMediaPhoto(media="AgACAgIAAxkBAAMHaFcTMPZN7jYfB-b3uR_WFMsk_QQAAhXvMRukirlKGXtiRMCU904BAAMCAAN4AAM2BA"),
        InputMediaPhoto(media="AgACAgIAAxkBAAMKaFcTvstEOfy671PFkdA_LtsbjBYAAhbvMRukirlKOh275kqGKBkBAAMCAAN5AAM2BA"),
        InputMediaPhoto(media="AgACAgIAAxkBAAMMaFcTx-ZSxh7F174w_axhQOWSPCsAAhfvMRukirlKgRT9cB-qn2sBAAMCAAN5AAM2BA"),
    ]
    await call.message.answer_media_group(media=media)

    await call.message.answer(
        text="Выберите действие ниже:",
        reply_markup=keyboard
    )

@router.callback_query(F.data == "gavrikov_3_selected")
async def gavrikov_callback_handler(call: CallbackQuery):
    text = "Круто, сейчас посмотрим, сколько таких же как ты"
    await call.message.edit_text(
        text=text
    )