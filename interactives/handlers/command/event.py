from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message
from aiogram.enums import ChatAction

from core.utils.enums import Variables, commands
from core.utils.start_texts import first_part, second_part, third_part, fourth_part, fifth_part

import asyncio

router = Router(name="event_command")


@router.message(Command(commands=["event"]))
async def event_command_handler(message: Message, variables: Variables):
    await message.answer(
        text="@barsevent, пишите им, если вас что-то беспокоит в организации и проведении мероприятия 🫡"
    )