from aiogram import Router, F
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, CallbackQuery

from core.bot_states import BotStates
from core.utils.enums import Variables

router = Router(name="nurkhametova_callback_router")

@router.callback_query(F.data.startswith("nurkhametova_menu_"))
async def nurkhametova(call: CallbackQuery, variables: Variables):
    answer = call.data.split("_")[-1]
    if answer == "false":
        text="❌ Неверно!"
    else:
        text="✅ Верно!"

    await call.message.edit_text(
        text=text
    )
    text = "Мигранта депортировали, не дав возможности обжаловать решение. Какое право нарушено?"
    keyboard = await variables.keyboards.menu.nurkhametova_start()
    await call.message.answer(
        text=text,
        reply_markup=keyboard
    )


@router.callback_query(F.data.startswith("nurkhametova_start_"))
async def nurkhametova1(call: CallbackQuery, variables: Variables):
    answer = call.data.split("_")[-1]
    if answer == "false":
        text = "❌ Неверно!"
    else:
        text = "✅ Верно!"

    await call.message.edit_text(
        text=text
    )
    text = "Не предоставили ребенку место в детском садике, какое право нарушено?"
    keyboard = await variables.keyboards.menu.nurkhametova_start1()
    await call.message.answer(
        text=text,
        reply_markup=keyboard
    )


@router.callback_query(F.data.startswith("nurkhametova_start1_"))
async def nurkhametova2(call: CallbackQuery, variables: Variables):
    answer = call.data.split("_")[-1]
    if answer == "false":
        text = "❌ Неверно!"
    else:
        text = "✅ Верно!"

    await call.message.edit_text(
        text=text
    )
    text = "Соседи по ночам шумят, нарушаются ___ права"
    keyboard = await variables.keyboards.menu.nurkhametova_start2()
    await call.message.answer(
        text=text,
        reply_markup=keyboard
    )


@router.callback_query(F.data.startswith("nurkhametova_start2_"))
async def nurkhametova3(call: CallbackQuery, variables: Variables):
    answer = call.data.split("_")[-1]
    if answer == "false":
        text = "❌ Неверно!"
    else:
        text = "✅ Верно!"

    await call.message.edit_text(
        text=text
    )