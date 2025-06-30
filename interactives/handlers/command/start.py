from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

from core.utils.enums import Variables, commands
from core.utils.user_texts import START_TEXT


router = Router(name="start_command")


@router.message(Command(commands=["start"]))
async def start_command_handler(message: Message, variables: Variables):
    await variables.bot.set_my_commands(commands=commands)
    await message.answer(text=START_TEXT)
