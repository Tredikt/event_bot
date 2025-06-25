from core.operations import KeyboardOperations
from core.utils.answer_choices import answer_choices, horoshutina_sequence, sadriev_test
from interactives.states import interactive_states, HoroshutinaState


class InteractiveKeyboard(KeyboardOperations):
    def __init__(self):
        super().__init__()
        self.horoshutina_states = {}

    async def belozerova_test(self, number_test: int):
        test_data = answer_choices[number_test - 1]
        options = test_data["options"]
        correct_index = test_data["correct_index"]

        buttons = {
            option: f"belozyortseva_test_{number_test}_{'true' if idx == correct_index else 'false'}"
            for idx, option in enumerate(options)
        }

        return await self.create_keyboard(buttons=buttons)

    async def gavrikov_start(self):
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

    async def zabegayev(self, step: str):
        buttons = {
            "Правда": f"zabegayev_{step}_true",
            "Ложь": f"zabegayev_{step}_false"
        }

    async def interactive_horoshutina(self, user_id):
        if user_id not in self.horoshutina_states:
            self.horoshutina_states[user_id] = interactive_states["HoroshutinaState"]()
            
        state: HoroshutinaState = self.horoshutina_states[user_id]

        if await state.is_completed():

        state = self.horoshutina_states[user_id]

        if state.is_completed():
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



    async def interactive_nurkhametova(self):
        buttons = {
            "семейные права": "interactive_nurkhametova_0_true",
            "гражданские права": "interactive_nurkhametova_0_false",
            "административные права": "interactive_nurkhametova_0_false"
        }
        return await self.create_keyboard(buttons=buttons)

    async def interactive_nurkhametova_1(self):
        buttons = {
            "Право на справедливый суд (ст. 46 Конституции)": "interactive_nurkhametova_1_true",
            "Гражданское право": "interactive_nurkhametova_1_false",
            "Право на предпринимательство": "interactive_nurkhametova_1_false"
        }
        return await self.create_keyboard(buttons=buttons)

    async def interactive_nurkhametova_2(self):
        buttons = {
            "Гражданское право": "interactive_nurkhametova_2_false",
            "Социальное право": "interactive_nurkhametova_2_true",
            "Право на образование": "interactive_nurkhametova_2_false"
        }
        return await self.create_keyboard(buttons=buttons)

    async def interactive_nurkhametova_3(self):
        buttons = {
            "Гражданские права": "interactive_nurkhametova_3_false",
            "Административные права": "interactive_nurkhametova_3_true",
            "Жилищные права": "interactive_nurkhametova_3_false"
        }
        return await self.create_keyboard(buttons=buttons)

    async def sadriev_test(self):
        options = sadriev_test["options"]
        correct_index = sadriev_test["correct_index"]

        buttons = {
            option: f"sadriev_test_{'true' if idx == correct_index else 'false'}"
            for idx, option in enumerate(options)
        }

        return await self.create_keyboard(buttons=buttons)

