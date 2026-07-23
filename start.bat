@echo off
setlocal

chcp 65001 >nul
cd /d "%~dp0"

echo ========================================
echo             Запуск 60DRBot
echo ========================================
echo.

if not exist ".venv\Scripts\python.exe" (
    echo Виртуальное окружение не найдено.
    echo Сначала будет выполнен install.bat.
    echo.

    call install.bat

    if errorlevel 1 (
        echo.
        echo [ОШИБКА] Установка завершилась с ошибкой.
        pause
        exit /b 1
    )
)

if not exist ".env" (
    echo [ОШИБКА] Не найден файл .env
    echo.
    echo Создайте файл .env в корне проекта
    echo и добавьте в него:
    echo.
    echo BOT_TOKEN=ваш_токен
    echo.
    pause
    exit /b 1
)

echo Бот запускается...
echo Для остановки нажмите Ctrl+C.
echo.

".venv\Scripts\python.exe" -m app.main

set "EXIT_CODE=%ERRORLEVEL%"

echo.

if not "%EXIT_CODE%"=="0" (
    echo [ОШИБКА] Бот завершился с кодом %EXIT_CODE%.
) else (
    echo Бот остановлен.
)

echo.
pause
exit /b %EXIT_CODE%