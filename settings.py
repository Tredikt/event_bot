from pathlib import Path

from dotenv import load_dotenv
from pydantic_settings import BaseSettings

# Подгружаем .env файл в переменные окружения, без этого не работает Pydantic-Settings
load_dotenv()

# Путь к корню проекта
BASE_DIR = Path(__file__).parent.parent


class Config(BaseSettings):
    TG_TOKEN: str
    
    DB_HOST: str = "localhost"
    DB_PORT: str = "5433"
    DB_PASSWORD: str = "password"
    DB_USER: str = "user"
    DB_NAME: str = "event_bot"

    DB_URL: str = (
        f"postgresql+asyncpg://"
        f"{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
    )

    ADMINS: str

    class ConfigDict:
        env: Path = BASE_DIR / ".env"


config = Config()
