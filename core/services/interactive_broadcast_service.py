from typing import List, Optional
from aiogram import Bot
from aiogram.types import InlineKeyboardMarkup

from core.keyboards_class import Keyboards
from core.models import User
from core.repositories import UserRepository
from core.services.broadcast_service import BroadcastService


class InteractiveBroadcastService:
    def __init__(self, bot: Bot, user_repository: UserRepository):
        self.bot = bot
        self.user_repository = user_repository
        self.broadcast_service = BroadcastService(bot)

    async def send_interactive_start(
        self,
        interactive_name: str,
        text: str,
        keyboard: InlineKeyboardMarkup
    ) -> dict[str, int]:
        """Отправляет начало интерактива всем пользователям"""
        
        users = await self._get_all_active_users()
        
        if not users:
            return {
                "total_sent": 0,
                "total_failed": 0,
                "total_users": 0,
                "error": "Нет пользователей в базе данных"
            }
        
        result = await self.broadcast_service.send_interactive_to_all_users(
            users=users,
            text=text,
            keyboard=keyboard
        )
        
        print(f"Рассылка интерактива '{interactive_name}' завершена. "
              f"Отправлено: {result['total_sent']}, "
              f"Ошибок: {result['total_failed']}")
        
        return result

    async def send_interactive_end(
        self,
        interactive_name: str,
        text: str,
        keyboard: Optional[InlineKeyboardMarkup] = None
    ) -> dict[str, int]:
        """Отправляет окончание интерактива всем пользователям"""
        
        users = await self._get_all_active_users()
        
        if not users:
            return {
                "total_sent": 0,
                "total_failed": 0,
                "total_users": 0,
                "error": "Нет пользователей в базе данных"
            }
        
        result = await self.broadcast_service.send_interactive_to_all_users(
            users=users,
            text=text,
            keyboard=keyboard
        )
        
        print(f"Рассылка окончания интерактива '{interactive_name}' завершена. "
              f"Отправлено: {result['total_sent']}, "
              f"Ошибок: {result['total_failed']}")
        
        return result

    async def send_custom_message(
        self,
        text: str,
        keyboard: Optional[InlineKeyboardMarkup] = None
    ) -> dict[str, int]:
        """Отправляет произвольное сообщение всем пользователям"""
        
        users = await self._get_all_active_users()
        
        if not users:
            return {
                "total_sent": 0,
                "total_failed": 0,
                "total_users": 0,
                "error": "Нет пользователей в базе данных"
            }
        
        result = await self.broadcast_service.send_interactive_to_all_users(
            users=users,
            text=text,
            keyboard=keyboard
        )
        
        print(f"Рассылка сообщения завершена. "
              f"Отправлено: {result['total_sent']}, "
              f"Ошибок: {result['total_failed']}")
        
        return result

    async def _get_all_active_users(self) -> List[User]:
        """Получает всех активных пользователей из базы данных"""
        
        try:
            users = await self.user_repository.get_all_users()
            return [user for user in users if user.user_id]
        except Exception as e:
            print(f"Ошибка получения пользователей: {e}")
            return []

    async def get_users_count(self) -> int:
        """Возвращает количество пользователей в базе"""
        
        users = await self._get_all_active_users()
        return len(users)

    async def send_interactive_broadcast(
        self,
        speaker_name: str,
        text: str,
        keyboard: Optional[InlineKeyboardMarkup]
    ) -> dict[str, int]:
        """Отправляет рассылку начала интерактива с инициализацией состояний"""
        
        try:
            result = await self.send_interactive_start(
                interactive_name=speaker_name,
                text=text,
                keyboard=keyboard
            )
            
            print(f"Интерактив {speaker_name}: отправлено {result['total_sent']} сообщений, ошибок: {result['total_failed']}")
            return result
            
        except Exception as e:
            print(f"Ошибка рассылки интерактива {speaker_name}: {e}")
            return {"total_sent": 0, "total_failed": 1, "total_users": 0, "error": str(e)}

    async def send_end_broadcast(
        self,
        speaker_name: str,
        text: str,
        keyboard: Optional[InlineKeyboardMarkup]
    ) -> dict[str, int]:
        """Отправляет рассылку об окончании выступления"""
        
        try:
            result = await self.send_interactive_end(
                interactive_name=speaker_name,
                text=text,
                keyboard=keyboard
            )
            
            print(f"Окончание {speaker_name}: отправлено {result['total_sent']} сообщений, ошибок: {result['total_failed']}")
            return result
            
        except Exception as e:
            print(f"Ошибка рассылки окончания {speaker_name}: {e}")
            return {"total_sent": 0, "total_failed": 1, "total_users": 0, "error": str(e)}

    async def get_interactive_keyboard(self, speaker_name: str):
        """Получает клавиатуру для конкретного интерактива"""
        
        keyboard_mapping = {
            "belozertseva": self._get_keyboard_method("belozyortseva_menu"),
            "gavrikov": self._get_keyboard_method("gavrikov_menu"),
            "zabegaev": self._get_keyboard_method("zabegaev_menu"),
            "zargaryan": self._get_keyboard_method("zargaryan_menu"),
            "mendubaev": self._get_keyboard_method("mendubaev_menu"),
            "nurhametova": self._get_keyboard_method("nurhametova_menu"),
            "sadriev": self._get_keyboard_method("sadriev_menu"),
            "horoshutina": self._get_keyboard_method("horoshutina_menu"),
            "gilmanova": self._get_keyboard_method("gilmanova_menu"),
            "ending": self._get_keyboard_method("gilmanova_menu"),
        }
        
        keyboard_method = keyboard_mapping.get(speaker_name)
        if keyboard_method:
            try:
                return await keyboard_method()
            except Exception as e:
                print(f"Ошибка получения клавиатуры для {speaker_name}: {e}")
                return None
        
        return None

    def _get_keyboard_method(self, method_name: str):
        """Получает метод клавиатуры по имени"""
        keyboards = Keyboards()
        return getattr(keyboards.interactives, method_name, None) 