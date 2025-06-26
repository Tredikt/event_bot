from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

from core.utils.enums import Variables
from settings import config


router = Router(name="start_command")

_START_TEXT = """
Приветственное сообщение, план мероприятия, обзор по функиционалу бота, повествование, 
что будет в этом боте сегодня, рассказ про геймификацию в боте, что за активность начисляются 
баллы, по которым разыграется приз в конце

Контакты организаторов мероприятия, по всем вопросам обращайтесь сюда
Ожидайте начала первой активности (первого выступления спикера)
"""


@router.message(Command(commands=["start"]))
async def start_command_handler(message: Message, variables: Variables):
    await message.answer(text=_START_TEXT)
