# app/services/broadcast.py

import asyncio
from typing import List, Tuple, Union

from aiogram import Bot
from aiogram.types import InlineKeyboardMarkup, Message
from sqlalchemy.ext.asyncio import AsyncSession

from core.models import User
from core.repositories import MessagesRepository


class BroadcastService:
    def __init__(
        self,
        bot: Bot,
        db_session: AsyncSession,
        messages_per_second: int = 6,
        batch_count: int = 5,
    ):
        self.bot = bot
        self.session = db_session
        self.messages_repo = MessagesRepository(session=db_session)
        self.messages_per_second = messages_per_second
        self.batch_count = batch_count

    async def send_interactive_to_all_users(
        self,
        users: List[User],
        text: str,
        keyboard: InlineKeyboardMarkup = None,
        collect_messages: bool = False,
        disable_web_page_preview: bool = False
    ) -> Union[dict[str, int], None]:
        """
        Рассылает текст + инлайн-клавиатуру всем пользователям партиями.
        Если collect_messages=True — после отправки сохраняет (chat_id, message_id) в БД.
        Возвращает статистику, если collect_messages=False; иначе — None.
        """
        batches = self._split_users_into_batches(users)
        tasks = [
            asyncio.create_task(
                self._send_to_batch(
                    batch=b,
                    text=text,
                    keyboard=keyboard,
                    batch_index=i,
                    collect_messages=collect_messages,
                    disable_web_page_preview=disable_web_page_preview
                )
            )
            for i, b in enumerate(batches)
        ]
        results = await asyncio.gather(*tasks, return_exceptions=True)

        if collect_messages:
            # results: List[List[Tuple[int, int]]]
            flat: List[Tuple[int, int]] = []
            for r in results:
                if isinstance(r, list):
                    flat.extend(r)
            if flat:
                await self.messages_repo.add_many(flat)
                print("here")
            return None

        return await self._calculate_results(results)

    def _split_users_into_batches(self, users: List[User]) -> List[List[User]]:
        """Делит список users на batch_count примерно равных частей."""
        n = len(users)
        base = n // self.batch_count
        rem = n % self.batch_count
        batches, start = [], 0
        for i in range(self.batch_count):
            size = base + (1 if i < rem else 0)
            batches.append(users[start:start + size])
            start += size
        return batches

    async def _send_to_batch(
        self,
        batch: List[User],
        text: str,
        keyboard: InlineKeyboardMarkup,
        batch_index: int,
        collect_messages: bool = False,
        disable_web_page_preview: bool = False
    ) -> Union[dict[str, int], List[Tuple[int, int]]]:
        """
        Отсылает одному батчу пользователей, не более messages_per_second в секунду.
        Если collect_messages=True — возвращает список (chat_id, message_id).
        Иначе — возвращает dict статистики по этому батчу.
        """
        successful, failed = 0, 0
        messages_list: List[Tuple[int, int]] = []

        for idx, user in enumerate(batch):
            try:
                msg: Message = await self.bot.send_message(
                    chat_id=user.user_id,
                    text=text,
                    reply_markup=keyboard,
                    parse_mode="HTML",
                    disable_web_page_preview=disable_web_page_preview
                )
                successful += 1
                if collect_messages:
                    messages_list.append((msg.chat.id, msg.message_id))
            except Exception as e:
                print(f"[batch {batch_index}] Ошибка отправки {user.user_id}: {e}")
                failed += 1

            # throttle
            if (idx + 1) % self.messages_per_second == 0:
                await asyncio.sleep(1)

        if collect_messages:
            return messages_list

        return {
            "batch_index": batch_index,
            "successful": successful,
            "failed": failed
        }

    async def _calculate_results(
        self,
        results: List[Union[dict, BaseException]]
    ) -> dict[str, int]:
        """Складывает результаты всех батчей в общую статистику."""
        total_successful = 0
        total_failed = 0

        for r in results:
            if isinstance(r, dict):
                total_successful += r.get("successful", 0)
                total_failed += r.get("failed", 0)
            else:
                total_failed += 1

        return {
            "total_sent": total_successful,
            "total_failed": total_failed,
            "total_users": total_successful + total_failed
        }

