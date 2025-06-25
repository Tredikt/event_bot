
from aiogram import Router, F
from aiogram.enums import InputMediaType
from aiogram.filters import StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, InputMediaPhoto

from core.utils.enums import Variables
from interactives.fsm.interactives import InteractivesStates

router = Router(name="zargaryan_state_router")


@router.message(F.text, StateFilter(InteractivesStates.zargaryan))
async def zargaryan(message: Message, variables: Variables):
    text = "Круто, спроси что-то ещё"
    await message.answer(
        text=text
    )
    await message.answer(
        text="Как вам это выступление? / материалы спикера в easy",
        reply_markup=await variables.keyboards.menu.ending()
    )
