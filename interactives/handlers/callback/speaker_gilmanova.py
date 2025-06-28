import asyncio

from aiogram import Router, F
from aiogram.enums import ChatAction
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery

from core.bot_states import BotStates
from core.utils.enums import Variables
from interactives.states.gilmanova_states import GilmanovaState


router = Router(name="speaker_gilmanova_callback")


@router.callback_query(F.data == "start_gilmanova")
async def start_gilmanova_interactive(callback: CallbackQuery, state: FSMContext, variables: Variables):
    await callback.message.edit_reply_markup(reply_markup=None)
    
    await variables.bot.send_chat_action(chat_id=callback.message.chat.id, action=ChatAction.TYPING)
    
    await asyncio.sleep(1.5)
    user_id: int = callback.from_user.id

    if not hasattr(variables.keyboards.menu, 'gilmanova_states'):
        variables.keyboards.menu.gilmanova_states = {}

    gilmanova_state_service = GilmanovaState()
    await gilmanova_state_service.start_interactive()
    variables.keyboards.menu.gilmanova_states[user_id] = gilmanova_state_service

    await callback.answer()
    await callback.message.answer(text="Как вы думаете, что мы сделали?")
    await state.set_state(BotStates.gilmanova)
