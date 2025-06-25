from typing import Callable, Dict, Any, Awaitable

from aiogram import BaseMiddleware, Bot
from aiogram.types import TelegramObject

from core.db_class import DBClass
from core.keyboards_class import Keyboards
from core.utils.enums import Variables
from core.services.interactive_broadcast_service import InteractiveBroadcastService


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

        broadcast_service = InteractiveBroadcastService(
            bot=self.bot,
            user_repository=self.db.user
        )
        
        data["variables"] = Variables(
            bot=self.bot,
            db=self.db,
            keyboards=self.keyboards,
            broadcast_service=broadcast_service
        )

        if callback_query:
            print(callback_query.data)
        elif message:
            user_id = str(message.from_user.id)
            user = await self.db.user.get_by_telegram_id(telegram_user_id=user_id)

            if not user:
                user_data = message.from_user
                await self.db.user.add_or_get(
                    telegram_user_id=user_id,
                    username=user_data.username,
                    first_name=user_data.first_name
                )

        return await handler(event, data)
