import asyncio
from typing import List
from aiogram import Bot
from aiogram.types import InlineKeyboardMarkup

from core.models import User


class BroadcastService:
    def __init__(self, bot: Bot):
        self.bot = bot
        self.messages_per_second = 6
        self.batch_count = 5

    async def send_interactive_to_all_users(
        self,
        users: List[User],
        text: str,
        keyboard: InlineKeyboardMarkup = None
    ) -> dict[str, int]:
        """Отправляет интерактив всем пользователям с ограничением скорости"""
        
        user_batches = self._split_users_into_batches(users)
        
        tasks = []
        for batch_index, batch in enumerate(user_batches):
            task = asyncio.create_task(
                self._send_to_batch(
                    batch=batch,
                    text=text,
                    keyboard=keyboard,
                    batch_index=batch_index
                )
            )
            tasks.append(task)
        
        results = await asyncio.gather(*tasks, return_exceptions=True)
        
        return self._calculate_results(results)

    def _split_users_into_batches(self, users: List[User]) -> List[List[User]]:
        """Разделяет пользователей на 5 равных частей"""
        
        batch_size = len(users) // self.batch_count
        remainder = len(users) % self.batch_count
        
        batches = []
        start_index = 0
        
        for i in range(self.batch_count):
            current_batch_size = batch_size + (1 if i < remainder else 0)
            end_index = start_index + current_batch_size
            batches.append(users[start_index:end_index])
            start_index = end_index
        
        return batches

    async def _send_to_batch(
        self,
        batch: List[User],
        text: str,
        keyboard: InlineKeyboardMarkup,
        batch_index: int
    ) -> dict[str, int]:
        """Отправляет сообщения одной группе пользователей с ограничением 6 сообщений в секунду"""
        
        successful_sends = 0
        failed_sends = 0
        
        for i, user in enumerate(batch):
            try:
                await self._send_message_to_user(
                    user_id=user.user_id,
                    text=text,
                    keyboard=keyboard
                )
                successful_sends += 1
                
            except Exception as e:
                print(f"Ошибка отправки пользователю {user.user_id}: {e}")
                failed_sends += 1
            
            if (i + 1) % self.messages_per_second == 0:
                await asyncio.sleep(1)
        
        return {
            "successful": successful_sends,
            "failed": failed_sends,
            "batch_index": batch_index
        }

    async def _send_message_to_user(
        self,
        user_id: str,
        text: str,
        keyboard: InlineKeyboardMarkup
    ) -> None:
        """Отправляет сообщение конкретному пользователю"""
        await self.bot.send_message(
            chat_id=user_id,
            text=text,
            reply_markup=keyboard
        )

    def _calculate_results(self, results: List[dict]) -> dict[str, int]:
        """Подсчитывает общие результаты рассылки"""
        
        total_successful = 0
        total_failed = 0
        
        for result in results:
            if isinstance(result, dict):
                total_successful += result.get("successful", 0)
                total_failed += result.get("failed", 0)
            else:
                total_failed += 1
        
        return {
            "total_sent": total_successful,
            "total_failed": total_failed,
            "total_users": total_successful + total_failed
        } 