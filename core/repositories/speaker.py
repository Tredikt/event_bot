from typing import List, Optional

from sqlalchemy import delete, select, insert, update

from core.db_templates import BaseRepository
from core.models import Speaker


class SpeakerRepository(BaseRepository):

    async def get_current_speaker(self) -> Optional[str]:
        stmt = select(Speaker.name)
        result = await self.session.execute(stmt)
        return result.scalars().first()

    async def add_or_update(self, name: str, id_: int = 1) -> None:
        speaker = await self.get_current_speaker()
        if not speaker:
            stmt = insert(Speaker).values(
                id=id_,
                name=name,
            )
        else:
            stmt = update(Speaker).values(
                name=name
            ).where(Speaker.id == id_)
        await self.session.execute(stmt)
        await self.session.commit()

    async def delete_by_id(self, id_: int = 1) -> None:
        stmt = delete(Speaker).where(Speaker.id == id_)
        await self.session.execute(stmt)
        await self.session.commit()