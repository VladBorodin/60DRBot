from functools import lru_cache

from pydantic import SecretStr
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """
    Настройки приложения.

    Значения загружаются из переменных окружения
    и из файла .env в корне проекта.
    """

    bot_token: SecretStr

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=False,
        extra="ignore",
    )


@lru_cache
def get_settings() -> Settings:
    """
    Создаёт объект настроек один раз и затем
    возвращает уже созданный экземпляр.
    """

    return Settings()