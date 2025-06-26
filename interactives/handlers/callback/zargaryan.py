from aiogram import Router, F
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, CallbackQuery

from core.bot_states import BotStates
from core.utils.enums import Variables

from event_bot.interactives.fsm.interactives import InteractivesStates

router = Router(name="zargaryan_callback_router")


@router.callback_query(F.data == "zargaryan")
async def zargaryan_start(call: CallbackQuery, state: FSMContext):
    await state.set_state(InteractivesStates.zargaryan)
    text = "Задавайте вопросы спикеру, отправляйте их в ответа на это сообщение прямо в чат, ваши вопросы будут выводиться на экран, так что несколько раз подумайте)"
    await call.message.edit_text(
        text=text
    )