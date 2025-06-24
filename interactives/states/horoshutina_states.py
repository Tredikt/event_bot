class HoroshutinaState:
    def __init__(self):
        self.current_step = 1
        self.wrong_selections = set()
        self.completed_steps = set()
        
    async def add_wrong_selection(self, word: str) -> None:
        """Добавляет неправильный выбор в список неправильных выборов"""
        self.wrong_selections.add(word)
        
    async def complete_step(self, word: str) -> None:
        """Завершает текущий шаг и сбрасывает неправильные выборы"""
        self.completed_steps.add(word)
        self.wrong_selections.clear()
        self.current_step += 1
        
    async def is_completed(self) -> bool:
        """Проверяет, завершен ли интерактив"""
        return self.current_step > 6
        
    async def reset(self) -> None:
        """Сбрасывает состояние интерактива"""
        self.current_step = 1
        self.wrong_selections.clear()
        self.completed_steps.clear()
        
    async def get_expected_word(self, sequence_data: list[dict]) -> str:
        """Получает ожидаемое слово для текущего шага"""
        for item in sequence_data:
            if item["order"] == self.current_step:
                return item["word"]
        return None
