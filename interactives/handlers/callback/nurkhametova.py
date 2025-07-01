import asyncio
from aiogram import Router, F
from aiogram.types import CallbackQuery
from aiogram.enums import ChatAction

from core.utils.answer_choices import nurkhametova_correct_answers
from core.utils.enums import Variables
from core.utils.nurkhametova_data import explanations, buttons_1, buttons_2
from core.utils.animate_waiting_message import animate_next_question_loading, send_staged_question
from core.utils.scoring_utils import add_user_score


router = Router(name="nurkhametova_callback_router")


@router.callback_query(F.data == "nurkhametova_start_interactive")
async def nurkhametova_start_interactive(call: CallbackQuery, variables: Variables):
    """Обработчик кнопки запуска интерактива - отправляет первый вопрос поэтапно"""
    await call.answer()
    await call.message.delete()
    await asyncio.sleep(1)
    
    await send_staged_question(
        call=call,
        variables=variables,
        start_text="После развода",
        main_text="отец запрещает матери видеться с ребёнком без причины.",
        question_text="Это ущемляет ______ родителя",
        buttons_data=buttons_1,
        callback_prefix="nurkhametova_question_1"
    )


@router.callback_query(F.data.startswith("nurkhametova_question_1_"))
async def nurkhametova(call: CallbackQuery, variables: Variables):
    await call.answer()
    selected_index = int(call.data.split("_")[-1])
    key = "question_1"
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
    await asyncio.sleep(2)
    await animate_next_question_loading(message=call.message, bot=call.bot)
    await send_staged_question(
        call=call,
        variables=variables,
        start_text="Следующий вопрос:\n\nМигранта депортировали,",
        main_text="не дав возможности обжаловать решение.",
        question_text="Какое право нарушено?",
        buttons_data=buttons_2,
        callback_prefix="nurkhametova_question_2"
    )


@router.callback_query(F.data.startswith("nurkhametova_question_2_"))
async def nurkhametova1(call: CallbackQuery, variables: Variables):
    await call.answer()
    selected_index = int(call.data.split("_")[-1])
    key = "question_2"
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
