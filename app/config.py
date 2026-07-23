from functools import lru_cache

from pydantic import SecretStr
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """
    Настройки приложения.

    Значения загружаются из переменных окружения
    и файла .env в корне проекта.
    """

    # Telegram
    bot_token: SecretStr
    bot_proxy_url: str | None = None

    # PostgreSQL
    database_url: SecretStr

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=False,
        extra="ignore",
    )


@lru_cache
def get_settings() -> Settings:
    """
    Возвращает единый объект настроек приложения.

    Благодаря lru_cache файл .env читается только
    при первом вызове функции.
    """

    return Settings()