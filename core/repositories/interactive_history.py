from typing import Optional, List
from sqlalchemy import select, func, insert
from sqlalchemy.exc import IntegrityError

from core.db_templates import BaseRepository
from core.models.interactive_history import InteractiveHistory


class InteractiveHistoryRepository(BaseRepository):
    options = []

    async def add_record(
        self,
        user_id: str,
        interactive_name: str,
        points_earned: int = 1
    ) -> InteractiveHistory:
        """Добавляет запись о прохождении интерактива"""
        try:
            insert_stmt = insert(InteractiveHistory).values(
                user_id=user_id,
                interactive_name=interactive_name,
                points_earned=points_earned,
            ).returning(InteractiveHistory)
            result = await self.session.execute(statement=insert_stmt)
            await self.session.commit()
            return result.scalar_one()
        except IntegrityError:
            await self.session.rollback()
            return None

    async def get_user_history(self, user_id: str, limit: int = 20) -> List[InteractiveHistory]:
        """Получает историю интерактивов пользователя"""
        select_stmt = (
            select(InteractiveHistory)
            .where(InteractiveHistory.user_id == user_id)
            .order_by(InteractiveHistory.completed_at.desc())
            .limit(limit)
            .options(*self.options)
        )
        result = await self.session.execute(select_stmt)
        return result.scalars().all()

    async def check_already_completed(self, user_id: str, interactive_name: str) -> bool:
        """Проверяет, проходил ли пользователь этот интерактив"""
        select_stmt = select(InteractiveHistory).where(
            InteractiveHistory.user_id == user_id,
            InteractiveHistory.interactive_name == interactive_name
        )
        result = await self.session.execute(select_stmt)
        return result.scalar_one_or_none() is not None

    async def get_interactive_stats(self, interactive_name: str) -> dict:
        """Получает статистику по интерактиву"""
        select_stmt = select(
            func.count(InteractiveHistory.id).label('total_completions'),
            func.count(func.distinct(InteractiveHistory.user_id)).label('unique_users'),
            func.sum(InteractiveHistory.points_earned).label('total_points')
        ).where(InteractiveHistory.interactive_name == interactive_name)
        
        result = await self.session.execute(select_stmt)
        row = result.first()
        
        return {
            'total_completions': row.total_completions or 0,
            'unique_users': row.unique_users or 0,
            'total_points': row.total_points or 0
        }

    async def get_by_user_and_interactive(self, user_id: str, interactive_name: str) -> Optional[InteractiveHistory]:
        """Получает запись по пользователю и названию интерактива"""
        select_stmt = select(InteractiveHistory).where(
            InteractiveHistory.user_id == user_id,
            InteractiveHistory.interactive_name == interactive_name
        ).options(*self.options)
        result = await self.session.execute(statement=select_stmt)
        return result.scalar_one_or_none()

    async def get_all_history(self) -> List[InteractiveHistory]:
        """Получает всю историю интерактивов для аналитики"""
        select_stmt = select(InteractiveHistory).order_by(
            InteractiveHistory.completed_at.desc()
        ).options(*self.options)
        result = await self.session.execute(statement=select_stmt)
        return result.scalars().all() 
