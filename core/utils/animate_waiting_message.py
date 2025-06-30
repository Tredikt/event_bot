import asyncio
from aiogram.enums import ChatAction
from aiogram.types import Message, CallbackQuery
from aiogram import Bot
from aiogram.utils.keyboard import InlineKeyboardBuilder

from core.utils.enums import Variables


async def animate_next_question_loading(message: Message, bot: Bot):
    """Показывает прогресс-бар подготовки следующего вопроса"""
    progress_stages = []
    for percent in range(0, 101, 10):
        filled_blocks = percent // 10
        empty_blocks = 10 - filled_blocks
        bar = "█" * filled_blocks + "░" * empty_blocks
        progress_text = (f"╔════════════════════╗\n║ {bar} {percent:3d}%     ║\n╚════════════════════╝\n\n🎯 Готовлю следующий вопрос...")
        
        progress_stages.append(progress_text)
    
    loading_message = await message.answer(text=f"```\n{progress_stages[0]}\n```", parse_mode="Markdown")
    
    for stage in progress_stages[1:]:
        try:
            await loading_message.edit_text(text=f"```\n{stage}\n```", parse_mode="Markdown")
            await asyncio.sleep(0.4)
        except Exception as e:
            print(f"Ошибка при анимации подготовки следующего вопроса: {e}")
    
    final_message = ("╔════════════════════╗\n║ ██████████ 100%      ║\n╚════════════════════╝\n\n✅ Вопрос готов!")
    
    try:
        await loading_message.edit_text(text=f"```\n{final_message}\n```", parse_mode="Markdown")
        await asyncio.sleep(0.5)
    except Exception as e:
        print(f"Ошибка при анимации подготовки следующего вопроса: {e}")
    
    await loading_message.delete()


async def animate_answer_analysis(message: Message, bot: Bot):
    """Показывает прогресс-бар анализа ответа пользователя"""
    await bot.send_chat_action(chat_id=message.chat.id, action=ChatAction.TYPING)
    progress_stages = []
    thinking_animations = [".", ".🤔", "...", "..🤖", "..", "..🧐", "."]
    
    for i, percent in enumerate(range(0, 101, 10)):
        filled_blocks = percent // 10
        empty_blocks = 10 - filled_blocks
        bar = "█" * filled_blocks + "░" * empty_blocks
        dots = thinking_animations[i % len(thinking_animations)]
        progress_text = (f"╔════════════════════╗\n║ {bar} {percent:3d}%     ║\n╚════════════════════╝\n\n🧠 Анализирую ответ{dots}")
        progress_stages.append(progress_text)
    
    loading_message = await message.answer(text=f"```\n{progress_stages[0]}\n```", parse_mode="Markdown")
    
    for stage in progress_stages[1:]:
        try:
            await loading_message.edit_text(text=f"```\n{stage}\n```", parse_mode="Markdown")
            await asyncio.sleep(0.4)
        except Exception as e:
            print(f"Ошибка при анимации анализа ответа: {e}")
    
    final_message = ("╔════════════════════╗\n║ ██████████ 100%      ║\n╚════════════════════╝\n\n✅ Анализ завершён!")
    
    try:
        await loading_message.edit_text(text=f"```\n{final_message}\n```", parse_mode="Markdown")
        await asyncio.sleep(0.5)
    except Exception as e:
        print(f"Ошибка при анимации анализа ответа: {e}")
    
    await loading_message.delete()


async def animate_buttons_appearance(message: Message, bot: Bot, buttons_data: dict, callback_prefix: str):
    """Постепенно добавляет кнопки к существующему сообщению"""
    builder = InlineKeyboardBuilder()
    await asyncio.sleep(0.8)
    
    for idx, (button_text, callback_data) in enumerate(buttons_data.items()):
        await asyncio.sleep(0.6)
        builder.button(text=button_text, callback_data=callback_data)
        builder.adjust(1)
        try:
            await message.edit_text(
                text=message.text,
                reply_markup=builder.as_markup()
            )
        except Exception as e:
            print(f"Ошибка при добавлении кнопок: {e}")
        await asyncio.sleep(0.5)


async def send_staged_question(
    call: CallbackQuery, 
    variables: Variables,
    start_text: str,
    main_text: str, 
    question_text: str, 
    buttons_data: dict, 
    callback_prefix: str,
    main_text_delay: float = 2.5,
    question_delay: float = 2.0
):
    """
    Универсальная функция для поэтапной отправки вопросов с анимацией
    
    Args:
        call: CallbackQuery объект
        variables: Variables объект
        main_text: Основной текст (например, "Бэкенд сервиса разделён на две ключевые части")
        question_text: Текст вопроса (например, "Какие?")
        buttons_data: Словарь с данными кнопок {text: callback_data}
        callback_prefix: Префикс для callback_data кнопок
        main_text_delay: Задержка после основного текста (по умолчанию 2.5 сек)
        question_delay: Задержка после "Вопрос...." (по умолчанию 2.0 сек)
    """
    await call.message.answer(text=start_text)
    await call.bot.send_chat_action(chat_id=call.message.chat.id, action=ChatAction.TYPING)
    await asyncio.sleep(main_text_delay)
    await call.message.answer(text=main_text)
    await variables.bot.send_chat_action(chat_id=call.message.chat.id, action=ChatAction.TYPING)
    await asyncio.sleep(question_delay)
    question_message = await call.message.answer(text=question_text)
    
    await animate_buttons_appearance(
        message=question_message,
        bot=call.bot,
        buttons_data=buttons_data,
        callback_prefix=callback_prefix
    )