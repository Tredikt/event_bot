from aiogram import Bot
from pydantic import BaseModel

from core.keyboards_class import Keyboards
from core.db_class import DBClass
from core.services.interactive_broadcast_service import InteractiveBroadcastService


class Variables(BaseModel):
    bot: Bot
    db: DBClass
    keyboards: Keyboards
    broadcast_service: InteractiveBroadcastService

    class Config:
        arbitrary_types_allowed = True
