from aiogram import Router, F
from aiogram.types import Message, CallbackQuery

from core.utils.enums import Variables


router = Router(name="belozyortseva_router")




@router.callback_query(F.data.startswith("belozyortseva_test_"))
async def belozyortseva_callback_handler(call: CallbackQuery, variables: Variables):
    parts = call.data.split("_")
    number_test = int(parts[-2])
    is_correct = parts[-1] == "true"
    text = "✅ Верно!" if is_correct else "❌ Неверно!"
    number_test += 1
    if number_test == 2:
        await call.message.edit_text(
            text=text,
        )
        await call.message.answer(
            text="Фронтенд — это адаптивное веб-приложение, которое общается с сервером через…",
            reply_markup=await variables.keyboards.menu.belozyortseva_menu(number_test=number_test)
        )
    await call.answer()