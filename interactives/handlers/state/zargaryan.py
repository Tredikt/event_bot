from aiogram import Router, F
from aiogram.filters import StateFilter
from aiogram.types import Message
from aiogram.fsm.context import FSMContext

from event_bot.interactives.fsm.interactives import InteractivesStates

# путь к твоему классу состояний

router = Router(name="zargaryan_state_router")

# Хендлер для текстовых сообщений в состоянии zargaryan
@router.message(F.text, StateFilter(InteractivesStates.zargaryan))
async def handle_zargaryan_message(message: Message):
    await message.answer("Круто, спроси что-то ещё")