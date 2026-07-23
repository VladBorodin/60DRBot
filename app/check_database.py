import asyncio
import logging

from app.database.session import (
    check_database_connection,
    dispose_database_engine,
)


async def main() -> None:
    """
    Проверяет подключение приложения к PostgreSQL.
    """

    try:
        await check_database_connection()
        logging.info("Подключение к PostgreSQL успешно установлено")
    finally:
        await dispose_database_engine()


if __name__ == "__main__":
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
    )

    asyncio.run(main())