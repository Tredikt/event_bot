
from aiogram import Router, F
from aiogram.enums import InputMediaType
from aiogram.filters import StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, InputMediaPhoto



from interactives.fsm.interactives import InteractivesStates

router = Router(name="zargaryan_state_router")


@router.message(F.text, StateFilter(InteractivesStates.zargaryan))
async def zargaryan(message: Message, state: FSMContext):
    text = "Круто, спроси что-то ещё"
    await message.answer(
        text=text
    )
