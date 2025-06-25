from core.operations import KeyboardOperations
from core.utils.button_data import admin_buttons


class AdminKeyboard(KeyboardOperations):
    path = "admin"

    def __init__(self):
        self.all_buttons = admin_buttons
        self.buttons_per_page = 6
        self.total_pages = (len(self.all_buttons) + self.buttons_per_page - 1) // self.buttons_per_page
        self.pressed_buttons = set()
        self.admin_message_id = None
        self.current_page = 0

    async def menu(self, page: int = 0):
        self.current_page = page
        start_index = page * self.buttons_per_page
        end_index = start_index + self.buttons_per_page
        current_page_buttons = self.all_buttons[start_index:end_index]
        
        buttons_dict = {}
        
        for i, (text, callback_data) in enumerate(current_page_buttons):
            if callback_data in self.pressed_buttons:
                display_text = f"✅ {text}"
            else:
                display_text = text
            buttons_dict[i] = [(display_text, callback_data)]
        
        nav_buttons = []
        if page > 0:
            nav_buttons.append(("◀️ Назад", f"admin_page_{page-1}"))
        
        nav_buttons.append((f"{page + 1}/{self.total_pages}", f"number_page_{page + 1}"))
        
        if page < self.total_pages - 1:
            nav_buttons.append(("▶️ Вперед", f"admin_page_{page+1}"))
        
        if len(nav_buttons) > 1:
            buttons_dict[len(current_page_buttons)] = [(btn[0], btn[1]) for btn in nav_buttons]
        
        return await self.create_keyboard(buttons=buttons_dict, architecture=True)
    
    async def mark_button_pressed(self, callback_data: str):
        """Отмечает кнопку как нажатую"""
        self.pressed_buttons.add(callback_data)
    
    def set_admin_message_id(self, message_id: int):
        """Устанавливает ID сообщения с админ-панелью для последующего обновления"""
        self.admin_message_id = message_id
