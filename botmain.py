import asyncio
import logging
import sys

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.fsm.storage.memory import MemoryStorage
from sqlalchemy.ext.asyncio import async_sessionmaker

from core.db_class import DBClass
from core.utils.get_async_db import get_async_db, SessionMaker
from feedback_checker import check
from middlewares.basic_middleware import BasicMiddleware
from settings import config, DB_URL

from core.routers import routers


loop = asyncio.get_event_loop()
middleware_db: DBClass = loop.run_until_complete(get_async_db())

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
    print(DB_URL)
    storage = MemoryStorage()

    bot = Bot(token=config.TG_TOKEN, default=DefaultBotProperties(parse_mode="HTML"))
    dp = Dispatcher(bot=bot, storage=storage)

    dp.include_routers(*routers)
    dp.update.middleware(BasicMiddleware(bot=bot, db=middleware_db, session=SessionMaker))

    asyncio.create_task(check(bot=bot))
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


def start_app():
    asyncio.run(main())



if __name__ == "__main__":
    start_app()
