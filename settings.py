from pathlib import Path

from dotenv import load_dotenv
from pydantic_settings import BaseSettings

# Подгружаем .env файл в переменные окружения, без этого не работает Pydantic-Settings
load_dotenv()

# Путь к корню проекта
BASE_DIR = Path(__file__).parent.parent


class Config(BaseSettings):
    TG_TOKEN: str
    
    DB_HOST: str
    DB_PORT: str
    DB_PASSWORD: str
    DB_USER: str
    DB_NAME: str

    ADMINS: str
    ADMINS_USERNAMES: str


    class ConfigDict:
        env: Path = BASE_DIR / ".env"


config = Config()
DB_URL: str = (
     # "postgresql+asyncpg://"
     # f"{config.DB_USER}:{config.DB_PASSWORD}@{config.DB_HOST}:{config.DB_PORT}/{config.DB_NAME}"
     "sqlite+aiosqlite:///event_bot.db"
)
