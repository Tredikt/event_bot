from core.operations import KeyboardOperations
from core.utils.answer_choices import answer_choices


class InteractiveKeyboard(KeyboardOperations):
    async def belozerova_test(self, number_test: int):
        test_data = answer_choices[number_test - 1]
        options = test_data["options"]
        correct_index = test_data["correct_index"]

        buttons = {
            option: f"belozerova_test_{number_test}_{'true' if idx == correct_index else 'false'}"
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
