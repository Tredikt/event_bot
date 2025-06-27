from aiogram import Router, F
from aiogram.types import CallbackQuery

from core.utils.enums import Variables
from core.utils.answers import zabegayev_answers


router = Router(name="zabegayev_callback_router")


@router.callback_query(F.data.startswith("start_zabegayev_"))
async def start_zabegayev(call: CallbackQuery, variables: Variables):
    mode = call.data.split("_")[-1]
    keyboard = await variables.keyboards.menu.zabegayev_1()
    text = ""
    await call.message.delete()
    if mode == "false":
        text="Неверно 😢\n" + zabegayev_answers["zabegaev_1"]
    else:
        text = "✅ Верно!\n" + zabegayev_answers["zabegaev_1"]
    await call.message.answer(
        text=text
    )
    await call.message.answer(
        text="Настройка Sprinter под госсистемы (например, 'Электронный бюджет') занимает 3+ месяца из-за сложной интеграции",
        reply_markup=keyboard
    )


@router.callback_query(F.data.startswith("zabegayev_1_"))
async def zabegayev_2(call: CallbackQuery, variables: Variables):
    mode = call.data.split("_")[-1]
    keyboard = await variables.keyboards.menu.zabegayev_2()
    text = ""
    await call.message.delete()
    if mode == "false":
        text = "Миф! \n" + zabegayev_answers["zabegaev_2"]
    else:
        text="✅ Верно!\n" + zabegayev_answers["zabegaev_2"]

    await call.message.answer(
        text=text
    )
    await call.message.answer(
        text="Sprinter генерирует сложные документы с динамическими таблицами и условным форматированием без ручного программирования шаблонов — в отличие от FastReport/Stimulsoft",
        reply_markup=keyboard
    )


@router.callback_query(F.data.startswith("zabegayev_2_"))
async def zabegayev_2(call: CallbackQuery, variables: Variables):
    mode = call.data.split("_")[-1]
    text = ""
    await call.message.delete()
    if mode == "false":
        text="Не совсем 😢\n" + zabegayev_answers["zabegaev_3"]
    else:
        text = "✅ Верно!\n" + zabegayev_answers["zabegaev_3"]
    await call.message.answer(
        text=text,
        parse_mode="HTML"
    )