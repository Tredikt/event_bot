from aiogram.types import CallbackQuery, Message
from core.utils.enums import Variables


async def add_user_score(call: CallbackQuery | Message, variables: Variables, interactive_name: str) -> str:
    """
    Обрабатывает правильный ответ пользователя: начисляет балл и возвращает текст с рейтингом
    
    Args:
        call: CallbackQuery объект
        variables: Variables объект с доступом к сервисам
        interactive_name: Название интерактива для записи в БД
    
    Returns:
        str: Дополнительный текст с информацией о баллах и рейтинге
    """
    telegram_user_id = str(call.from_user.id)
    current_rating = await variables.db.interactive_service.complete_interactive(
        telegram_user_id=telegram_user_id,
        username=call.from_user.username,
        first_name=call.from_user.first_name,
        interactive_name=interactive_name,
        points=1
    )
    
    return f"\n\n🎉 +1 балл! Ваш рейтинг: {current_rating}" 