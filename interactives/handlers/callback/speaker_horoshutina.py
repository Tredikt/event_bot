from aiogram import Router, F
from aiogram.types import CallbackQuery

from core.utils.enums import Variables
from core.utils.answer_choices import horoshutina_sequence
from core.utils.decorators import admin_interactive


def get_word_by_id(word_id):
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
        variables.keyboards.menu.horoshutina_states[user_id].reset()
    
    await callback.message.answer(
        text="🎯 Расставьте правильную последовательность этапов продаж:",
        reply_markup=await variables.keyboards.menu.interactive_horoshutina(user_id)
    )


@router.callback_query(F.data.startswith("horoshutina_"))
async def process_horoshutina_selection(callback: CallbackQuery, variables: Variables):
    user_id = callback.from_user.id
    selected_id = callback.data.replace("horoshutina_", "")
    
    if user_id not in variables.keyboards.menu.horoshutina_states or variables.keyboards.menu.horoshutina_states[user_id] is None:
        await callback.answer("❌ Интерактив не активен")
        return
    
    state = variables.keyboards.menu.horoshutina_states[user_id]
    selected_word = get_word_by_id(selected_id)
    expected_word = state.get_expected_word(horoshutina_sequence)
    
    if selected_word == expected_word:
        handle_correct_selection(state, selected_word)
    else:
        state.add_wrong_selection(selected_word)
    
    new_keyboard = await variables.keyboards.menu.interactive_horoshutina(user_id)
    await callback.message.edit_reply_markup(reply_markup=new_keyboard)
    
    if state.is_completed():
        user = await variables.db.user.add_or_get(
            telegram_user_id=str(callback.from_user.id),
            username=callback.from_user.username,
            first_name=callback.from_user.first_name
        )
        
        await variables.db.user.add_points(
            telegram_user_id=str(callback.from_user.id),
            points=1,
            interactive_name="horoshutina"
        )
        
        current_rating = await variables.db.user.get_user_rating(str(callback.from_user.id))
        await callback.message.answer(f"🎉 +1 балл! Ваш рейтинг: {current_rating}")
    
    await callback.answer()


def handle_correct_selection(state, selected_word):
    state.complete_step(selected_word)


@router.callback_query(F.data == "horoshutina_completed")
async def horoshutina_completed_handler(callback: CallbackQuery):
    await callback.answer("🎉 Интерактив завершен!")


@router.callback_query(F.data == "finished_horoshutina")
@admin_interactive
async def finished_horoshutina(callback: CallbackQuery, variables: Variables):
    """Отметка о завершении выступления Хорошутиной"""
    await callback.message.answer("📢 Хорошутина закончила выступление!")