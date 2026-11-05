# AQA Docker Project

Учебный проект для демонстрации запуска автотестов (API, Smoke, UI) в Docker и Docker Compose.

## Требования
- Python 3.12+ (для локального запуска)
- Docker Desktop (для запуска в контейнерах)
- Allure CLI (опционально, для просмотра отчётов)

## Структура проекта
- mock_api/server.py — локальный mock API
- tests/test_smoke.py — быстрые smoke-тесты
- tests/test_health.py — API-тесты
- tests/test_ui.py — UI-тесты на Playwright
- Dockerfile — сборка образа для API/Smoke тестов
- Dockerfile.ui — сборка образа для UI-тестов (Playwright)
- compose.yaml — запуск API и тестов вместе
- requirements.txt — зафиксированные зависимости

## Локальный запуск (без Docker)

Активируйте виртуальное окружение и установите зависимости:
python -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt

1. Локальный smoke:
python -m pytest -m smoke -q

2. Локальный mock API и API-тест (в двух терминалах):
Терминал 1 (сервер):
python mock_api/server.py
Терминал 2 (тест):
python -m pytest -m api -q

## Сборка и запуск Docker

1. Сборка основного образа:
docker build -t aqa-tests:local .

2. Автономный Docker smoke:
docker run --rm aqa-tests:local

3. Сборка и запуск UI-тестов (Playwright):
New-Item -ItemType Directory -Force .\test-results
docker build -f Dockerfile.ui -t aqa-ui-tests:local .
docker run --rm --init --ipc=host `
  --mount "type=bind,src=$($PWD.Path)/test-results,dst=/app/test-results" `
  aqa-ui-tests:local

## Docker Compose

1. Проверка Compose:
docker compose config --quiet

2. Compose API-тест (по умолчанию):
docker compose up --build --abort-on-container-exit --exit-code-from tests

3. Выбор marker (например, smoke):
$env:PYTEST_MARKER="smoke"
docker compose up --build --abort-on-container-exit --exit-code-from tests
Remove-Item Env:PYTEST_MARKER

## Очистка
Остановить и удалить контейнеры, сети:
docker compose down --remove-orphans

## Просмотр Allure
После прогона API-тестов через Compose в папке allure-results появятся результаты.
allure serve allure-results

## Правила обновления
- Версия Python-образа: 3.12.14-slim-bookworm
- После обновления зависимостей (изменения requirements.txt) выполняются три прогона: локальный, Docker- и Compose.
- Полный requirements.txt создаётся в чистом виртуальном окружении командой python -m pip freeze > requirements.txt.
- Дата последней проверки: 2026-11-05