from interactives.keyboards import InteractiveKeyboard
from admin.keyboards import AdminKeyboard


class Keyboards:
    def __init__(self):
        self.menu = InteractiveKeyboard()
        self.admin = AdminKeyboard()
        self.interactives = InteractiveKeyboard()
