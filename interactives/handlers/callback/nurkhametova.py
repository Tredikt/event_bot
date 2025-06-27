from aiogram import Router, F
from aiogram.types import CallbackQuery

from core.utils.enums import Variables
from core.utils.nurkhametova_explanation import explanations
from core.utils.nurkhametova_questions import questions

router = Router(name="nurkhametova_callback_router")

keyboards = {
    "menu": "nurkhametova_menu",
    "start": "nurkhametova_start",
    "start1": "nurkhametova_start1",
    "start2": "nurkhametova_start2"
}

# 1. Первый вопрос
@router.callback_query(F.data.startswith("nurkhametova_menu_"))
async def nurkhametova(call: CallbackQuery, variables: Variables):
    answer = call.data.split("_")[-1]
    key = "menu"
    correct_text = explanations[key]
    if answer == "false":
        text = f"❌ Неверно!\n\n{correct_text}"
    else:
        text = f"✅ Верно!\n\n{correct_text}"
    await call.message.edit_text(text=text)
    await call.message.answer(
        text=questions["start"],
        reply_markup=await getattr(variables.keyboards.menu, keyboards["start"])()
    )

# 2. Второй вопрос
@router.callback_query(F.data.startswith("nurkhametova_start_"))
async def nurkhametova1(call: CallbackQuery, variables: Variables):
    answer = call.data.split("_")[-1]
    key = "start"
    correct_text = explanations[key]
    if answer == "false":
        text = f"❌ Неверно!\n\n{correct_text}"
    else:
        text = f"✅ Верно!\n\n{correct_text}"
    await call.message.edit_text(text=text)
    await call.message.answer(
        text=questions["start1"],
        reply_markup=await getattr(variables.keyboards.menu, keyboards["start1"])()
    )

# 3. Третий вопрос
@router.callback_query(F.data.startswith("nurkhametova_start1_"))
async def nurkhametova2(call: CallbackQuery, variables: Variables):
    answer = call.data.split("_")[-1]
    key = "start1"
    correct_text = explanations[key]
    if answer == "false":
        text = f"❌ Неверно!\n\n{correct_text}"
    else:
        text = f"✅ Верно!\n\n{correct_text}"
    await call.message.edit_text(text=text)
    await call.message.answer(
        text=questions["start2"],
        reply_markup=await getattr(variables.keyboards.menu, keyboards["start2"])()
    )

# 4. Последний вопрос — финал
@router.callback_query(F.data.startswith("nurkhametova_start2_"))
async def nurkhametova3(call: CallbackQuery, variables: Variables):
    answer = call.data.split("_")[-1]
    key = "start2"
    correct_text = explanations[key]
    if answer == "false":
        text = f"❌ Неверно!\n\n{correct_text}"
    else:
        text = f"✅ Верно!\n\n{correct_text}"
    await call.message.edit_text(text=text)
    # Можно добавить финальное сообщение или статистику, если хочешь
