import asyncio
from datetime import datetime, timedelta

import pytz
from aiogram import Bot

from core.db_class import DBClass


async def check(bot: Bot, db: DBClass):
    while True:
        users = await db.user.get_users_with_feedback_waiting()
        # now = datetime.now(pytz.timezone("Europe/Moscow"))
        now = datetime.now()
        for user in users:
            # print(user.feedback_waiting, now)
            try:
                if (user.feedback_waiting + timedelta(minutes=2)) < now:
                # if (user.feedback_waiting + timedelta(seconds=15)) < now:
                    await bot.send_message(
                        chat_id=user.user_id,
                        text="😔 <b>Эх, жаль.</b> Спикеру было бы полезно получить любую обратную связь.\n<i>Но ладно, теперь <b>наша задача — встретить следующего спикера.</b></i>"
                    )
                    await db.user.update_user_info(telegram_user_id=user.user_id, feedback_waiting=None)
            except Exception as e:
                print(e)
        await asyncio.sleep(5)
