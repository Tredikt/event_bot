from aiogram import Router, F
from aiogram.filters import StateFilter
from aiogram.types import Message, ReactionTypeEmoji
from aiogram.fsm.context import FSMContext
from interactives.fsm.interactives import InteractivesStates
from interactives.handlers.callback.zargaryan import QUESTIONS


router = Router(name="zargaryan_state_router")


# Хендлер для текстовых сообщений в состоянии zargaryan
@router.message(F.text, StateFilter(InteractivesStates.zargaryan))
async def handle_zargaryan_message(message: Message, state: FSMContext, variables):
    user_id = message.from_user.id
    
    # Проверяем, есть ли состояние у пользователя
    if not hasattr(variables.keyboards.menu, 'zargaryan_states') or \
       user_id not in variables.keyboards.menu.zargaryan_states:
        await message.answer("Пожалуйста, начните опрос заново, нажав на кнопку 'Ответить на вопросы'")
        return
    
    state_data = variables.keyboards.menu.zargaryan_states[user_id]
    
    # Сохраняем ответ
    state_data.answers.append(message.text)
    state_data.current_question += 1
    await message.react(reaction=[ReactionTypeEmoji(emoji="👍")], is_big=True)

    # Проверяем, есть ли еще вопросы
    if state_data.current_question < len(QUESTIONS):
        # Задаем следующий вопрос
        await message.answer(
            f"Спасибо за ответ!\n\nВопрос {state_data.current_question + 1}:\n{QUESTIONS[state_data.current_question]}"
        )
    else:
        # Все вопросы заданы
        current_rating = await variables.db.interactive_service.complete_interactive(
            telegram_user_id=user_id,
            username=message.from_user.username,
            first_name=message.from_user.first_name,
            interactive_name="zargaryan",
            points=1
        )
        await message.answer(
            text=f"Спасибо за ответы на все вопросы!\n\n 🎉 +1 балл! Ваш рейтинг: {current_rating}"
        )
        # Очищаем состояние
        del variables.keyboards.menu.zargaryan_states[user_id]
        await state.clear()