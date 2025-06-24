class HoroshutinaState:
    def __init__(self):
        self.current_step = 1
        self.wrong_selections = set()
        self.completed_steps = set()
        
    def add_wrong_selection(self, word):
        self.wrong_selections.add(word)
        
    def complete_step(self, word):
        self.completed_steps.add(word)
        self.wrong_selections.clear()
        self.current_step += 1
        
    def is_completed(self):
        return self.current_step > 6
        
    def reset(self):
        self.current_step = 1
        self.wrong_selections.clear()
        self.completed_steps.clear()
        
    def get_expected_word(self, sequence_data):
        for item in sequence_data:
            if item["order"] == self.current_step:
                return item["word"]
        return None
