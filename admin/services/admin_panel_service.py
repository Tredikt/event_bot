from aiogram.types import CallbackQuery
from core.utils.enums import Variables


class AdminPanelService:
    
    @staticmethod
    async def update_admin_panel(callback: CallbackQuery, variables: Variables) -> None:
        """Обновляет админ-панель после изменения состояния кнопок"""
        
        try:
            symbol = "!" if "." in callback.message.text else "."
            users_count = await variables.broadcast_service.get_users_count()
            text = f"Админ-панель:\nПользователей в базе: {users_count}{symbol}"
            keyboard = await variables.keyboards.admin.menu(page=variables.keyboards.admin.current_page)
            
            await callback.message.edit_text(
                text=text,
                reply_markup=keyboard
            )
            
        except Exception as e:
            print(f"Ошибка обновления админ-панели: {e}") 