import asyncio

from aiogram import Router, F
from aiogram.enums import ChatAction
from aiogram.types import CallbackQuery

from core.utils.enums import Variables
from core.utils.answer_choices import horoshutina_sequence
from core.utils.scoring_utils import add_user_score
from interactives.states.horoshutina_states import HoroshutinaState
from core.utils.animate_waiting_message import send_animation_one_question


async def get_word_by_id(word_id: int) -> str | None:
    for item in horoshutina_sequence:
        if item["id"] == word_id:
            return item["word"]
    return None


def create_horoshutina_buttons():
    """Создает кнопки для интерактива Хорошутиной"""
    buttons = {}
    for item in horoshutina_sequence:
        word = item["word"]
        word_id = item["id"]
        buttons[word] = f"horoshutina_{word_id}"
    return buttons


router = Router(name="speaker_horoshutina_callback")


@router.callback_query(F.data == "horoshutina_start_interactive")
async def horoshutina_start_interactive(call: CallbackQuery, variables: Variables, current_speaker: str):
    """Обработчик кнопки запуска интерактива - отправляет вопрос поэтапно"""
    if current_speaker != call.data.split("_")[1]:
        kb = await variables.keyboards.menu.get_empty_keyboard()
        await call.message.edit_reply_markup(reply_markup=kb)
        await call.answer(show_alert=True, text="Данный спикер уже не выступает. Невозможно начать данный интерактив")
        return
    else:
        await call.answer()
        await call.message.delete()
        await asyncio.sleep(1)
    
    user_id = call.from_user.id
    if user_id in variables.keyboards.menu.horoshutina_states:
        await variables.keyboards.menu.horoshutina_states[user_id].reset()
    else:
        variables.keyboards.menu.horoshutina_states[user_id] = HoroshutinaState()
    
    buttons_data = create_horoshutina_buttons()
    
    await send_animation_one_question(
        call=call,
        variables=variables,
        start_text="Пора проверить ваши знания по продажам!",
        question_text="<b>Соберите правильную цепочку «шагов продаж»:</b>",
        buttons_data=buttons_data,
        callback_prefix="horoshutina"
    )


@router.callback_query(F.data.startswith("horoshutina_"))
async def process_horoshutina_selection(callback: CallbackQuery, variables: Variables):
    user_id = callback.from_user.id
    selected_id = callback.data.replace("horoshutina_", "")
    
    if user_id not in variables.keyboards.menu.horoshutina_states or variables.keyboards.menu.horoshutina_states[user_id] is None:
        variables.keyboards.menu.horoshutina_states[user_id] = HoroshutinaState()
    
    state: HoroshutinaState = variables.keyboards.menu.horoshutina_states[user_id]
    selected_word = await get_word_by_id(word_id=selected_id)
    expected_word = await state.get_expected_word(sequence_data=horoshutina_sequence)
    
    if selected_word == expected_word:
        await handle_correct_selection(state=state, selected_word=selected_word)
    else:
        await state.add_wrong_selection(word=selected_word)
    
    new_keyboard = await variables.keyboards.menu.interactive_horoshutina(user_id=user_id)
    await callback.message.edit_reply_markup(reply_markup=new_keyboard)
    
    if await state.is_completed():
        await callback.message.delete()
        await _send_sales_stages_sequentially(callback, variables)
    
    await callback.answer()


async def handle_correct_selection(state: HoroshutinaState, selected_word: str) -> None:
    """Обработка правильного выбора"""
    await state.complete_step(word=selected_word)


async def _send_sales_stages_sequentially(callback: CallbackQuery, variables: Variables) -> None:
    """Отправляет этапы продаж построчно с анимацией в одном редактируемом сообщении"""
    await variables.bot.send_chat_action(chat_id=callback.message.chat.id, action=ChatAction.TYPING)
    await asyncio.sleep(1.5)
    
    current_text = "🔥 <b>Прекрасно!</b> Всё выстроено правильно — ты точно в фокусе.\n\n✅ <b>Этапы идут в такой последовательности:</b>"
    message = await callback.message.answer(text=current_text, parse_mode="HTML")
    sales_stages = [
        "1️⃣ Выявление потребности",
        "2️⃣ Показ", 
        "3️⃣ Демоиспользование",
        "4️⃣ Дожим",
        "5️⃣ Итоговое формирование условий",
        "6️⃣ Контрактование"
    ]
    
    for stage in sales_stages:
        await asyncio.sleep(1.2)
        await variables.bot.send_chat_action(chat_id=callback.message.chat.id, action=ChatAction.TYPING)
        await asyncio.sleep(0.8)
        
        current_text += f"\n\n{stage}"
        await message.edit_text(text=current_text)
    
    await asyncio.sleep(1.5)
    await variables.bot.send_chat_action(chat_id=callback.message.chat.id, action=ChatAction.TYPING)
    await asyncio.sleep(0.8)
    
    current_text += "\n\n🎉 <i><b>+1 балл</b></i>"
    await add_user_score(call=callback, variables=variables, interactive_name="horoshutina_question_1", points=2)
    await message.edit_text(text=current_text)
