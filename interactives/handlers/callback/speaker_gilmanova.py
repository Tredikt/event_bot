from aiogram import Router, F
from aiogram.types import CallbackQuery, Message, ReactionTypeEmoji

from core.utils.enums import Variables
from core.utils.decorators import admin_interactive
from core.utils.answer_validator import AnswerValidator
from interactives.states.gilmanova_states import GilmanovaState


router = Router(name="speaker_gilmanova_callback")


@router.callback_query(F.data == "interactive_gilmanova")
@admin_interactive
async def start_gilmanova_interactive(callback: CallbackQuery, variables: Variables):
    user_id: int = callback.from_user.id
    
    if not hasattr(variables.keyboards.menu, 'gilmanova_states'):
        variables.keyboards.menu.gilmanova_states = {}
    
    if user_id not in variables.keyboards.menu.gilmanova_states:
        variables.keyboards.menu.gilmanova_states[user_id] = GilmanovaState()
    
    state: GilmanovaState = variables.keyboards.menu.gilmanova_states[user_id]
    await state.start_interactive()
    
    await callback.message.answer("🤔 Как вы думаете, что мы сделали?")


@router.message()
async def process_gilmanova_answer(message: Message, variables: Variables):
    user_id: int = message.from_user.id
    
    if not await _is_gilmanova_active(variables, user_id):
        return
    
    state: GilmanovaState = variables.keyboards.menu.gilmanova_states[user_id]
    user_answer: str = message.text
    await message.react(reaction=[ReactionTypeEmoji(emoji="👍")], is_big=True)

    is_correct: bool = await AnswerValidator.check_gilmanova_answer(user_answer=user_answer)
    
    if is_correct:
        await _handle_correct_answer(message=message, variables=variables, state=state)
    else:
        await _handle_incorrect_answer(message=message, variables=variables, state=state)


async def _is_gilmanova_active(variables: Variables, user_id: int) -> bool:
    if not hasattr(variables.keyboards.menu, 'gilmanova_states'):
        return False
        
    if user_id not in variables.keyboards.menu.gilmanova_states:
        return False
        
    state: GilmanovaState = variables.keyboards.menu.gilmanova_states[user_id]
    return await state.is_interactive_active()


async def _handle_correct_answer(message: Message, variables: Variables, state: GilmanovaState) -> None:
    await state.finish_interactive()
    
    telegram_user_id: str = str(message.from_user.id)
    
    current_rating: int = await variables.db.interactive_service.complete_interactive(
        telegram_user_id=telegram_user_id,
        username=message.from_user.username,
        first_name=message.from_user.first_name,
        interactive_name="gilmanova",
        points=1
    )
    
    await message.answer(f"🎉 Правильно! +1 балл! Ваш рейтинг: {current_rating}")


async def _handle_incorrect_answer(message: Message, variables: Variables, state: GilmanovaState) -> None:
    """Обработка неправильного ответа"""
    await state.add_attempt()
    
    if await state.has_attempts_left():
        failure_message: str = await state.get_failure_message()
        await message.answer(failure_message)
    else:
        await _show_correct_answer(message=message, variables=variables, state=state)


async def _show_correct_answer(message: Message, variables: Variables, state: GilmanovaState) -> None:
    """Показывает правильный ответ и завершает интерактив"""
    await state.finish_interactive()
    
    failure_message: str = await state.get_failure_message()
    
    await message.answer(failure_message)

    current_rating: int = await variables.db.interactive_service.complete_interactive(
        telegram_user_id=str(message.from_user.id),
        username=message.from_user.username,
        first_name=message.from_user.first_name,
        interactive_name="gilmanova",
        points=1
    )
    
    await message.answer(f"За усердие +1 балл! Ваш рейтинг: {current_rating}")


@router.callback_query(F.data == "finished_gilmanova")
@admin_interactive
async def finished_gilmanova(callback: CallbackQuery, variables: Variables):
    await callback.message.answer("📢 Гильманова закончила выступление!")
