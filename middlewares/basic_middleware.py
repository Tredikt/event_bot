from typing import Callable, Dict, Any, Awaitable

from aiogram import BaseMiddleware, Bot
from aiogram.types import TelegramObject

from core.db_class import DBClass
from core.keyboards_class import Keyboards
from core.utils.enums import Variables


class BasicMiddleware(BaseMiddleware):
    def __init__(self, bot: Bot, db: DBClass):
        self.bot = bot
        self.db = db
        self.keyboards = Keyboards()

    async def __call__(
            self,
            handler: Callable[[TelegramObject, Dict[str, Any]], Awaitable[Any]],
            event: TelegramObject,
            data: Dict[str, Any]) -> Any:

        callback_query = event.callback_query
        message = event.message

        data["variables"] = Variables(
            bot=self.bot,
            db=self.db,
            keyboards=self.keyboards
        )

        if callback_query:
            print(callback_query.data)

        return await handler(event, data)
