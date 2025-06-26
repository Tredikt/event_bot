from aiogram import Router, F
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, CallbackQuery

from core.bot_states import BotStates
from core.utils.enums import Variables

router = Router(name="zabegayev_callback_router")


@router.callback_query(F.data.startswith("start_zabegayev_"))
async def start_zabegayev(call: CallbackQuery, variables: Variables):
    mode = call.data.split("_")[-1]
    keyboard = await variables.keyboards.menu.zabegayev_1()
    text = ""
    if mode == "false":
        text="Неверно! В отличие от legacy-решений, Sprinter работает в браузере без установки — это принципиальное архитектурное преимущество. Никаких зависимостей, никаких 'квестов' с обновлениями. Открыли веб-интерфейс — и работаете даже с планшета!"
    else:
        text = "✅ Верно!"
    await call.message.answer(
        text=text
    )
    await call.message.answer(
        text="Настройка Sprinter под госсистемы (например, 'Электронный бюджет') занимает 3+ месяца из-за сложной интеграции",
        reply_markup=keyboard
    )


@router.callback_query(F.data.startswith("zabegayev_1_"))
async def zabegayev_2(call: CallbackQuery, variables: Variables):
    mode = call.data.split("_")[-1]
    keyboard = await variables.keyboards.menu.zabegayev_2()
    text = ""
    if mode == "false":
        text="Миф! Sprinter внедряется за 1 день благодаря модульной архитектуре и готовым адаптерам. Например, в Минфине мы подключили генерацию отчетов за 4 часа. Docker + веб-компоненты — и вы в работе!"
    else:
        text = "✅ Верно!"
    await call.message.answer(
        text=text
    )
    await call.message.answer(
        text="Sprinter генерирует сложные документы с динамическими таблицами и условным форматированием без ручного программирования шаблонов — в отличие от FastReport/Stimulsoft",
        reply_markup=keyboard
    )


@router.callback_query(F.data.startswith("zabegayev_2_"))
async def zabegayev_2(call: CallbackQuery, variables: Variables):
    mode = call.data.split("_")[-1]
    text = ""
    if mode == "false":
        text="Миф! Sprinter внедряется за 1 день благодаря модульной архитектуре и готовым адаптерам. Например, в Минфине мы подключили генерацию отчетов за 4 часа. Docker + веб-компоненты — и вы в работе!"
    else:
        text = "✅ Верно!"
    await call.message.edit_text(
        text=text
    )