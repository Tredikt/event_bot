from functools import wraps
from typing import Callable, Any
from aiogram.types import CallbackQuery
from core.utils.enums import Variables



def admin_interactive(handler: Callable) -> Callable:
    """
    Декоратор для интерактивов админ-панели.
    Автоматически отмечает кнопки и отвечает на callback
    """
    @wraps(handler)
    async def wrapper(*args, **kwargs):
        callback = None
        variables = None
        
        for arg in args:
            if isinstance(arg, CallbackQuery):
                callback = arg
            if hasattr(arg, 'keyboards'):
                variables = arg
        
        if 'callback' in kwargs:
            callback = kwargs['callback']
        if 'variables' in kwargs:
            variables = kwargs['variables']
        
        if not callback:
            return await handler(*args, **kwargs)
            
        callback_data = callback.data
        
        result = await handler(*args, **kwargs)
        
        if callback_data.startswith(("interactive_", "finished_")):
            was_already_pressed = callback_data in variables.keyboards.admin.pressed_buttons
            
            await variables.keyboards.admin.mark_button_pressed(callback_data=callback_data)
            
            if not was_already_pressed:
                current_page = 0
                for i, (text, data) in enumerate(variables.keyboards.admin.all_buttons):
                    if data == callback_data:
                        current_page = i // variables.keyboards.admin.buttons_per_page
                        break
                
                try:
                    keyboard = await variables.keyboards.admin.menu(page=current_page)
                    
                    if variables.keyboards.admin.admin_message_id:
                        await variables.bot.edit_message_reply_markup(
                            chat_id=callback.message.chat.id,
                            message_id=variables.keyboards.admin.admin_message_id,
                            reply_markup=keyboard
                        )
                    else:
                        sent_message = await callback.message.answer(
                            "🔧 Админ-панель:",
                            reply_markup=keyboard
                        )
                        variables.keyboards.admin.set_admin_message_id(sent_message.message_id)
                except Exception as e:
                    print(f"❌ Ошибка обновления админской клавиатуры: {e}")
        
        try:
            await callback.answer()
        except:
            pass
        
        return result
    
    return wrapper 