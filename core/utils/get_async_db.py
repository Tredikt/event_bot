from typing import TYPE_CHECKING
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker

from settings import DB_URL

if TYPE_CHECKING:
    from core.db_class import DBClass

engine = create_async_engine(DB_URL, pool_pre_ping=True)
SessionMaker = async_sessionmaker(engine, expire_on_commit=False)


async def get_async_db() -> "DBClass":
    """Создаёт и возвращает новый DBClass с новой сессией.
    
    Вызвавший обязан закрыть сессию после использования: `await db.session.close()`.
    """
    from core.db_class import DBClass
    session = SessionMaker()
    return DBClass(session=session)