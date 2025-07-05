import asyncio
from aiogram import Router, F
from aiogram.types import CallbackQuery

from core.utils.enums import Variables
from core.utils.answers import sadriev_answers
from core.utils.sadriev_data import buttons_1, sadriev_correct_answers
from core.utils.animate_waiting_message import animate_answer_analysis, send_animation_one_question
from core.utils.scoring_utils import add_user_score


router = Router(name="speaker_sadriev_callback")


@router.callback_query(F.data == "sadriev_start_interactive")
async def sadriev_start_interactive(call: CallbackQuery, variables: Variables):
    """Обработчик кнопки запуска интерактива - отправляет вопрос поэтапно"""
    await call.answer()
    await call.message.delete()
    await asyncio.sleep(1)
    
    await send_animation_one_question(
        call=call,
        variables=variables,
        start_text="Как думаешь:",
        question_text="<b>Сколько кибератак было зарегистрировано в России в 2024 году?</b>",
        buttons_data=buttons_1,
        callback_prefix="sadriev_question_1"
    )


@router.callback_query(F.data.startswith("sadriev_question_1_"))
async def sadriev_question_1(call: CallbackQuery, variables: Variables):
    """Обработчик вопроса Садриева"""
    await call.answer()
    selected_index = int(call.data.split("_")[-1])
    correct_answer_index = sadriev_correct_answers[1]
    await call.message.edit_reply_markup(reply_markup=None)
    await animate_answer_analysis(message=call.message, bot=variables.bot)
    
    if selected_index == correct_answer_index:
        result_text = sadriev_answers["correct"]
        await add_user_score(call=call, variables=variables, interactive_name="sadriev")
    else:
        result_text = sadriev_answers["incorrect"]
    
    await call.message.answer(text=result_text, parse_mode="HTML")
