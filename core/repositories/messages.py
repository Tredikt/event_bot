from typing import List

from sqlalchemy import delete, select, insert
from sqlalchemy.ext.asyncio import AsyncSession

from core.db_templates import BaseRepository
from core.models import Messages


class MessagesRepository(BaseRepository):

    async def create(self, chat_id: str, message_id: int) -> None:
        stmt = insert(Messages).values(
            chat_id=chat_id,
            message_id=message_id,
        )
        await self.session.execute(stmt)
        await self.session.commit()

    async def delete_by_chat_id(self, chat_id: str) -> None:
        """
        Удалить все записи по chat_id.
        Возвращает число удалённых строк.
        """
        stmt = delete(Messages).where(Messages.chat_id == chat_id)
        await self.session.execute(stmt)
        await self.session.commit()

    async def get_by_chat_id(self, chat_id: str) -> List[int]:
        """Получить все сообщения для данного chat_id."""
        stmt = select(Messages).where(Messages.chat_id == chat_id)
        result = await self.session.execute(stmt)
        return result.scalars().all()

    async def get_all(self):
        stmt = select(Messages)
        result = await self.session.execute(stmt)
        return result.scalars().all()

    async def delete_all(self):
        stmt = delete(Messages)
        await self.session.execute(stmt)
        await self.session.commit()