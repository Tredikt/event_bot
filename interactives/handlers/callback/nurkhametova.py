from aiogram import Router, F
from aiogram.types import Message, CallbackQuery

from core.utils.enums import Variables
from core.utils.nurkhamedova_text import nurkhametova_text

router = Router(name="nurkhametova_callback_router")

@router.callback_query(F.data == "nurkhametova")
async def nurkhametova_start(call: CallbackQuery, variables):
    text = nurkhametova_text[0]["text"]
    keyboard = await variables.keyboards.menu.interactive_nurkhametova()
    await call.message.edit_text(text=text, reply_markup=keyboard)


@router.callback_query(F.data.startswith("interactive_nurkhametova_"))
async def handle_nurkhametova_step(call: CallbackQuery, variables):
    try:
        _, _, step_str, user_answer = call.data.split("_")
        step_index = int(step_str)
    except Exception:
        await call.answer("Ошибка разбора ответа", show_alert=True)
        return

    step = nurkhametova_text[step_index]
    correct_answer = step["correct"]
    feedback = step.get("wrong_feedback")

    messages = []

    if user_answer != correct_answer and feedback:
        messages.append(feedback)

    next_step_index = step_index + 1
    if next_step_index < len(nurkhametova_text):
        next_text = nurkhametova_text[next_step_index]["text"]

        if next_step_index == 1:
            keyboard = await variables.keyboards.menu.interactive_nurkhametova_1()
        elif next_step_index == 2:
            keyboard = await variables.keyboards.menu.interactive_nurkhametova_2()
        elif next_step_index == 3:
            keyboard = await variables.keyboards.menu.interactive_nurkhametova_3()
        else:
            keyboard = None

        messages.append(next_text)
        await call.message.edit_text("\n\n".join(messages), reply_markup=keyboard)

    else:
        messages.append("🎉 Это был финальный шаг. Спасибо за участие!")
        await call.message.edit_text("\n\n".join(messages), reply_markup=None)