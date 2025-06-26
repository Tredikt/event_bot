from aiogram import Router, F
from aiogram.types import CallbackQuery

from core.utils.enums import Variables

router = Router(name="gavrikov_router")


@router.callback_query(F.data == "gavrikov_3_selected")
async def gavrikov_callback_handler(call: CallbackQuery, variables: Variables):
    text = "Круто, сейчас посмотрим, сколько таких же как ты"
    await call.message.edit_text(
        text=text,
        reply_markup=await variables.keyboards.menu.get_empty_keyboard()
    )