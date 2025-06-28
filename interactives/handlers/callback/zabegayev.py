import asyncio
from aiogram import Router, F
from aiogram.types import CallbackQuery
from aiogram.enums import ChatAction

from core.utils.enums import Variables
from core.utils.answers import zabegayev_answers
from core.utils.animate_waiting_message import animate_next_question_loading
from core.utils.scoring_utils import add_user_score


router = Router(name="zabegayev_callback_router")


@router.callback_query(F.data.startswith("start_zabegayev_"))
async def start_zabegayev(call: CallbackQuery, variables: Variables):
    mode = call.data.split("_")[-1]
    
    await call.message.edit_reply_markup(reply_markup=None)
    
    await variables.bot.send_chat_action(chat_id=call.message.chat.id, action=ChatAction.TYPING)
    
    await asyncio.sleep(1.5)
    
    if mode == "false":
        text = f"❌ Неверно!\n\n{zabegayev_answers['zabegaev_1']}"
    else:
        text = f"✅ Верно!\n\n{zabegayev_answers['zabegaev_1']}"
        text += await add_user_score(call=call, variables=variables, interactive_name="zabegayev")
    
    await call.message.answer(text=text)
    
    await animate_next_question_loading(message=call.message, bot=variables.bot)
    
    keyboard = await variables.keyboards.menu.zabegayev_1()
    await call.message.answer(
        text="Настройка Sprinter под госсистемы (например, 'Электронный бюджет') занимает 3+ месяца из-за сложной интеграции",
        reply_markup=keyboard
    )
    await call.answer()


@router.callback_query(F.data.startswith("zabegayev_1_"))
async def zabegayev_2(call: CallbackQuery, variables: Variables):
    mode = call.data.split("_")[-1]
    
    await call.message.edit_reply_markup(reply_markup=None)
    
    await variables.bot.send_chat_action(chat_id=call.message.chat.id, action=ChatAction.TYPING)
    
    await asyncio.sleep(1.5)
    
    if mode == "false":
        text = f"❌ Миф!\n\n{zabegayev_answers['zabegaev_2']}"
    else:
        text = f"✅ Верно!\n\n{zabegayev_answers['zabegaev_2']}"
        text += await add_user_score(call=call, variables=variables, interactive_name="zabegayev")

    await call.message.answer(text=text)
    await call.answer()
