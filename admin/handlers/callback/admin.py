from aiogram import Router, Bot
from aiogram.types import CallbackQuery


admin_callback_router = Router()


@admin_callback_router.callback_query(lambda c: c.data.startswith("admin_page_"))
async def admin_page_handler(callback: CallbackQuery, variables):
    page = int(callback.data.split("admin_page_")[1])
    
    text = "Админ-панель:"
    keyboard = await variables.keyboards.admin.menu(page=page)

    await callback.message.edit_text(
        text=text,
        reply_markup=keyboard
    )
    
    await callback.answer()


@admin_callback_router.callback_query(lambda c: "/" in c.data and c.data.replace("/", "").replace(" ", "").isdigit())
async def admin_page_info_handler(callback: CallbackQuery):
    await callback.answer()


@admin_callback_router.callback_query(lambda c: c.data.startswith("interactive_") or c.data.startswith("finished_"))
async def speaker_action_handler(callback: CallbackQuery, variables):
    callback_data = callback.data
    
    was_already_pressed = callback_data in variables.keyboards.admin.pressed_buttons
    
    await variables.keyboards.admin.mark_button_pressed(callback_data)
    
    button_text = None
    for text, data in variables.keyboards.admin.all_buttons:
        if data == callback_data:
            button_text = text
            break
    
    if button_text:
        await callback.message.answer(f"📢 {button_text}")
    
    if not was_already_pressed:
        current_page = 0
        for i, (text, data) in enumerate(variables.keyboards.admin.all_buttons):
            if data == callback_data:
                current_page = i // variables.keyboards.admin.buttons_per_page
                break
        
        keyboard = await variables.keyboards.admin.menu(page=current_page)
        await callback.message.edit_reply_markup(reply_markup=keyboard)
    
    await callback.answer()
