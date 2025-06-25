from aiogram import Router, F
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, CallbackQuery

from core.utils.enums import Variables
from interactives.fsm.interactives import InteractivesStates

router = Router(name="zargaryan_callback_router")

@router.callback_query(F.data == "zargaryan")
async def zarharyan_start(call: CallbackQuery, state: FSMContext):
    await state.set_state(BotStates.base)
    await state.update_data(interactive_name="zargaryan")
    await state.set_state(InteractivesStates.zargaryan)
    text = "Задавайте вопросы спикеру, отправляйте их в ответа на это сообщение прямо в чат, ваши вопросы будут выводиться на экран, так что несколько раз подумайте)"
    await call.massage.edit_text(
        text=text
    )