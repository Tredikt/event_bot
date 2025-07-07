from aiogram import Router, F
from aiogram.filters import StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from core.bot_states import BotStates
from core.utils.scoring_utils import add_user_score
from core.utils.enums import Variables
from core.utils.interactive_messages import get_feedback_thank_message

router = Router(name="ending_state")


@router.message(F.text, StateFilter(BotStates.ending))
async def ending_state_handler(message: Message, state: FSMContext, variables: Variables):
    user_id = str(message.from_user.id)
    user = await variables.db.user.get_by_telegram_id(telegram_user_id=user_id)
    if user.feedback_waiting:
        interactive_name = (await state.get_data())["interactive_name"]
        await variables.db.feedback.add_or_update(
            telegram_user_id=user_id,
            name=interactive_name,
            inside=message.text,
            rate="insight"
        )
        text = get_feedback_thank_message(interactive_name)
        await add_user_score(call=message, variables=variables, interactive_name=interactive_name + "_ending", points=2)

        await message.answer(text=text, parse_mode="HTML")
        
        await variables.db.user.update_user_info(
            telegram_user_id=user_id,
            feedback_waiting=None,
            current_speaker=None
        )
    await state.clear()