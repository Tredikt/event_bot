from aiogram import Router, F
from aiogram.types import CallbackQuery

from core.utils.enums import Variables
from core.utils.decorators import admin_interactive


router = Router(name="speaker_sadriev_callback")


@router.callback_query(F.data == "interactive_sadriev")
@admin_interactive
async def start_sadriev_interactive(callback: CallbackQuery, variables: Variables):
    await callback.message.answer(
        text="Как вы думаете, сколько кибератак было в России в 2024 году?",
        reply_markup=await variables.keyboards.menu.sadriev_test()
    )


@router.callback_query(F.data.startswith("sadriev_test_"))
async def process_sadriev_test(callback: CallbackQuery, variables: Variables):
    is_correct = callback.data.endswith("_true")
    
    if is_correct:
        text = "✅ Верно! Общее количество кибератак, зарегистрированных в России за 2024 год, составило 1 811 562 707"
        
        telegram_user_id = str(callback.from_user.id)
        current_rating = await variables.db.interactive_service.complete_interactive(
            telegram_user_id=telegram_user_id,
            username=callback.from_user.username,
            first_name=callback.from_user.first_name,
            interactive_name="sadriev",
            points=1
        )
        
        text += f"\n\n🎉 +1 балл! Ваш рейтинг: {current_rating}"
    else:
        text = "❌ Неверно! Правильный ответ: от 1 млрд до 2 млрд"
    
    await callback.message.edit_text(text=text)
    await callback.answer()


@router.callback_query(F.data == "finished_sadriev")
@admin_interactive
async def finished_sadriev(callback: CallbackQuery, variables: Variables):
    """Отметка о завершении выступления Садриева"""
    await callback.message.answer("📢 Садриев закончил выступление!") 