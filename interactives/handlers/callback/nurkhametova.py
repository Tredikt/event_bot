import asyncio
from aiogram import Router, F
from aiogram.types import CallbackQuery
from aiogram.enums import ChatAction

from core.utils.answer_choices import nurkhametova_correct_answers
from core.utils.enums import Variables
from core.utils.nurkhametova_explanation import explanations
from core.utils.nurkhametova_questions import questions
from core.utils.animate_waiting_message import animate_next_question_loading
from core.utils.scoring_utils import add_user_score

router = Router(name="nurkhametova_callback_router")

keyboards = {
    "menu": "nurkhametova_menu",
    "start": "nurkhametova_start",
}


@router.callback_query(F.data.startswith("nurkhametova_menu_"))
async def nurkhametova(call: CallbackQuery, variables: Variables):
    selected_index = int(call.data.split("_")[-1])
    key = "menu"
    correct_text = explanations[key]
    
    await call.message.edit_reply_markup(reply_markup=None)
    
    await call.bot.send_chat_action(chat_id=call.message.chat.id, action=ChatAction.TYPING)
    
    await asyncio.sleep(1.5)
    
    is_correct = selected_index == nurkhametova_correct_answers[key]
    
    if not is_correct:
        text = f"❌ Неверно!\n\n{correct_text}"
    else:
        text = f"✅ Верно!\n\n{correct_text}"
        text += await add_user_score(call=call, variables=variables, interactive_name="nurkhametova")
        
    await call.message.answer(text=text)
    
    await animate_next_question_loading(message=call.message, bot=call.bot)
    
    await call.message.answer(
        text=questions["start"],
        reply_markup=await getattr(variables.keyboards.menu, keyboards["start"])()
    )
    await call.answer()


@router.callback_query(F.data.startswith("nurkhametova_start_"))
async def nurkhametova1(call: CallbackQuery, variables: Variables):
    selected_index = int(call.data.split("_")[-1])
    key = "start"
    correct_text = explanations[key]
    
    await call.message.edit_reply_markup(reply_markup=None)
    
    await call.bot.send_chat_action(chat_id=call.message.chat.id, action=ChatAction.TYPING)
    
    await asyncio.sleep(1.5)
    
    is_correct = selected_index == nurkhametova_correct_answers[key]
    
    if not is_correct:
        text = f"❌ Неверно!\n\n{correct_text}"
    else:
        text = f"✅ Верно!\n\n{correct_text}"
        text += await add_user_score(call=call, variables=variables, interactive_name="nurkhametova")
        
    await call.message.answer(text=text)
    await call.answer()
