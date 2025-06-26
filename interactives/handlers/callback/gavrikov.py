from aiogram import Router, F
from aiogram.types import CallbackQuery, InputMediaPhoto

from core.utils.enums import Variables

router = Router(name="gavrikov_router")


@router.callback_query(F.data == "gavrikov_menu")
async def gavrikov_callback_handler(call: CallbackQuery, variables: Variables):
    text = "Выбери свой вариант"

    media = [
        InputMediaPhoto(media="AgACAgIAAxkBAAMFaFcQ_bAajmdRRrRUPc1WLuF5uVcAAgLvMRukirlKyfZiVwEziscBAAMCAAN5AAM2BA"),
        InputMediaPhoto(media="AgACAgIAAxkBAAMHaFcTMPZN7jYfB-b3uR_WFMsk_QQAAhXvMRukirlKGXtiRMCU904BAAMCAAN4AAM2BA"),
        InputMediaPhoto(media="AgACAgIAAxkBAAMKaFcTvstEOfy671PFkdA_LtsbjBYAAhbvMRukirlKOh275kqGKBkBAAMCAAN5AAM2BA"),
        InputMediaPhoto(media="AgACAgIAAxkBAAMMaFcTx-ZSxh7F174w_axhQOWSPCsAAhfvMRukirlKgRT9cB-qn2sBAAMCAAN5AAM2BA")
    ]

    # Отправляем медиагруппу (альбом)
    await call.message.answer_media_group(media=media)

    # Затем отправляем сообщение с кнопками
    await call.message.answer(
        text=text,
        reply_markup=await variables.keyboards.menu.gavrikov_menu()
    )