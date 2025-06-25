from aiogram import Router, F
from aiogram.types import Message, CallbackQuery

from core.utils.enums import Variables

mendubaev_router = Router()


@mendubaev_router.callback_query(F.data == "mendubaev")
async def first_mendubaev(call: CallbackQuery, variables: Variables):
    text = "Сегодня 11 июля.  Вам поступила задача от заказчика на реализацию электронного согласования документов. В ходе анализа и обсуждения выявлены следующие требования (выберите подходящий вариант)\n1 Вариант\n- Простая статусная модель\n- Несложная орг. структура\n- Процессы стабильны во времени\n2 Вариант\n- Гибкие процессы с ветвлением и циклами\n- Сложные стратегии принятия решений\n- Обеспечение юридической значимости"
    keyboard = await variables.keyboards.menu.mendubaev_start()
    await call.message.answer(
        text=text,
        reply_markup=keyboard
    )


@mendubaev_router.callback_query(F.data.startswith("mendubaev"))
async def second_mendubaev(call: CallbackQuery, variables: Variables):
    mode = call.data.split("_")[-1]
    if mode == "1":
        text = "Отлично! Все получится Быстро, Дешево, и конечно будет работать! 12 июля вы приступили к работам. 19 июля на встрече с Заказчиком он попросил\n1 Вариант\n'Добавить еще пару статусов, но чтобы они были только вот тут'\n2 Вариант\n'Немного поменять вот этот вот процесс вот как-то так'"
        keyboard = await variables.keyboards.menu.mendubaev_1()
        await call.message.edit_text(
            text=text,
            reply_markup=keyboard
        )
    else:
        text = "Отлично!\nВам выделили много времени, большие бюджеты.\nВсе должно получится классно!\n12 июля вы приступили к работам.\n12 августа на встрече с Заказчиком он попросил в приоритете переключиться с Согласования на интеграцию со СМЭВ\nВы:'Хорошо, но мы будем вынуждены...'\n1 Вариант\nИсключить из плана настраиваемые стратегии принятия решений\n2 Вариант\nУпростить визуальный редактор, и оставить только линейные процессы"
        keyboard = await variables.keyboards.menu.mendubaev_2()
        await call.message.edit_text(
            text=text,
            reply_markup=keyboard
        )


@mendubaev_router.callback_query(F.data.startswith("1_mendubaev_"))
async def third_mendubaev(call: CallbackQuery, variables: Variables):
    mode = call.data.split("_")[-1]
    if mode == "1":
        text = "Без проблем! Мы уже почти закончили, но еще можем сделать эти правки.\n'Спустя 2 недели на очередном Демо Заказчик сказал:Мы тут еще подумали, и решили:...'1 Вариант\n'вот эти статусы мы все-таки уберем и изменим логику перехода'2 Вариант\n'у Руководителя есть Зам и нужно, чтобы он тоже мог утвердить документ'"
        keyboard = await variables.keyboards.menu.mendubaev_final_1()
        await call.message.edit_text(
            text=text,
            reply_markup=keyboard
        )
    else:
        text = "Без проблем! Мы уже почти закончили, но еще можем сделать эти правки.\n'Спустя 2 недели на очередном Демо Заказчик сказал:Мы тут еще подумали, и решили:...'1 Вариант\n'вот эти статусы мы все-таки уберем и изменим логику перехода'2 Вариант\n'у Руководителя есть Зам и нужно, чтобы он тоже мог утвердить документ'"
        keyboard = await variables.keyboards.menu.mendubaev_final_1()
        await call.message.edit_text(
            text=text,
            reply_markup=keyboard
        )


@mendubaev_router.callback_query(F.data.startswith("2_mendubaev_"))
async def fourth_mendubaev(call: CallbackQuery, variables: Variables):
    mode = call.data.split("_")[-1]
    if mode == "1":
        text = "Спустя месяц интеграция со СМЭВ реализована, часть команды вернулась к работе над Согласованием. Еще спустя время на демонстрации Заказчику функционала параллельного согласования ...\n1 Вариант\nЗаказчик сказал: 'Конечно, хорошо, но вы один раз все сами настроите, больше менять нам не нужно, а вот где настраиваются стратегии принятия решений? Это нам точно потребуется!'\n2 Вариант\nУ вас упал стенд, потому что не хватило времени на комплексное тестирование  гибкого, но и от того сложного функционала"
        keyboard = await variables.keyboards.menu.mendubaev_final_2()
        await call.message.edit_text(
            text=text,
            reply_markup=keyboard
        )
    else:
        text = "Спустя месяц интеграция со СМЭВ реализована, часть команды вернулась к работе над Согласованием.  Еще спустя время на демонстрации Заказчику функционала работы со стратегиями принятий решений ...\n1 Вариант\nЗаказчик сказал: 'Конечно, хорошо, но решения принимаются у нас всегда одинаково - большинством, а как сделать параллельное согласование несколькими подразделениями? Это нам точно потребуется!'2 Варинт\nУ вас упал стенд, потому что не хватило времени на комплексное тестирование гибкого, но и от того сложного функционала"
        keyboard = await variables.keyboards.menu.mendubaev_final_2()
        await call.message.edit_text(
            text=text,
            reply_markup=keyboard
        )


@mendubaev_router.callback_query(F.data.startswith("final_mendubaev"))
async def final_mendubaev(call: CallbackQuery):
    mode = call.data.split("_")[-1]
    if mode == "1":
        text = "Некоторое время спустя...\nРЕЗУЛЬТАТ\nУра, все работает!\nЗатраты: «быстро» x N, «дёшево» x N\n\nМы в «предвкушении» новых требований…"
    else:
        text = "Некоторое время спустя...\nРЕЗУЛЬТАТ\nСделали, сколько успели.\nВ целом все работает, но бывают баги\nПоловина изначально запрошенных возможностей оказалась не нужна.\nПолучилось специфическое под конкретного Заказчика решение.\nПетю нельзя отпускать 'далеко' от проекта, потому что только он знает, как тут все работает."

    await call.message.edit_text(
        text=text
    )