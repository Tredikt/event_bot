import asyncio

import pytz
from datetime import datetime

from aiogram import Router, F
from aiogram.filters import StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.types import Message
from aiogram.enums import ChatAction


from core.bot_states import BotStates
from core.utils.enums import Variables
from core.utils.interactive_messages import get_speaker_insight_message

router = Router(name="ask_speaker_state")


@router.message(F.text, StateFilter(BotStates.ask_speaker))
async def ask_speaker_state_handler(message: Message, state: FSMContext, variables: Variables):
    interactive_name = (await state.get_data())["interactive_name"]
    user_id = str(message.from_user.id)

    await variables.db.question.add(
        user_id=user_id,
        interactive_name=interactive_name,
        body=message.text
    )
    await variables.bot.send_chat_action(chat_id=user_id, action=ChatAction.TYPING)
    await asyncio.sleep(1)
    await state.clear()
    
    insight_text = get_speaker_insight_message(interactive_name)
    await message.answer(
        text=insight_text,
        reply_markup=await variables.keyboards.menu.get_empty_keyboard(),
        parse_mode="HTML"
    )
    await variables.db.user.update_user_info(
        telegram_user_id=user_id,
        # feedback_waiting=datetime.now(pytz.timezone("Europe/Moscow"))
        feedback_waiting=datetime.now(),
        current_speaker=interactive_name
    )
    await state.set_state(BotStates.ending)
    await state.update_data(interactive_name=interactive_name)
