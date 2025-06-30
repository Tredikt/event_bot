'''Создание класса для управления базой данных'''
from sqlalchemy.ext.asyncio import AsyncSession

from core.repositories import (
    UserRepository,
    InteractiveHistoryRepository,
    FeedbackRepository
)
from core.services import InteractiveService


class DBClass:
    '''
    Этот класс предназначен для соединения всех репозиториев и управления базой данных из одного места
    '''

    def __init__(self, session: AsyncSession):
        self.user = UserRepository(session=session)
        self.feedback = FeedbackRepository(session=session)
        self.interactive_history = InteractiveHistoryRepository(session=session)
        self.question = QuestionRepository(session=session)

        self.interactive_service = InteractiveService(db=self)
