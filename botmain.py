import asyncio
import logging
import sys

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.fsm.storage.memory import MemoryStorage
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker

from core.db_class import DBClass
from middlewares.basic_middleware import BasicMiddleware
from settings import config

from core.routers import routers


logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)


def handle_exception(exc_type, exc_value, exc_traceback):
    if issubclass(exc_type, KeyboardInterrupt):
        # Оставить стандартную обработку Ctrl+C
        sys.__excepthook__(exc_type, exc_value, exc_traceback)
        return
    logging.error("Необработанное исключение", exc_info=(exc_type, exc_value, exc_traceback))


sys.excepthook = handle_exception


async def main():
    storage = MemoryStorage()

    engine = create_async_engine(config.DATABASE_URL)
    session = async_sessionmaker(engine, expire_on_commit=False)

    bot = Bot(token=config.TG_TOKEN, default=DefaultBotProperties(parse_mode="HTML"))
    dp = Dispatcher(bot=bot, storage=storage)

    dp.include_routers(*routers)
    async with session() as session:
        dp.update.middleware(BasicMiddleware(bot=bot, db=DBClass(session=session)))
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


def start_app():
    asyncio.run(main())


if __name__ == "__main__":
    start_app()
