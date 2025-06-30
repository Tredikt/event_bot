import asyncio
from aiogram import Router, F
from aiogram.types import CallbackQuery
from core.utils.enums import Variables
from core.utils.interactive_messages import get_interactive_message
from core.utils.speaker_utils import get_speaker_display_name
from admin.services import AdminPanelService


router = Router(name="admin_callback")


@router.callback_query(F.data.startswith("admin_page_"))
async def admin_page_handler(callback: CallbackQuery, variables: Variables):
    page = int(callback.data.split("admin_page_")[1])
    
    users_count = await variables.broadcast_service.get_users_count()
    text = f"Админ-панель:\nПользователей в базе: {users_count}"
    keyboard = await variables.keyboards.admin.menu(page=page)

    await callback.message.edit_text(
        text=text,
        reply_markup=keyboard
    )
    
    await callback.answer()


@router.callback_query(F.data.startswith("number_page_"))
async def admin_page_info_handler(callback: CallbackQuery):
    await callback.answer()


@router.callback_query(F.data.startswith("interactive_"))
async def interactive_start_handler(callback: CallbackQuery, variables: Variables):
    speaker_name = callback.data.split("interactive_")[1]
    await variables.keyboards.admin.mark_button_pressed(callback_data=callback.data)
    await AdminPanelService.update_admin_panel(callback=callback, variables=variables)
    keyboard = await variables.broadcast_service.get_interactive_keyboard(speaker_name=speaker_name)
    text = get_interactive_message(speaker_name=speaker_name, message_type="start")

    asyncio.create_task(variables.broadcast_service.send_interactive_broadcast(
        speaker_name=speaker_name,
        text=text,
        keyboard=keyboard
    ))

    await callback.answer(text=f"Запущена рассылка интерактива {get_speaker_display_name(speaker_name=speaker_name)}")


@router.callback_query(F.data.startswith("finished_"))
async def interactive_end_handler(callback: CallbackQuery, variables: Variables):
    speaker_name = callback.data.split("finished_")[1]
    await variables.keyboards.admin.mark_button_pressed(callback_data=callback.data)
    await AdminPanelService.update_admin_panel(callback=callback, variables=variables)
    text = get_interactive_message(speaker_name=speaker_name, message_type="end")
    
    asyncio.create_task(variables.broadcast_service.send_end_broadcast(
        speaker_name=speaker_name,
        text=text,
        keyboard=await variables.keyboards.interactives.performance_ending(interactive_name=speaker_name)
    ))
    
    await callback.answer(text=f"Запущена рассылка об окончании выступления {get_speaker_display_name(speaker_name=speaker_name)}")
