from typing import Optional

from sqlalchemy import insert, select, update
from sqlalchemy.exc import IntegrityError

from core.db_templates import BaseRepository
from core.models import Question


class QuestionRepository(BaseRepository):

    async def add(
        self,
        user_id: str,
        interactive_name: str,
        body: str
    ):
        insert_stmt = insert(Question).values(
            user_id=user_id,
            interactive_name=interactive_name,
            body=body
        )
        await self.session.execute(statement=insert_stmt)
        await self.session.commit()

    async def get(self, interactive_name: str):
        stmt = select(Question).where(Question.interactive_name == interactive_name)
        result = await self.session.execute(statement=stmt)
        return result.scalars().all()
