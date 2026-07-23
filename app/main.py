import asyncio
import logging

from aiogram import Bot, Dispatcher

from app.config import get_settings
from app.handlers.start import router as start_router


async def main() -> None:
    """
    Главная асинхронная функция приложения.
    """

    settings = get_settings()

    bot = Bot(
        token=settings.bot_token.get_secret_value(),
    )

    dispatcher = Dispatcher()

    dispatcher.include_router(start_router)

    logging.info("60DRBot запущен")

    await dispatcher.start_polling(
        bot,
        allowed_updates=dispatcher.resolve_used_update_types(),
    )


if __name__ == "__main__":
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
    )

    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        logging.info("60DRBot остановлен")