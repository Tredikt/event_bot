from aiogram.fsm.state import StatesGroup, State


class BotStates(StatesGroup):
    base = State()
    ending = State()
