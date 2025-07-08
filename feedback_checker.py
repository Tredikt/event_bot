import asyncio
from datetime import datetime, timedelta

import pytz
from aiogram import Bot

from core.db_class import DBClass
from core.utils.get_async_db import get_async_db
from core.utils.interactive_messages import get_no_feedback_message


async def check(bot: Bot, db: DBClass | None = None):
    while True:
        try:
            # Создаем новую сессию для каждого запроса
            current_db = await get_async_db()
            
            try:
                users = await current_db.user.get_users_with_feedback_waiting()
                # now = datetime.now(pytz.timezone("Europe/Moscow"))
                now = datetime.now()
                for user in users:
                    # print(user.feedback_waiting, now)
                    try:
                        if (user.feedback_waiting + timedelta(minutes=2)) < now:
                        # if (user.feedback_waiting + timedelta(seconds=15)) < now:
                            # Используем current_speaker из базы данных, fallback на belozertseva
                            speaker_name = user.current_speaker or "belozertseva"
                            message_text = get_no_feedback_message(speaker_name)
                            await bot.send_message(
                                chat_id=user.user_id,
                                text=message_text,
                                parse_mode="HTML"
                            )
                            await current_db.user.update_user_info(
                                telegram_user_id=user.user_id, 
                                feedback_waiting=None,
                                current_speaker=None
                            )
                    except Exception as e:
                        print(f"Ошибка обработки пользователя {user.user_id}: {e}")
                        await current_db.user.update_user_info(
                            telegram_user_id=user.user_id, 
                            feedback_waiting=None,
                            current_speaker=None
                        )
            finally:
                # Закрываем сессию после использования
                await current_db.session.close()
                
        except Exception as e:
            print(f"Ошибка в feedback_checker: {e}")
            
        await asyncio.sleep(5)
