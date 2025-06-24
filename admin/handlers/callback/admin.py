from aiogram import Router, F
from aiogram.types import CallbackQuery
from core.utils.enums import Variables


router = Router(name="admin_callback")


@router.callback_query(F.data.startswith("admin_page_"))
async def admin_page_handler(callback: CallbackQuery, variables: Variables):
    page = int(callback.data.split("admin_page_")[1])
    
    text = "Админ-панель:"
    keyboard = await variables.keyboards.admin.menu(page=page)

    await callback.message.edit_text(
        text=text,
        reply_markup=keyboard
    )
    
    await callback.answer()


@router.callback_query(F.data.startswith("number_page_"))
async def admin_page_info_handler(callback: CallbackQuery):
    await callback.answer()
