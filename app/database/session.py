from sqlalchemy import text
from sqlalchemy.ext.asyncio import (
    AsyncEngine,
    AsyncSession,
    async_sessionmaker,
    create_async_engine,
)

from app.config import get_settings


settings = get_settings()


engine: AsyncEngine = create_async_engine(
    url=settings.database_url.get_secret_value(),
    echo=False,
    pool_pre_ping=True,
)


async_session_factory = async_sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False,
)


async def check_database_connection() -> None:
    """
    Проверяет, что приложение может подключиться к PostgreSQL.

    Запрос SELECT 1 ничего не изменяет в базе,
    а только подтверждает работоспособность соединения.
    """

    async with engine.connect() as connection:
        await connection.execute(text("SELECT 1"))


async def dispose_database_engine() -> None:
    """
    Корректно закрывает соединения SQLAlchemy.
    """

    await engine.dispose()