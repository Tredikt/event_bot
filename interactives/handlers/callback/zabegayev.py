from aiogram import Router, F
from aiogram.types import Message, CallbackQuery

from core.utils.enums import Variables

zabegayev_router = Router()


@zabegayev_router.callback_query(F.data == "zabegayev")
async def zabegayev(call: CallbackQuery, variables: Variables):
    text = "Sprinter требует установки толстых клиентов в каждую систему"
    keyboard = await variables.keyboards.menu.start_zabegayev()
    await call.message.edit_text(
        text=text,
        reply_markup=keyboard
    )


@zabegayev_router.callback_query(F.data.startswith("start_zabegayev_"))
async def start_zabegayev(call: CallbackQuery, variables: Variables):
    mode = call.data.split("_")[-1]
    keyboard = await variables.keyboards.menu.zabegayev_1()
    if mode == "false":
        await call.message.edit_text(
            text="Неверно! В отличие от legacy-решений, Sprinter работает в браузере без установки — это принципиальное архитектурное преимущество. Никаких зависимостей, никаких 'квестов' с обновлениями. Открыли веб-интерфейс — и работаете даже с планшета!"
        )
    await call.message.answer(
        text="Настройка Sprinter под госсистемы (например, 'Электронный бюджет') занимает 3+ месяца из-за сложной интеграции",
        reply_markup=keyboard
    )


@zabegayev_router.callback_query(F.data.startswith("zabegayev_1_"))
async def zabegayev_2(call: CallbackQuery, variables: Variables):
    mode = call.data.split("_")[-1]
    keyboard = await variables.keyboards.menu.zabegayev_2()
    if mode == "false":
        await call.message.edit_text(
            text="Миф! Sprinter внедряется за 1 день благодаря модульной архитектуре и готовым адаптерам. Например, в Минфине мы подключили генерацию отчетов за 4 часа. Docker + веб-компоненты — и вы в работе!"
    )
    await call.message.edit_text(
        text="Sprinter генерирует сложные документы с динамическими таблицами и условным форматированием без ручного программирования шаблонов — в отличие от FastReport/Stimulsoft",
        reply_markup=keyboard
    )