from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message


router = Router(name="start")


@router.message(CommandStart())
async def handle_start_command(message: Message) -> None:
    """
    Обрабатывает команду /start.

    Пока бот только приветствует пользователя.
    На следующем этапе здесь начнётся регистрация сотрудника.
    """

    user = message.from_user

    if user is None:
        user_name = "коллега"
    else:
        user_name = user.full_name

    await message.answer(
        text=(
            f"Здравствуйте, {user_name}!\n\n"
            "Вы подключились к корпоративному боту 60DRBot.\n"
            "Позже здесь появится регистрация сотрудников "
            "и получение персональных рассылок."
        )
    )