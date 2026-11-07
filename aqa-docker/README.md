# AQA Docker Project (pytest + Playwright + Allure + Jenkins)

Проект содержит автотесты (Smoke, API, Regression, UI) и локальный mock API, упакованные в Docker и настроенные для запуска в CI/CD (Jenkins).

## 📋 Требования к Jenkins-агенту
- ОС: Linux (или Windows с WSL2).
- Git: Установлен и доступен в `$PATH`.
- Docker: Установлен Docker Engine (v20.10+) и Docker Compose v2.
- Права: Пользователь Jenkins должен иметь доступ к Docker (запущен от `root` или добавлен в группу `docker`).
- Текущая конфигурация: Используется паттерн Docker-in-Docker (DinD). Jenkins запущен в контейнере с флагами `-u root` и `-v /var/run/docker.sock:/var/run/docker.sock`, внутри установлен Docker CLI и Allure CLI (Java).

## 🧩 Плагины Jenkins
Обязательные:
- Pipeline (Declarative Pipeline).
- Git (для работы с SCM).
- Allure Jenkins Plugin (для построения HTML-отчетов).

Опциональные:
- Credentials Binding (используется для безопасной передачи токена `aqa-api-token`).

## ⚙️ Параметры Job
В пайплайне настроен параметр `TEST_SET` со следующими значениями:
- `smoke` — быстрые тесты без зависимостей.
- `api` — тесты API (требуют поднятия `mock_api`).
- `regression` — регрессионные проверки.
- `ui` — UI-тесты на Playwright (запускаются в браузере Chromium).

## 🐳 Локальные команды (Docker)

1. Проверка конфигурации Compose:
docker compose config --quiet

2. Сборка образа:
docker build -t aqa-tests:local .

3. Автономный Docker smoke:
docker run --rm aqa-tests:local

4. Compose API-тест (Linux/macOS):
PYTEST_MARKER=api docker compose up --build --abort-on-container-exit --exit-code-from tests
(Для Windows PowerShell: `$env:PYTEST_MARKER="api"; docker compose up --build --abort-on-container-exit --exit-code-from tests`)

5. Выбор marker (пример для UI):
$env:PYTEST_MARKER="ui"
docker compose up --build --abort-on-container-exit --exit-code-from tests
Remove-Item Env:PYTEST_MARKER

6. Очистка:
docker compose down --remove-orphans

## 🛠️ Локальные команды (без Docker)

1. Локальный smoke:
python -m pytest -m smoke -q

2. Локальный Mock API и API-тест (в двух терминалах):
Терминал 1 (сервер): python mock_api/server.py
Терминал 2 (тест): python -m pytest -m api -q

3. Просмотр Allure (локально):
allure serve allure-results/ui

## 🔑 Значение COMPOSE_PROJECT_NAME
В пайплайне генерируется переменная окружения:
COMPOSE_PROJECT_NAME = "aqa-${JOB_BASE_NAME}-${BUILD_NUMBER}"

Назначение: Предотвращает конфликты между параллельными сборками. Все контейнеры, сети и образы текущего билда получают уникальный префикс (например, `aqa-aqa-docker-pipeline-30-api-1`), поэтому сборки разных джоб не мешают друг другу.

## 📂 Пути к артефактам
- Сырые результаты Allure: `/app/allure-results/ui` (внутри контейнера) -> копируются в Jenkins через `docker cp`.
- Скриншоты и трейсы Playwright: `/app/test-results/` (внутри контейнера) -> сохраняются как артефакты сборки.
- Готовый HTML-отчет: Генерируется автоматически и доступен во вкладке Allure Report в интерфейсе Jenkins.

## 🔐 Правила Credentials
- Секреты (токены, пароли) никогда не хранятся в Git.
- Используется Jenkins Credentials типа Secret text с ID `aqa-api-token`.
- Секрет объявляется строго внутри конкретного stage (через `withCredentials`), чтобы ограничить область его видимости.
- Значение передается в Docker-контейнер через переменные окружения (в `compose.yaml` указано `API_TOKEN: ${API_TOKEN}`).

## 🚑 Порядок диагностики падения
1. Откройте Console Output сборки.
2. Найдите первый красный stage (Checkout, Prepare, Validate, Tests).
3. Прочитайте первую содержательную ошибку (например, `docker: command not found` или `AssertionError`).
4. Проверьте значение параметра `TEST_SET`.
5. Скачайте артефакты (скриншоты) и откройте Allure Report.
6. Выполните локально ту же команду, чтобы воспроизвести падение.
7. Разделите проблему: инфраструктура (Docker), код теста или реальный баг.

## 🧹 Правила Cleanup
- Блок `post { cleanup { ... } }` выполняется всегда, даже если тесты упали.
- Используется команда `docker compose down --remove-orphans --rmi local || true`.
- Флаг `--rmi local` удаляет образы, созданные текущей сборкой.
- Конструкция `|| true` нужна, чтобы ошибка очистки (например, если контейнер уже удален) не ломала статус сборки.
- Никогда не используйте флаг `-v` в `down` без понимания состава volume'ов, чтобы случайно не удалить нужные данные.
