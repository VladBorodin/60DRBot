@echo off
setlocal

chcp 65001 >nul
cd /d "%~dp0"

echo ========================================
echo      Установка зависимостей 60DRBot
echo ========================================
echo.

if not exist "requirements.txt" (
    echo [ОШИБКА] Не найден файл requirements.txt
    echo Скрипт должен находиться в корне проекта.
    pause
    exit /b 1
)

set "PYTHON_COMMAND=py"

%PYTHON_COMMAND% --version >nul 2>&1

if errorlevel 1 (
    set "PYTHON_COMMAND=python"
)

%PYTHON_COMMAND% --version >nul 2>&1

if errorlevel 1 (
    echo [ОШИБКА] Python не найден.
    echo Установите Python и добавьте его в PATH.
    pause
    exit /b 1
)

echo [1/3] Проверка виртуального окружения...

if not exist ".venv\Scripts\python.exe" (
    echo Виртуальное окружение не найдено.
    echo Создание .venv...

    %PYTHON_COMMAND% -m venv .venv

    if errorlevel 1 (
        echo [ОШИБКА] Не удалось создать виртуальное окружение.
        pause
        exit /b 1
    )
) else (
    echo Виртуальное окружение уже существует.
)

echo.
echo [2/3] Обновление pip...

".venv\Scripts\python.exe" -m pip install --upgrade pip

if errorlevel 1 (
    echo [ОШИБКА] Не удалось обновить pip.
    pause
    exit /b 1
)

echo.
echo [3/3] Установка зависимостей...

".venv\Scripts\python.exe" -m pip install -r requirements.txt

if errorlevel 1 (
    echo [ОШИБКА] Не удалось установить зависимости.
    pause
    exit /b 1
)

echo.
echo ========================================
echo     Установка успешно завершена
echo ========================================
echo.
echo Теперь можно запустить start.bat.
echo.

pause
exit /b 0