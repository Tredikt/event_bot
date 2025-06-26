from aiogram import Router, F
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery, Message
from aiogram.utils.keyboard import InlineKeyboardBuilder

from core.utils.enums import Variables
from core.utils.decorators import admin_interactive
from interactives.fsm.interactives import InteractivesStates

router = Router(name="zargaryan_callback_router")


QUESTIONS = [
    "Почему заказчик купит именно решение БАРС?",
    "Разве федералы уже не сделали такую систему: Все регионы сдают им отчетность.",
    "Какая стоимость данного решения сейчас? Какие сроки внедрения?"
]


class ZargaryanState:
    def __init__(self):
        self.current_question = 0
        self.answers = []


@router.callback_query(F.data == "answer_questions_zargaryan")
async def zargaryan_start(call: CallbackQuery, state: FSMContext, variables: Variables):
    await call.message.delete()
    user_id = call.from_user.id

    if not hasattr(variables.keyboards.menu, 'zargaryan_states'):
        variables.keyboards.menu.zargaryan_states = {}
    
    # Создаем состояние для пользователя, если его еще нет
    if user_id not in variables.keyboards.menu.zargaryan_states:
        variables.keyboards.menu.zargaryan_states[user_id] = ZargaryanState()
    
    # Отправляем первый вопрос
    state_data = variables.keyboards.menu.zargaryan_states[user_id]
    await call.message.answer(
        text=f"Вопрос {state_data.current_question + 1}:\n{QUESTIONS[state_data.current_question]}"
    )
    await state.set_state(InteractivesStates.zargaryan)
    await call.answer()


@router.callback_query(F.data == "finished_zargaryan")
@admin_interactive
async def finished_zargaryan(call: CallbackQuery, variables: Variables, state: FSMContext):
    user_id = call.from_user.id
    if hasattr(variables.keyboards.menu, 'zargaryan_states') and user_id in variables.keyboards.menu.zargaryan_states:
        del variables.keyboards.menu.zargaryan_states[user_id]
    await call.message.answer(text="📢 Заргарян закончил выступление!")
    await state.clear()