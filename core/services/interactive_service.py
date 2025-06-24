from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from core.db_class import DBClass
    from core.repositories.user import UserRepository
    from core.repositories.interactive_history import InteractiveHistoryRepository


class InteractiveService:
    """Сервис для работы с интерактивами"""
    
    def __init__(self, db: "DBClass"):
        self.db = db
    
    async def complete_interactive(
        self,
        telegram_user_id: str,
        username: str = None,
        first_name: str = None,
        interactive_name: str = "unknown",
        points: int = 1
    ) -> int:
        """
        Завершает интерактив для пользователя:
        1. Создает или получает пользователя
        2. Начисляет баллы
        3. Записывает в историю
        4. Возвращает текущий рейтинг
        """
        
        user = await self.db.user.add_or_get(
            telegram_user_id=telegram_user_id,
            username=username,
            first_name=first_name
        )
        
        await self.db.user.add_points(
            telegram_user_id=telegram_user_id,
            points=points
        )
        
        await self.db.interactive_history.add_record(
            user_id=telegram_user_id,
            interactive_name=interactive_name,
            points_earned=points
        )
        
        current_rating = await self.db.user.get_user_rating(telegram_user_id)
        return current_rating 