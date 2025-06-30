from aiogram import Router, F
from aiogram.filters import StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from core.bot_states import BotStates
from core.utils.enums import Variables

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
    await message.answer(
        text="Оставь инсайт по поводу выступления спикера в ответ на это сообщение, мы обязательно передадим его спикеру",
        reply_markup=await variables.keyboards.menu.get_empty_keyboard()
    )
    await state.set_state(BotStates.ending)
    await state.update_data(interactive_name=interactive_name)
