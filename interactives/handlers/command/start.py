from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message
from aiogram.enums import ChatAction

from core.utils.enums import Variables, commands
from core.utils.start_texts import first_part, second_part, third_part, fourth_part, fifth_part

import asyncio

router = Router(name="start_command")


@router.message(Command(commands=["start"]))
async def start_command_handler(message: Message, variables: Variables):
    await message.chat.do(ChatAction.TYPING)
    await asyncio.sleep(1)
    await message.answer(first_part, parse_mode="HTML")

    await asyncio.sleep(3)
    await message.chat.do(ChatAction.TYPING)
    await asyncio.sleep(1.5)
    await message.answer(second_part, parse_mode="HTML")

    await asyncio.sleep(3.5)
    await message.chat.do(ChatAction.TYPING)
    await asyncio.sleep(2)
    await message.answer(third_part, parse_mode="HTML")

    await asyncio.sleep(4)
    await message.chat.do(ChatAction.TYPING)
    await asyncio.sleep(1.5)
    await message.answer(fourth_part, parse_mode="HTML")

    await asyncio.sleep(3)
    await message.chat.do(ChatAction.TYPING)
    await asyncio.sleep(1)
    await message.answer(fifth_part, parse_mode="HTML")
