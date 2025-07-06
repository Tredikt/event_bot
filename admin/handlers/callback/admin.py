import asyncio
from aiogram import Router, F
from aiogram.types import CallbackQuery

from core.utils.delete_keyboard import delete_keyboard
from core.utils.enums import Variables
from core.utils.interactive_messages import get_interactive_message, get_performance_start_message
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


@router.callback_query(F.data.startswith("start_perfomance_"))
async def performance_start_handler(callback: CallbackQuery, variables: Variables):
    speaker_name = callback.data.split("start_perfomance_")[1]
    await variables.keyboards.admin.mark_button_pressed(callback_data=callback.data)
    await AdminPanelService.update_admin_panel(callback=callback, variables=variables)
    text = get_performance_start_message(speaker_name=speaker_name)
    await variables.db.speaker.add_or_update(name=speaker_name)

    asyncio.create_task(variables.broadcast_service.send_custom_message(text=text))

    await callback.answer(text=f"Запущена рассылка о начале выступления {get_speaker_display_name(speaker_name=speaker_name)}")


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

    if speaker_name == "all":
        text = "Спасибо, что был с нами на Годовом собрании!\n🎉Помоги нам стать лучше — оставь обратную связь: forms.gle/zsmkbSVUU8oyARjv5\nУвидимся в следующем году! 🚀"
        display_name = "всех выступлений"
        keyboard = await variables.keyboards.menu.get_empty_keyboard()
    else:
        text = get_interactive_message(speaker_name=speaker_name, message_type="end")
        display_name = f"выступления {get_speaker_display_name(speaker_name=speaker_name)}"
        keyboard = await variables.keyboards.interactives.performance_ending(interactive_name=speaker_name)
        await variables.db.user.update_feedback_waiting(speaker_name=speaker_name)

    asyncio.create_task(variables.broadcast_service.send_end_broadcast(
        speaker_name=speaker_name,
        text=text,
        keyboard=keyboard
    ))

    await callback.answer(text=f"Запущена рассылка об окончании {display_name}")

