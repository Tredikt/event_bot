from aiogram.fsm.state import StatesGroup, State


class BotStates(StatesGroup):
    base = State()
    ending = State()
    ask_speaker = State()
    question = State()

