import asyncio
from aiogram.enums import ChatAction
from aiogram.types import Message
from aiogram.client import Bot


async def animate_next_question_loading(message: Message, bot: Bot):
    """Показывает прогресс-бар подготовки следующего вопроса"""
    progress_stages = []
    for percent in range(0, 101, 10):
        filled_blocks = percent // 10
        empty_blocks = 10 - filled_blocks
        
        bar = "█" * filled_blocks + "░" * empty_blocks
        
        progress_text = f"""╔════════════════════╗
║ {bar} {percent:3d}%     ║
╚════════════════════╝

🎯 Готовлю следующий вопрос..."""
        
        progress_stages.append(progress_text)
    
    loading_message = await message.answer(text=f"```\n{progress_stages[0]}\n```", parse_mode="Markdown")
    
    for stage in progress_stages[1:]:
        try:
            await loading_message.edit_text(text=f"```\n{stage}\n```", parse_mode="Markdown")
            await asyncio.sleep(0.4)
        except:
            pass
    
    final_message = """╔════════════════════╗
║ ██████████ 100%      ║
╚════════════════════╝

✅ Вопрос готов!"""
    
    try:
        await loading_message.edit_text(text=f"```\n{final_message}\n```", parse_mode="Markdown")
        await asyncio.sleep(0.5)
    except:
        pass
    
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
        
        progress_text = f"""╔════════════════════╗
║ {bar} {percent:3d}%     ║
╚════════════════════╝

🧠 Анализирую ответ{dots}"""
        
        progress_stages.append(progress_text)
    
    loading_message = await message.answer(text=f"```\n{progress_stages[0]}\n```", parse_mode="Markdown")
    
    for stage in progress_stages[1:]:
        try:
            await loading_message.edit_text(text=f"```\n{stage}\n```", parse_mode="Markdown")
            await asyncio.sleep(0.4)
        except:
            pass
    
    final_message = """╔════════════════════╗
║ ██████████ 100%      ║
╚════════════════════╝

✅ Анализ завершён!"""
    
    try:
        await loading_message.edit_text(text=f"```\n{final_message}\n```", parse_mode="Markdown")
        await asyncio.sleep(0.5)
    except:
        pass
    
    await loading_message.delete()