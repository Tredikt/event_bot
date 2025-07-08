# app/core/utils/edit_messages_fast.py

import asyncio
from typing import Any, Tuple

from aiogram import Bot
from aiogram.utils.keyboard import InlineKeyboardBuilder
from sqlalchemy.ext.asyncio import AsyncSession



async def edit_messages_fast(bot: Bot, db) -> None:
    """
    Быстрое редактирование ранее отправленных сообщений.
    Берёт все сохранённые (chat_id, message_id) из БД и вызывает edit_message_text.
    """
    kb = InlineKeyboardBuilder().as_markup()
    messages_repo = db.messages
    messages = await messages_repo.get_all()  # List[Tuple[int,int]]

    async def edit_single(chat_id: int, message_id: int):
        """Редактирует одно сообщение."""
        try:
            await bot.edit_message_reply_markup(
                chat_id=chat_id,
                message_id=message_id,
                reply_markup=kb
            )
        except Exception as e:
            print(f"Ошибка редактирования сообщения {chat_id}:{message_id} — {e}")

    # создаём задачу на каждую пару
    tasks = [edit_single(chat_id, message_id) for chat_id, message_id in messages]

    if tasks:
        await asyncio.gather(*tasks)
        await messages_repo.delete_all()