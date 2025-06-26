from aiogram import Router, F
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, CallbackQuery

from core.bot_states import BotStates
from core.utils.enums import Variables
from core.utils.zabegayev_steps import zabegayev_steps

router = Router(name="zabegaev_callback_router")


@router.callback_query(F.data == "zabegayev")
async def start_zabegayev(call: CallbackQuery, state: FSMContext, variables: Variables):
    await state.set_state(BotStates.base)
    await state.update_data(interactive_name="zabegayev")
    step = "0"
    keyboard = await variables.keyboards.menu.zabegayev(step)
    text = zabegayev_steps[step]["question"]
    await call.message.edit_text(text=text, reply_markup=keyboard)

@zabegayev_router.callback_query(F.data == "zabegayev")
async def zabegayev(call: CallbackQuery, state: FSMContext, variables: Variables):
    await state.set_state(BotStates.base)
    await state.update_data(interactive_name="zabegayev")
    text = "Sprinter требует установки толстых клиентов в каждую систему"
    keyboard = await variables.keyboards.menu.start_zabegayev()
    await call.message.edit_text(
        text=text,
        reply_markup=keyboard
    )

@router.callback_query(F.data.startswith("zabegayev_"))
async def handle_step(call: CallbackQuery, variables: Variables):
    parts = call.data.split("_")
    if len(parts) != 3:
        await call.answer("Некорректные данные", show_alert=True)
        return

    step, answer = parts[1], parts[2]
    current = zabegayev_steps.get(step)

    if not current:
        await call.answer("Неизвестный шаг", show_alert=True)
        return

    response = ""

    if answer != current["correct"]:
        response += current["wrong_feedback"] + "\n\n"

    next_step = current["next"]
    if next_step:
        next_text = zabegayev_steps[next_step]["question"]
        keyboard = await variables.keyboards.menu.zabegayev(next_step)
        response += next_text
        await call.message.edit_text(text=response, reply_markup=keyboard)
    else:
        response += "🎉 Это был финальный шаг. Спасибо за участие!"
        await call.message.edit_text(text=response, reply_markup=None)
        await call.edit_text(
            text="Как вам это выступление? / материалы спикера в easy",
            reply_markup=await variables.keyboards.menu.ending()
        )