'''Создание класса для управления базой данных'''
from sqlalchemy.ext.asyncio import AsyncSession


class DBClass:
    '''
    Этот класс предназначен для соединения всех репозиториев и управления базой данных из одного места
    '''

    def __init__(self, session: AsyncSession):
        pass
