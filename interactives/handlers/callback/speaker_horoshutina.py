from aiogram import Router, F
from aiogram.types import CallbackQuery

from core.utils.enums import Variables
from core.utils.answer_choices import horoshutina_sequence
from core.utils.decorators import admin_interactive
from interactives.states.horoshutina_states import HoroshutinaState


async def get_word_by_id(word_id: int) -> str | None:
    for item in horoshutina_sequence:
        if item["id"] == word_id:
            return item["word"]
    return None


router = Router(name="speaker_horoshutina_callback")


@router.callback_query(F.data == "interactive_horoshutina")
@admin_interactive
async def start_horoshutina_interactive(callback: CallbackQuery, variables: Variables):
    user_id = callback.from_user.id
    
    if user_id in variables.keyboards.menu.horoshutina_states and variables.keyboards.menu.horoshutina_states[user_id] is not None:
        await variables.keyboards.menu.horoshutina_states[user_id].reset()
    
    await callback.message.answer(
        text="🎯 Расставьте правильную последовательность этапов продаж:",
        reply_markup=await variables.keyboards.menu.interactive_horoshutina(user_id=user_id)
    )


@router.callback_query(F.data.startswith("horoshutina_"))
async def process_horoshutina_selection(callback: CallbackQuery, variables: Variables):
    user_id = callback.from_user.id
    selected_id = callback.data.replace("horoshutina_", "")
    
    if user_id not in variables.keyboards.menu.horoshutina_states or variables.keyboards.menu.horoshutina_states[user_id] is None:
        await callback.answer("❌ Интерактив не активен")
        return
    
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
        telegram_user_id = str(callback.from_user.id)
        
        current_rating = await variables.db.interactive_service.complete_interactive(
            telegram_user_id=telegram_user_id,
            username=callback.from_user.username,
            first_name=callback.from_user.first_name,
            interactive_name="horoshutina",
            points=1
        )
        
        await callback.message.answer(f"🎉 +1 балл! Ваш рейтинг: {current_rating}")
    
    await callback.answer()


async def handle_correct_selection(state: HoroshutinaState, selected_word: str) -> None:
    """Обработка правильного выбора"""
    await state.complete_step(word=selected_word)


@router.callback_query(F.data == "horoshutina_completed")
async def horoshutina_completed_handler(callback: CallbackQuery):
    await callback.answer("🎉 Интерактив завершен!")


@router.callback_query(F.data == "finished_horoshutina")
@admin_interactive
async def finished_horoshutina(callback: CallbackQuery, variables: Variables):
    """Отметка о завершении выступления Хорошутиной"""
    await callback.message.answer("📢 Хорошутина закончила выступление!")