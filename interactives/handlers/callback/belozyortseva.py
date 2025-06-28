import asyncio
from aiogram import Router, F
from aiogram.types import CallbackQuery
from aiogram.enums import ChatAction

from core.utils.enums import Variables
from core.utils.answers import belozyortseva_explanations, belozyortseva_next_questions
from core.utils.answer_choices import answer_choices
from core.utils.animate_waiting_message import animate_next_question_loading
from core.utils.scoring_utils import add_user_score

router = Router(name="belozyortseva_router")


@router.callback_query(F.data.startswith("belozyortseva_test_"))
async def belozyortseva_callback_handler(call: CallbackQuery, variables: Variables):
    parts = call.data.split("_")
    number_test = int(parts[-2])
    selected_index = int(parts[-1])

    await call.message.edit_reply_markup(reply_markup=None)
    
    await call.bot.send_chat_action(chat_id=call.message.chat.id, action=ChatAction.TYPING)
    
    await asyncio.sleep(1.5)

    test_data = answer_choices[number_test - 1]
    correct_index = test_data["correct_index"]
    is_correct = selected_index == correct_index

    correct_explanation = belozyortseva_explanations.get(number_test, "")
    if is_correct:
        text = f"✅ Верно!\n\n{correct_explanation}"
        text += await add_user_score(call=call, variables=variables, interactive_name="belozyortseva")
    else:
        text = f"❌ Неверно!\n\n{correct_explanation}"

    await call.message.answer(text=text)

    number_test += 1

    next_question_text = belozyortseva_next_questions.get(number_test)
    if next_question_text:
        await animate_next_question_loading(message=call.message, bot=call.bot)
        
        await call.message.answer(
            text=next_question_text,
            reply_markup=await variables.keyboards.menu.belozyortseva_menu(number_test=number_test)
        )
    await call.answer()