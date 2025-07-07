from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message
from aiogram.enums import ChatAction

from core.utils.enums import Variables, commands
from core.utils.start_texts import first_part, second_part, third_part, fourth_part, fifth_part

import asyncio

router = Router(name="support_command")


@router.message(Command(commands=["support"]))
async def support_command_handler(message: Message, variables: Variables):
    await message.answer(
        text="если бот ругается или не подаёт признаков жизни, пишите ему 👉 @Leninchanin"
    )