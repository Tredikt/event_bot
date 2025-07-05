from datetime import datetime
from typing import Optional

from sqlalchemy import insert, select, update
from sqlalchemy.exc import IntegrityError, SQLAlchemyError

from core.db_templates import BaseRepository
from core.models import User


class UserRepository(BaseRepository):
    options = []

    async def add_or_get(
        self,
        telegram_user_id: str,
        username: str = None,
        first_name: str = None,
    ) -> User:
        """Добавляет пользователя или возвращает существующего"""
        existing_user = await self.get_by_telegram_id(telegram_user_id=telegram_user_id)
        if existing_user:
            return existing_user
            
        try:
            insert_stmt = insert(User).values(
                user_id=telegram_user_id,
                username=username,
                first_name=first_name,
            )
            await self.session.execute(statement=insert_stmt)
            await self.session.commit()
            return await self.get_by_telegram_id(telegram_user_id=telegram_user_id)
        except IntegrityError as ie:
            print(f"Ошибка добавления пользователя: {ie}")
            # Возможно, пользователь уже существует (race condition)
            # Просто возвращаем существующего пользователя
            return await self.get_by_telegram_id(telegram_user_id=telegram_user_id)

    async def get_by_id(self, id: int) -> Optional[User]:
        """Получает пользователя по внутреннему ID (первичный ключ)"""
        select_stmt = select(User).where(User.id == id).options(*self.options)
        result = await self.session.execute(statement=select_stmt)
        return result.scalar_one_or_none()
    
    async def get_by_telegram_id(self, telegram_user_id: str) -> Optional[User]:
        """Получает пользователя по Telegram user_id"""
        select_stmt = select(User).where(User.user_id == telegram_user_id).options(*self.options)
        try:
            result = await self.session.execute(statement=select_stmt)
            return result.scalar_one_or_none()
        except SQLAlchemyError as e:
            print(f"Ошибка получения пользователя: {e}")
            # Не делаем rollback, так как это может вызвать конфликт сессий
            # Сессия будет закрыта в middleware
            return None
    
    async def update_user_info(
        self,
        telegram_user_id: str,
        **kwargs
    ) -> Optional[User]:
        """Обновляет информацию о пользователе"""
        user = await self.get_by_telegram_id(telegram_user_id=telegram_user_id)
        if not user:
            return None
        update_stmt = update(User).where(
            User.user_id == telegram_user_id
        ).values(**kwargs)
        result = await self.session.execute(statement=update_stmt)
        await self.session.commit()
        # return result.scalar_one()

    async def update_feedback_waiting(self, speaker_name: str = None):
        """Обновляет feedback_waiting для всех пользователей и устанавливает текущего спикера"""
        values = {"feedback_waiting": datetime.now()}
        if speaker_name:
            values["current_speaker"] = speaker_name
        
        stmt = update(User).values(**values)
        await self.session.execute(statement=stmt)
        await self.session.commit()

    async def get_all_users(self) -> list[User]:
        """Получает всех пользователей"""
        select_stmt = select(User).order_by(User.id).options(*self.options)
        result = await self.session.execute(statement=select_stmt)
        return result.scalars().all()
    
    async def add_points(
        self,
        telegram_user_id: str,
        points: int
    ) -> Optional[User]:
        """Начисляет баллы пользователю"""
        
        user = await self.get_by_telegram_id(telegram_user_id=telegram_user_id)
        if not user:
            return None
            
        user.rating += points
        await self.session.commit()
        return user
    
    async def get_user_rating(self, telegram_user_id: str) -> int:
        """Получает рейтинг пользователя"""
        user = await self.get_by_telegram_id(telegram_user_id)
        return user.rating if user else 0
    
    async def get_top_users(self, limit: int = 10) -> list[User]:
        """Получает топ пользователей по рейтингу"""
        select_stmt = select(User).order_by(User.rating.desc()).limit(limit).options(*self.options)
        result = await self.session.execute(statement=select_stmt)
        return result.scalars().all()

    async def get_users_with_feedback_waiting(self):
        select_stmt = select(User).where(User.feedback_waiting.isnot(None))
        result = await self.session.execute(statement=select_stmt)
        return result.scalars().all()