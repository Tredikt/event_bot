from aiogram import Bot
from aiogram.types import BotCommand

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



commands = [
    BotCommand(command='support', description='Связаться с технической поддержкой'),
    BotCommand(command='event', description='Связаться с организаторами'),
    BotCommand(command='order', description='Порядок выступления'),
    BotCommand(command='plan', description='План мероприятия'),
    BotCommand(command='navigator', description='Навигатор по боту')
]