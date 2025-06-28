import asyncio
from aiogram import Router, F
from aiogram.types import CallbackQuery

from core.utils.enums import Variables
from core.utils.answers import sadriev_answers
from core.utils.answer_choices import sadriev_test
from core.utils.animate_waiting_message import animate_answer_analysis
from core.utils.scoring_utils import add_user_score


router = Router(name="speaker_sadriev_callback")


@router.callback_query(F.data.startswith("sadriev_test_"))
async def process_sadriev_test(callback: CallbackQuery, variables: Variables):
    selected_index = int(callback.data.split("_")[-1])
    
    await callback.message.edit_reply_markup(reply_markup=None)
        
    await animate_answer_analysis(message=callback.message, bot=variables.bot)

    correct_index = sadriev_test["correct_index"]
    is_correct = selected_index == correct_index

    if is_correct:
        text = f"✅ Верно!\n\n{sadriev_answers['sadriev_answer']}"
        text += await add_user_score(callback, variables, "sadriev")
    else:
        text = f"❌ Неверно :(\n\nПравильный ответ: {sadriev_answers['sadriev_answer']}"
    
    await callback.message.answer(text=text)
    await callback.answer()
