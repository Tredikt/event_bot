from datetime import datetime

import pytz
from aiogram import Router, F
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery

from core.bot_states import BotStates
from core.utils.answers import answers
from core.utils.enums import Variables

router = Router(name="ending")


@router.callback_query(F.data.startswith("ending"))
async def ending_handler(call: CallbackQuery, state: FSMContext, variables: Variables):
    user_id = call.from_user.id
    review = call.data.split("_")[-1]
    interactive_name = (await state.get_data())["interactive_name"]
    await variables.db.feedback.add_or_update(
        telegram_user_id=user_id,
        name=interactive_name,
        review=answers[review]
    )
    await call.message.edit_text(
        text="Оставь инсайт по поводу выступления спикера в ответ на это сообщение, мы обязательно передадим его спикеру",
        reply_markup=await variables.keyboards.menu.get_empty_keyboard()
    )
    await variables.db.user.update_user_info(
        telegram_user_id=user_id,
        feedback_waiting=datetime.now(pytz.timezone("Europe/Moscow"))
    )
    await state.set_state(BotStates.ending)