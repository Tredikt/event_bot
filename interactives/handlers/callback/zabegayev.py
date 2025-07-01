import asyncio
from aiogram import Router, F
from aiogram.types import CallbackQuery
from aiogram.enums import ChatAction

from core.utils.enums import Variables
from core.utils.answers import zabegayev_answers
from core.utils.zabegayev_data import buttons_1, buttons_2, zabegayev_correct_answers
from core.utils.animate_waiting_message import animate_next_question_loading, send_staged_question
from core.utils.scoring_utils import add_user_score


router = Router(name="zabegayev_callback_router")


@router.callback_query(F.data == "zabegayev_start_interactive")
async def zabegayev_start_interactive(call: CallbackQuery, variables: Variables):
    """Обработчик кнопки запуска интерактива - отправляет первый вопрос поэтапно"""
    await call.answer()
    await call.message.delete()
    await asyncio.sleep(1)
    
    await send_staged_question(
        call=call,
        variables=variables,
        start_text="Вопрос....",
        main_text="Legacy-решения требуют сложной установки и настройки.",
        question_text="Правда или ложь?",
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
        result_text = f"✅ Верно!\n\n{zabegayev_answers['zabegaev_1']}"
        result_text += await add_user_score(call=call, variables=variables, interactive_name="zabegayev")
    else:
        result_text = f"❌ Неверно!\n\n{zabegayev_answers['zabegaev_1']}"
    
    await call.message.answer(text=result_text)
    await asyncio.sleep(2)
    await animate_next_question_loading(message=call.message, bot=call.bot)
    await send_staged_question(
        call=call,
        variables=variables,
        start_text="Следующий вопрос:\n\nНастройка Sprinter под госсистемы",
        main_text="(например, 'Электронный бюджет') занимает 3+ месяца из-за сложной интеграции.",
        question_text="Правда или ложь?",
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
        result_text = f"✅ Верно!\n\n{zabegayev_answers['zabegaev_2']}"
        result_text += await add_user_score(call=call, variables=variables, interactive_name="zabegayev")
    else:
        result_text = f"❌ Миф!\n\n{zabegayev_answers['zabegaev_2']}"
    
    await call.message.answer(text=result_text)
