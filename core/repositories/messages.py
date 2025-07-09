# app/core/repositories/messages.py

from typing import Sequence, Any, Tuple, List
from sqlalchemy import insert, select, delete
from sqlalchemy.ext.asyncio import AsyncSession

from core.models import Messages


class MessagesRepository:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def add_many(self, messages: Sequence[Any] | None) -> None:
        """
        Вставляет пары (chat_id, message_id) в таблицу messages.
        Если messages пусто или None — ничего не делает.
        """
        if not messages:
            return

        rows = []
        for item in messages:
            try:
                chat_id, message_id, *_ = item
            except Exception:
                continue
            rows.append({"chat_id": str(chat_id), "message_id": message_id})

        if not rows:
            return

        stmt = insert(Messages).values(rows)
        await self.session.execute(stmt)
        await self.session.commit()

    async def get_all(self) -> list[Tuple[str, int]]:
        """
        Возвращает список всех сохранённых (chat_id, message_id).
        """
        stmt = select(Messages.chat_id, Messages.message_id)
        result = await self.session.execute(stmt)
        # result.fetchall() даст список кортежей
        return list(result.fetchall())

    async def delete_all(self):
        stmt = delete(Messages)
        await self.session.execute(stmt)
        await self.session.commit()

    async def get_by_chat_id(self, chat_id: str) -> List[Messages]:
        stmt = select(Messages).where(Messages.chat_id == chat_id)
        result = await self.session.execute(stmt)
        return list(result.scalars().all())

    async def delete_by_chat_id(self, chat_id: str) -> None:
        stmt = delete(Messages).where(Messages.chat_id == chat_id)
        await self.session.execute(stmt)
        await self.session.commit()