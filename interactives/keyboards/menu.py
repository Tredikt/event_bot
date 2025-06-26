from core.operations import KeyboardOperations
from core.utils.answer_choices import answer_choices, horoshutina_sequence, sadriev_test
from interactives.states import HoroshutinaState


class InteractiveKeyboard(KeyboardOperations):
    def __init__(self):
        super().__init__()
        self.horoshutina_states = {}
        
    async def performance_ending(self, interactive_name: str):
        buttons = {
            "Круто": f"ending_{interactive_name}_cool",
            "Неплохо": f"ending_{interactive_name}_good",
            "Задать вопрос спикеру": f"ask_speaker_{interactive_name}"
        }
        return await self.create_keyboard(buttons=buttons)

    async def belozerova_test(self, number_test: int):
        test_data = answer_choices[number_test - 1]
        options = test_data["options"]
        correct_index = test_data["correct_index"]

        buttons = {
            option: f"belozyortseva_test_{number_test}_{'true' if idx == correct_index else 'false'}"
            for idx, option in enumerate(options)
        }

        return await self.create_keyboard(buttons=buttons)

    async def gavrikov_test(self):
        test_data = answer_choices[2]
        options = test_data["options"]

        buttons = {
            option: "gavrikov_3_selected"
            for option in options
        }

        return await self.create_keyboard(buttons=buttons)

    async def mendubaev_start(self):
        buttons = {
            "1 Вариант": "mendubaev_1",
            "2 Вариант": "mendubaev_2"
        }
        return await self.create_keyboard(buttons=buttons)

    async def mendubaev_1(self):
        buttons = {
            "1 Вариант": "1_mendubaev_1",
            "2 Вариант": "1_mendubaev_2"
        }
        return await self.create_keyboard(buttons=buttons)

    async def mendubaev_2(self):
        buttons = {
            "1 Вариант": "2_mendubaev_1",
            "2 Вариант": "2_mendubaev_2"
        }
        return await self.create_keyboard(buttons=buttons)

    async def mendubaev_final(self):
        buttons = {
            "1 Вариант": "final_mendubaev",
            "2 Вариант": "final_mendubaev"
        }
        return await self.create_keyboard(buttons=buttons)

    async def start_zabegayev(self):
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

        if await state.is_completed():
            return await self.create_keyboard({"🎉 Завершено!": "horoshutina_completed"})
        
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

    async def sadriev_test(self):
        options = sadriev_test["options"]
        correct_index = sadriev_test["correct_index"]

        buttons = {
            option: f"sadriev_test_{'true' if idx == correct_index else 'false'}"
            for idx, option in enumerate(options)
        }

        return await self.create_keyboard(buttons=buttons)

    async def belozyortseva_menu(self):
        """Интерактив Белозерцевой - сразу первый тест"""
        return await self.belozerova_test(number_test=1)

    async def gavrikov_menu(self):
        """Интерактив Гаврикова - сразу тест"""
        return await self.gavrikov_test()

    async def mendubaev_menu(self):
        """Интерактив Мендубаева - сразу варианты"""
        return await self.mendubaev_start()

    async def sadriev_menu(self):
        """Интерактив Садриева - сразу тест"""
        return await self.sadriev_test()

    async def horoshutina_menu(self):
        """Интерактив Хорошутиной - начальные кнопки"""
        buttons = {}
        for item in horoshutina_sequence:
            word = item["word"]
            word_id = item["id"]
            buttons[word] = f"horoshutina_{word_id}"
        
        return await self.create_keyboard(buttons=buttons)

    async def gilmanova_menu(self):
        """Интерактив Гильмановой - после нажатия на кнопку отправляет вопрос"""
        buttons = {
            "Открыть вопрос": "start_gilmanova"
        }
        return await self.create_keyboard(buttons=buttons)

    async def zabegaev_menu(self):
        """Интерактив Забегаева - сразу первый вопрос"""
        return await self.start_zabegayev()

    async def zargaryan_menu(self):
        """Интерактив Заргарян - основные варианты"""
        buttons = {
            "Вариант 1": "zargaryan_1",
            "Вариант 2": "zargaryan_2",
            "Вариант 3": "zargaryan_3"
        }
        return await self.create_keyboard(buttons=buttons)

    async def nurhametova_menu(self):
        """Интерактив Нурхаметовой - основные варианты"""
        buttons = {
            "Ответ А": "nurhametova_a",
            "Ответ Б": "nurhametova_b",
            "Ответ В": "nurhametova_c"
        }
        return await self.create_keyboard(buttons=buttons)
