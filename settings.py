import os
from pathlib import Path

from dotenv import load_dotenv
from pydantic_settings import BaseSettings

# Путь к корню проекта
BASE_DIR = Path(__file__).parent

# Загружаем .env файл только если он существует (для локальной разработки)
env_path = BASE_DIR / ".env"
if env_path.exists():
    print(f"Loading .env from: {env_path}")
    load_dotenv(env_path)
else:
    print("No .env file found, using environment variables from system")


class Config(BaseSettings):
    TG_TOKEN: str
    
    DB_HOST: str = "localhost"
    DB_PORT: str = "5432"
    DB_PASSWORD: str = "password"
    DB_USER: str = "user"
    DB_NAME: str = "event_bot"

    ADMINS: str

    @property
    def DB_URL(self) -> str:
        return (
            f"postgresql+asyncpg://"
            f"{self.DB_USER}:{self.DB_PASSWORD}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"
        )

    class Config:
        # Не указываем env_file для продакшена - используем системные переменные окружения
        case_sensitive = True


config = Config()
print(f"Loaded config - DB_HOST: {config.DB_HOST}, ADMINS count: {len(config.ADMINS.split(','))}")
