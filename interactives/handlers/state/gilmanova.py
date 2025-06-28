from aiogram import Router, F
from aiogram.filters import StateFilter
from aiogram.types import Message, ReactionTypeEmoji

from core.bot_states import BotStates
from core.utils.answer_validator import AnswerValidator
from core.utils.enums import Variables
from core.utils.animate_waiting_message import animate_answer_analysis
from interactives.states.gilmanova_states import GilmanovaState


router = Router(name="gilmanova_state")


@router.message(F.text, StateFilter(BotStates.gilmanova))
async def process_gilmanova_answer(message: Message, variables: Variables):
    user_id: int = message.from_user.id
    
    await _ensure_gilmanova_state_exists(variables=variables, user_id=user_id)
    
    if not await _is_gilmanova_active(variables=variables, user_id=user_id):
        return
    
    state: GilmanovaState = variables.keyboards.menu.gilmanova_states[user_id]
    
    if await state.is_currently_processing() or await state.is_interactive_finished():
        return
    
    await state.set_processing(True)
    
    try:
        user_answer: str = message.text
        await message.react(reaction=[ReactionTypeEmoji(emoji="👍")], is_big=True)

        is_correct: bool = await AnswerValidator.check_gilmanova_answer(user_answer=user_answer)
        
        if is_correct:
            await _handle_correct_answer(message=message, variables=variables, state=state)
        else:
            await _handle_incorrect_answer(message=message, variables=variables, state=state)
    finally:
        await state.set_processing(False)


async def _ensure_gilmanova_state_exists(variables: Variables, user_id: int) -> None:
    """Обеспечивает существование состояния Гильмановой для пользователя"""
    
    if not hasattr(variables.keyboards.menu, 'gilmanova_states'):
        variables.keyboards.menu.gilmanova_states = {}
    
    if user_id not in variables.keyboards.menu.gilmanova_states:
        variables.keyboards.menu.gilmanova_states[user_id] = GilmanovaState()
        state = variables.keyboards.menu.gilmanova_states[user_id]
        await state.start_interactive()
        print(f"Инициализировано состояние Гильмановой для пользователя {user_id}")


async def _is_gilmanova_active(variables: Variables, user_id: int) -> bool:
    if not hasattr(variables.keyboards.menu, 'gilmanova_states'):
        return False
        
    if user_id not in variables.keyboards.menu.gilmanova_states:
        return False
        
    state: GilmanovaState = variables.keyboards.menu.gilmanova_states[user_id]
    return await state.is_interactive_active()


async def _handle_correct_answer(message: Message, variables: Variables, state: GilmanovaState) -> None:
    await state.finish_interactive()
    
    await animate_answer_analysis(message=message, bot=variables.bot)
    
    telegram_user_id: str = str(message.from_user.id)
    
    current_rating: int = await variables.db.interactive_service.complete_interactive(
        telegram_user_id=str(telegram_user_id),
        username=message.from_user.username,
        first_name=message.from_user.first_name,
        interactive_name="gilmanova",
        points=1
    )
    
    await message.answer(text=f"🎉 Правильно! +1 балл! Ваш рейтинг: {current_rating}")


async def _handle_incorrect_answer(message: Message, variables: Variables, state: GilmanovaState) -> None:
    """Обработка неправильного ответа"""
    await state.add_attempt()
    
    await animate_answer_analysis(message=message, bot=variables.bot)
    
    if await state.has_attempts_left():
        failure_message: str = await state.get_failure_message()
        await message.answer(text=failure_message)
    else:
        await _show_correct_answer(message=message, variables=variables, state=state)


async def _show_correct_answer(message: Message, variables: Variables, state: GilmanovaState) -> None:
    """Показывает правильный ответ и завершает интерактив"""
    await state.finish_interactive()
    
    failure_message: str = await state.get_failure_message()
    
    await message.answer(text=failure_message)
    
    current_rating: int = await variables.db.interactive_service.complete_interactive(
        telegram_user_id=str(message.from_user.id),
        username=message.from_user.username,
        first_name=message.from_user.first_name,
        interactive_name="gilmanova",
        points=1
    )
    
    await message.answer(text=f"За усердие +1 балл! Ваш рейтинг: {current_rating}")