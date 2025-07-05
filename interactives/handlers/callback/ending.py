from aiogram import Router, F
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery
from aiogram.enums import ChatAction
import asyncio

from core.utils.answers import answers
from core.utils.interactive_messages import get_speaker_insight_message, get_feedback_message
from core.utils.enums import Variables
from core.bot_states import BotStates
from datetime import datetime

router = Router()


@router.callback_query(F.data.startswith("ending"))
async def ending_handler(call: CallbackQuery, state: FSMContext, variables: Variables):
    user_id = str(call.from_user.id)
    data = call.data.split("_")
    rate = data[-1]
    interactive_name = data[-2]
    await variables.db.feedback.add_or_update(
        telegram_user_id=user_id,
        name=interactive_name,
        rate=answers[rate]
    )
    await variables.bot.send_chat_action(chat_id=user_id, action=ChatAction.TYPING)
    await asyncio.sleep(1)
    
    text = get_feedback_message(interactive_name)
    await call.message.delete()
    await call.message.answer(text=text, parse_mode="HTML")
    await variables.bot.send_chat_action(chat_id=user_id, action=ChatAction.TYPING)
    await asyncio.sleep(1)
    
    insight_text = get_speaker_insight_message(interactive_name)
    await call.message.answer(
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


@router.callback_query(F.data.startswith("ask_speaker"))
async def ask_speaker_handler(call: CallbackQuery, state: FSMContext, variables: Variables):
    user_id = str(call.from_user.id)
    interactive_name = call.data.split("_")[-1]
    
    await variables.bot.send_chat_action(chat_id=call.from_user.id, action=ChatAction.TYPING)
    await asyncio.sleep(1)
    
    insight_text = get_speaker_insight_message(interactive_name)
    await call.message.delete()
    await call.message.answer(
        text=insight_text,
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
