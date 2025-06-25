class GilmanovaState:
    def __init__(self):
        self.attempts_count: int = 0
        self.max_attempts: int = 3
        self.is_active: bool = False
        self.is_finished: bool = False
        
    async def start_interactive(self) -> None:
        self.is_active = True
        self.attempts_count = 0
        self.is_finished = False
        
    async def add_attempt(self) -> None:
        self.attempts_count += 1
        
    async def get_attempts_count(self) -> int:
        return self.attempts_count
        
    async def get_max_attempts(self) -> int:
        return self.max_attempts
        
    async def is_interactive_active(self) -> bool:
        return self.is_active
        
    async def is_interactive_finished(self) -> bool:
        return self.is_finished
        
    async def finish_interactive(self) -> None:
        self.is_finished = True
        self.is_active = False
        
    async def reset(self) -> None:
        self.attempts_count = 0
        self.is_active = False
        self.is_finished = False
        
    async def has_attempts_left(self) -> bool:
        return self.attempts_count < self.max_attempts
        
    async def get_failure_message(self) -> str:
        if self.attempts_count == 1:
            return "Круто, ты был близок, попробуй ещё"
        elif self.attempts_count == 2:
            return "Подумай ещё"
        else:
            return "Сейчас спикер скажет правильный ответ"
