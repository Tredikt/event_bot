from core.operations import KeyboardOperations


class AdminKeyboard(KeyboardOperations):
    path = "admin"

    def __init__(self):
        self.all_buttons = [
            ("Белозерцева - Интерактив", "interactive_belozertseva"),
            ("Белозерцеева - Закончила выступление", "finished_belozertseva"),
            
            ("Гавриков - Интерактив", "interactive_gavrikov"),
            ("Гавриков - Закончил выступление", "finished_gavrikov"),
            
            ("Забегаев - Интерактив", "interactive_zabegaev"),
            ("Забегаев - Закончил выступление", "finished_zabegaev"),
            
            ("Заргарян - Интерактив", "interactive_zargaryan"),
            ("Заргарян - Закончил выступление", "finished_zargaryan"),
            
            ("Мендубаев - Интерактив", "interactive_mendubaev"),
            ("Мендубаев - Закончил выступление", "finished_mendubaev"),
            
            ("Нурхаметова - Интерактив", "interactive_nurhametova"),
            ("Нурхаметова - Закончила выступление", "finished_nurhametova"),
            
            ("Садриев - Интерактив", "interactive_sadriev"),
            ("Садриев - Закончил выступление", "finished_sadriev"),
            
            ("Хорошутина - Интерактив", "interactive_horoshutina"),
            ("Хорошутина - Закончила выступление", "finished_horoshutina"),
            
            ("Гильманова - Интерактив", "interactive_gilmanova"),
            ("Гильманова - Закончила выступление", "finished_gilmanova"),
        ]
        self.buttons_per_page = 6
        self.total_pages = (len(self.all_buttons) + self.buttons_per_page - 1) // self.buttons_per_page
        self.pressed_buttons = set()

    async def menu(self, page: int = 0):
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
        
        nav_buttons.append((f"{page + 1}/{self.total_pages}", f"{page + 1}/{self.total_pages}"))
        
        if page < self.total_pages - 1:
            nav_buttons.append(("▶️ Вперед", f"admin_page_{page+1}"))
        
        if len(nav_buttons) > 1:
            buttons_dict[len(current_page_buttons)] = [(btn[0], btn[1]) for btn in nav_buttons]
        
        return await self.create_keyboard(buttons=buttons_dict, architecture=True)
    
    async def mark_button_pressed(self, callback_data: str):
        """Отмечает кнопку как нажатую"""
        self.pressed_buttons.add(callback_data)
