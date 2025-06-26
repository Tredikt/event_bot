from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker

from core.db_class import DBClass
from settings import DB_URL


async def get_async_db() -> DBClass:
    engine = create_async_engine(DB_URL)
    session = async_sessionmaker(engine, expire_on_commit=False)
    async with session() as session:
        return DBClass(session=session)