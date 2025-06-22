from interactives.keyboards import MenuKeyboard
from admin.keyboards import AdminKeyboard


class Keyboards:
    def __init__(self):
        self.menu = MenuKeyboard()
        self.admin = AdminKeyboard()
