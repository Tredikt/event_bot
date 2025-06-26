from aiogram import Router, F
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery

from core.bot_states import BotStates
from core.utils.enums import Variables
from core.utils.decorators import admin_interactive
from interactives.states.gilmanova_states import GilmanovaState


router = Router(name="speaker_gilmanova_callback")


@router.callback_query(F.data == "start_gilmanova")
async def start_gilmanova_interactive(callback: CallbackQuery, state: FSMContext, variables: Variables):
    user_id: int = callback.from_user.id

    if not hasattr(variables.keyboards.menu, 'gilmanova_states'):
        variables.keyboards.menu.gilmanova_states = {}

    gilmanova_state_service = GilmanovaState()
    await gilmanova_state_service.start_interactive()
    variables.keyboards.menu.gilmanova_states[user_id] = gilmanova_state_service

    await callback.answer()
    await callback.message.answer(text="Как вы думаете, что мы сделали?")
    await state.set_state(BotStates.gilmanova)


@router.callback_query(F.data.startswith("gilmanova_"))
async def process_gilmanova_button(callback: CallbackQuery, variables: Variables):
    """Обрабатывает нажатие кнопок интерактива, если они есть"""
    user_id: int = callback.from_user.id
    
    if not hasattr(variables.keyboards.menu, 'gilmanova_states'):
        variables.keyboards.menu.gilmanova_states = {}
    
    if user_id not in variables.keyboards.menu.gilmanova_states:
        variables.keyboards.menu.gilmanova_states[user_id] = GilmanovaState()
        state = variables.keyboards.menu.gilmanova_states[user_id]
        await state.start_interactive()
    
    await callback.answer(text="Пожалуйста, ответьте текстом в чат 📝")


@router.callback_query(F.data == "finished_gilmanova")
@admin_interactive
async def finished_gilmanova(callback: CallbackQuery, variables: Variables):
    await callback.message.answer(text="📢 Гильманова закончила выступление!")
