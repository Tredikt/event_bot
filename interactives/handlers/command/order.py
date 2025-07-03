from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message
from aiogram.enums import ChatAction

from core.utils.enums import Variables, commands

router = Router(name="order_command")


@router.message(Command(commands=["order"]))
async def order_command_handler(message: Message, variables: Variables):
    await message.answer(
        text=(
            "▪️ <b>Анастасия Белозёрова</b> (БЦ ОБР) — как системно учитывать учебники\n"
            "▪️ <b>Рим Мендубаев</b> (БЦ ОБП) — электронное согласование в реальности\n"
            "▪️ <b>Тимур Садриев</b> (BARS.UP) — доступ и безопасность без головняка\n"
            "▪️ <b>Дмитрий Адмакин</b> (БЦ ОПР) — NXTCore и ИИ на практике, а не на презентации\n"
            "▪️ <b>Асель Нурмухаметова</b> (БЦ Росстат) — кейс для Уполномоченного по правам человека\n"
            "▪️ <b>Александр Балуков</b> (БЦ Медицина) — цифровая лаборатория, не миф, а продукт\n"
            "▪️ <b>Юлия Хорошутина</b> (AlphaBI) — продуктовый подход, если без воды\n"
            "▪️ <b>Станислав Забегаев</b> (БЦ УНП) — отчёты и документы — быстро и без боли\n"
            "▪️ <b>Антон Гавриков</b> (БЦ ЖКХ) — зачем вообще этот ЕИРЦМ\n"
            "▪️ <b>Эльвира Гильманова</b> — как за 1825 дней из идеи сделать бизнес"
        ),
        parse_mode="HTML"
    )
