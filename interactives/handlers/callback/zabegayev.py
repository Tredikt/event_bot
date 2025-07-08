import asyncio
from aiogram import Router, F
from aiogram.types import CallbackQuery
from aiogram.enums import ChatAction

from core.utils.enums import Variables
from core.utils.answers import zabegayev_answers
from core.utils.zabegayev_data import buttons_1, buttons_2, zabegayev_correct_answers
from core.utils.animate_waiting_message import animate_next_question_loading, send_animation_one_question
from core.utils.scoring_utils import add_user_score


router = Router(name="zabegayev_callback_router")


@router.callback_query(F.data == "zabegayev_start_interactive")
async def zabegayev_start_interactive(call: CallbackQuery, variables: Variables, current_speaker: str):
    """Обработчик кнопки запуска интерактива - отправляет первый вопрос поэтапно"""
    await call.answer()
    await call.message.delete()
    await asyncio.sleep(1)
    
    await send_animation_one_question(
        call=call,
        variables=variables,
        start_text="<b>Sprinter требует установки \"толстых клиентов\" в каждую систему.</b>",
        question_text="Это правда или миф?",
        buttons_data=buttons_1,
        callback_prefix="zabegayev_question_1"
    )


@router.callback_query(F.data.startswith("zabegayev_question_1_"))
async def zabegayev_question_1(call: CallbackQuery, variables: Variables):
    """Обработчик первого вопроса Забегаева"""
    await call.answer()
    selected_index = int(call.data.split("_")[-1])
    correct_answer_index = zabegayev_correct_answers[1]
    await call.message.edit_reply_markup(reply_markup=None)
    await variables.bot.send_chat_action(chat_id=call.message.chat.id, action=ChatAction.TYPING)
    await asyncio.sleep(2)
    
    if selected_index == correct_answer_index:
        result_text = zabegayev_answers['zabegaev_1']['correct']
        result_text += "\n\n🎯 <i><b>+1 балл.</b> Едем дальше!</i>"
        points = 1
    else:
        result_text = zabegayev_answers['zabegaev_1']['incorrect']
        points = 0
    await add_user_score(call=call, variables=variables, interactive_name="zabegayev_question_1", points=points)

    await call.message.answer(text=result_text)
    await asyncio.sleep(2)
    await animate_next_question_loading(message=call.message, bot=call.bot)
    await send_animation_one_question(
        call=call,
        variables=variables,
        start_text="📍 <b>А теперь так:\nSprinter</b> генерирует сложные документы с динамическими таблицами и условным форматированием, <i>без ручного программирования шаблонов.</i>",
        question_text="<b>Это правда или нет?</b>",
        buttons_data=buttons_2,
        callback_prefix="zabegayev_question_2"
    )


@router.callback_query(F.data.startswith("zabegayev_question_2_"))
async def zabegayev_question_2(call: CallbackQuery, variables: Variables):
    """Обработчик второго вопроса Забегаева"""
    await call.answer()
    selected_index = int(call.data.split("_")[-1])
    correct_answer_index = zabegayev_correct_answers[2]
    await call.message.edit_reply_markup(reply_markup=None)
    await variables.bot.send_chat_action(chat_id=call.message.chat.id, action=ChatAction.TYPING)
    await asyncio.sleep(2)
    
    if selected_index == correct_answer_index:
        result_text = zabegayev_answers['zabegaev_2']['correct']
        result_text += "\n\n🎯 <i><b>+1 балл.</b> Так держать.</i>"
        points = 1
    else:
        result_text = zabegayev_answers['zabegaev_2']['incorrect']
        points = 0
    await add_user_score(call=call, variables=variables, interactive_name="zabegayev_question_2", points=points)

    await call.message.answer(text=result_text)
