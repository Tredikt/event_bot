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
            "<b>🎤 Спикеры дня:</b>\n"
            "— <b>Анастасия Белозёрова</b> <i>(БЦ ОБР): как системно учитывать учебники</i>\n"
            "— <b>Рим Мендубаев</b> <i>(БЦ ОБП): электронное согласование без хаоса</i>\n"
            "— <b>Тимур Садриев</b> <i>(ОВА): кибербезопасность для бизнеса</i>\n"
            "— <b>Дмитрий Адмакин</b> <i>(БЦ ОПР): программирование без кода</i>\n"
            "— <b>Асель Нурмухаметова</b> <i>(БЦ Росстат): кейс для Уполномоченного по правам человека в РФ</i>\n"
            "— <b>Александр Балуков</b> <i>(БЦ Медицина): цифровая лаборатория — не миф, а продукт</i>\n"
            "— <b>Юлия Хорошутина</b> <i>(AW/AlphaBI): продуктовый подход AlphaBI и AW BI</i>\n"
            "— <b>Станислав Забегаев</b> <i>(БЦ УНП): отчёты и документы без лишней рутины</i>\n"
            "— <b>Антон Гавриков</b> <i>(БЦ ЕИРЦ): ЕИРЦМ — что это и для чего он нужен?</i>\n"
            "— <b>Эльвира Гильманова</b> <i>: как за 1825 дней из идеи сделать бизнес</i>"
        ),
        parse_mode="HTML"
    )
