from core.operations import KeyboardOperations
from core.utils.answer_choices import answer_choices


class MenuKeyboard(KeyboardOperations):
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