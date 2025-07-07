import asyncio
from aiogram import Router, F
from aiogram.types import CallbackQuery
from aiogram.types import CallbackQuery
from aiogram.enums import ChatAction

from core.utils.enums import Variables
from core.utils.answers import belozyortseva_explanations, belozyortseva_next_questions
from core.utils.answer_choices import answer_choices
from core.utils.animate_waiting_message import animate_next_question_loading, send_animation_one_question
from core.utils.scoring_utils import add_user_score


router = Router(name="belozyortseva_router")


@router.callback_query(F.data == "start_belozyortseva_interactive")
async def start_belozyortseva_interactive(call: CallbackQuery, variables: Variables):
    """Обработчик кнопки запуска интерактива - отправляет первый вопрос поэтапно"""
    await call.answer()
    await call.message.delete()
    await asyncio.sleep(1)
    
    test_data = answer_choices[0]
    options = test_data["options"]
    buttons_data = {
        option: f"belozyortseva_test_1_{idx}"
        for idx, option in enumerate(options)
    }
    
    await send_animation_one_question(
        call=call,
        variables=variables,
        start_text="А вот и первый вопрос...",
        question_text="<b>Бэкенд сервиса делится на две главные части.</b> Вопрос на внимательность — <b>какие именно?</b>",
        buttons_data=buttons_data,
        callback_prefix="belozyortseva_test_1"
    )


@router.callback_query(F.data.startswith("belozyortseva_test_"))
async def belozyortseva_callback_handler(call: CallbackQuery, variables: Variables):
    await call.answer()
    
    parts = call.data.split("_")
    number_test = int(parts[-2])
    selected_index = int(parts[-1])

    await call.message.edit_reply_markup(reply_markup=None)
    await call.bot.send_chat_action(chat_id=call.message.chat.id, action=ChatAction.TYPING)
    await asyncio.sleep(3.5)

    test_data = answer_choices[number_test - 1]
    correct_index = test_data["correct_index"]
    is_correct = selected_index == correct_index
    explanation_data = belozyortseva_explanations.get(number_test, {})

    if is_correct:
        text = explanation_data.get("correct", "✅ Верно!")
        text += "\n\n🎉 <b>+1 балл!</b>"
        points = 1
    else:
        text = explanation_data.get("incorrect", "❌ Неверно!")
        points = 0
    await add_user_score(call=call, variables=variables, interactive_name="belozyortseva_question_" + str(number_test), points=points)

    await call.message.answer(text=text, parse_mode="HTML")
    number_test += 1
    await asyncio.sleep(2)
    next_question_text = belozyortseva_next_questions.get(number_test)
    
    if next_question_text:
        if number_test == 2:
            await _send_second_question_sequence(call, variables)
        else:
            await animate_next_question_loading(message=call.message, bot=call.bot)
            
            await call.message.answer(
                text=next_question_text,
                reply_markup=await variables.keyboards.menu.belozyortseva_menu(number_test=number_test)
            )


async def _send_second_question_sequence(call: CallbackQuery, variables: Variables):
    """Отправляет поэтапную последовательность для второго вопроса"""
    await animate_next_question_loading(message=call.message, bot=call.bot)
    
    test_data = answer_choices[1]  # Второй тест (индекс 1)
    options = test_data["options"]
    
    buttons_data = {
        option: f"belozyortseva_test_2_{idx}"
        for idx, option in enumerate(options)
    }
    
    await send_animation_one_question(
        call=call,
        variables=variables,
        start_text="Второй вопрос...",
        question_text="<b>Фронтенд</b> — это адаптивное веб-приложение, которое <b>общается с сервером через</b>",
        buttons_data=buttons_data,
        callback_prefix="belozyortseva_test_2"
    )