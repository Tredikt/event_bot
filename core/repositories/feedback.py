from typing import Optional

from sqlalchemy import insert, select, update
from sqlalchemy.exc import IntegrityError

from core.db_templates import BaseRepository
from core.models import User, Feedback


class FeedbackRepository(BaseRepository):
    options = []

    async def add_or_update(
            self,
            telegram_user_id: str,
            name: str,
            **kwargs
    ) -> Feedback:
        """Добавляет пользователя или возвращает существующего"""
        existing_feedback = await self.get_by_telegram_id_and_name(telegram_user_id=telegram_user_id, name=name)
        if existing_feedback:
            return await self.update(telegram_user_id=telegram_user_id, name=name, **kwargs)

        try:
            insert_stmt = insert(Feedback).values(
                user_id=telegram_user_id,
                interactive_name=name,
                **kwargs
            ).returning(Feedback)
            result = await self.session.execute(statement=insert_stmt)
            await self.session.commit()
            return result.scalar_one()
        except IntegrityError as ie:
            print(f"Ошибка добавления обратной связи: {ie}")
            # Возможно, запись уже существует (race condition)
            return await self.get_by_telegram_id_and_name(telegram_user_id=telegram_user_id, name=name)

    async def get_by_telegram_id_and_name(self, telegram_user_id: str, name: str) -> Optional[Feedback]:
        select_stmt = select(Feedback).where(
            Feedback.user_id == telegram_user_id,
            Feedback.interactive_name == name
        ).options(*self.options)
        result = await self.session.execute(statement=select_stmt)
        return result.scalar_one_or_none()

    async def update(
            self,
            telegram_user_id: str,
            name: str,
            **kwargs,
    ) -> Optional[Feedback]:
        update_stmt = update(Feedback).where(
            Feedback.user_id == telegram_user_id,
            Feedback.interactive_name == name
        ).values(**kwargs)
        #.returing(Feedback)
        result = await self.session.execute(statement=update_stmt)
        await self.session.commit()
        # return result.scalar_one()
