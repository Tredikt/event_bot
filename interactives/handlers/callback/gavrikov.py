from aiogram import Router, F
from aiogram.types import Message, CallbackQuery

from core.utils.enums import Variables

router = Router(name="gavrikov_router")

@router.callback_query(F.data == "gavrikov_3_selected")
async def gavrikov_callback_handler(call: CallbackQuery):
    text = "Круто, сейчас посмотрим, сколько таких же как ты"
    await call.message.edit_text(
        text=text
    )