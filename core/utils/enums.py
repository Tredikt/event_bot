from aiogram import Bot
from pydantic import BaseModel

from core.keyboards_class import Keyboards
from core.db_class import DBClass


class Variables(BaseModel):
    bot: Bot
    db: DBClass
    keyboards: Keyboards

    class Config:
        arbitrary_types_allowed = True
