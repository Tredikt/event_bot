from core.operations import KeyboardOperations
from core.utils.answer_choices import answer_choices, horoshutina_sequence, sadriev_test
from interactives.states import HoroshutinaState


class InteractiveKeyboard(KeyboardOperations):
    def __init__(self):
        super().__init__()
        self.horoshutina_states = {}
        
    async def performance_ending(self, interactive_name: str, rows: int = 1):
        buttons_dict = {
            "Круто": f"ending_{interactive_name}_cool",
            "Неплохо": f"ending_{interactive_name}_good",
            "Задать вопрос спикеру": f"ask_speaker_{interactive_name}"
        }
        buttons = dict()
        for num, (key, value) in enumerate(buttons_dict.items()):
            if num + 1 <= rows:
                buttons[key] = value
        
        return await self.create_keyboard(buttons=buttons)

    async def nurkhametova_start_interactive(self):
        buttons = {
            "Запустить интерактив": "nurkhametova_start_interactive"
        }
        return await self.create_keyboard(buttons=buttons)

    async def belozyortseva_start_interactive(self):
        buttons = {
            "Запустить интерактив": "start_belozyortseva_interactive"
        }
        return await self.create_keyboard(buttons=buttons)

    async def belozyortseva_menu(self, number_test: int):
        test_data = answer_choices[number_test - 1]
        options = test_data["options"]

        buttons = {
            option: f"belozyortseva_test_{number_test}_{idx}"
            for idx, option in enumerate(options)
        }

        return await self.create_keyboard(buttons=buttons)

    async def gavrikov_menu(self):
        buttons = {
            "Начать тест": "gavrikov_start"
        }
        return await self.create_keyboard(buttons=buttons)

    async def gavrikov_start(self):
        buttons = {
            "Что такое ЖКХ?": "gavrikov_pictures",
            "Не понимаю": "gavrikov_pictures",
            "Понимаю": "gavrikov_pictures",
            "Я сам участвовал в реализации этого проекта": "gavrikov_pictures",
        }
        return await self.create_keyboard(buttons=buttons, interval=2, count=2)

    async def zabegayev_start_interactive(self):
        buttons = {
            "Запустить интерактив": "zabegayev_start_interactive"
        }
        return await self.create_keyboard(buttons=buttons)

    async def zabegayev_menu(self):
        buttons = {
            "Правда": "start_zabegayev_false",
            "Ложь": "start_zabegayev_true"
        }
        return await self.create_keyboard(buttons=buttons)

    async def zabegayev_1(self):
        buttons = {
            "Правда": "zabegayev_1_false",
            "Ложь": "zabegayev_1_true"
        }
        return await self.create_keyboard(buttons=buttons)


    async def zabegayev_2(self):
        buttons = {
            "Правда": "zabegayev_2_true",
            "Ложь": "zabegayev_2_false"
        }
        return await self.create_keyboard(buttons=buttons)
    
    async def interactive_horoshutina(self, user_id):
        if user_id not in self.horoshutina_states:
            self.horoshutina_states[user_id] = HoroshutinaState()
            
        state: HoroshutinaState = self.horoshutina_states[user_id]

        if await state.is_completed():
            state = self.horoshutina_states[user_id]

        buttons = {}
        for item in horoshutina_sequence:
            word = item["word"]
            order = item["order"]
            word_id = item["id"]
            
            display_text = word
            
            if word in state.completed_steps:
                number_emoji = ["1️⃣", "2️⃣", "3️⃣", "4️⃣", "5️⃣", "6️⃣"][order - 1]
                display_text = f"{number_emoji} {word}"
            elif word in state.wrong_selections:
                display_text = f"❌ {word}"
                
            buttons[display_text] = f"horoshutina_{word_id}"
        
        return await self.create_keyboard(buttons=buttons)

    async def sadriev_start_interactive(self):
        buttons = {
            "Запустить интерактив": "sadriev_start_interactive"
        }
        return await self.create_keyboard(buttons=buttons)

    async def sadriev_menu(self):
        options = sadriev_test["options"]

        buttons = {
            option: f"sadriev_test_{idx}"
            for idx, option in enumerate(options)
        }

        return await self.create_keyboard(buttons=buttons)

    async def horoshutina_menu(self):
        """Интерактив Хорошутиной - начальные кнопки"""
        buttons = {}
        for item in horoshutina_sequence:
            word = item["word"]
            word_id = item["id"]
            buttons[word] = f"horoshutina_{word_id}"
        
        return await self.create_keyboard(buttons=buttons)

    async def zabegaev_menu(self):
        """Интерактив Забегаева - кнопка запуска интерактива"""
        return await self.zabegayev_start_interactive()


