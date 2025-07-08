'''Создание класса для управления базой данных'''
from sqlalchemy.ext.asyncio import AsyncSession

from core.repositories import (
    UserRepository,
    InteractiveHistoryRepository,
    FeedbackRepository,
    QuestionRepository,
    MessagesRepository,
)
from core.services.interactive_service import InteractiveService


class DBClass:
    '''
    Этот класс предназначен для соединения всех репозиториев и управления базой данных из одного места.
    После использования необходимо закрыть сессию: await db.session.close()
    '''

    def __init__(self, session: AsyncSession):
        self.session = session
        
        self.user = UserRepository(session=session)
        self.feedback = FeedbackRepository(session=session)
        self.interactive_history = InteractiveHistoryRepository(session=session)
        self.question = QuestionRepository(session=session)
        self.messages = MessagesRepository(session=session)

        self.interactive_service = InteractiveService(db=self)
