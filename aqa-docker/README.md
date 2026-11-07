# AQA Docker Project (pytest + Playwright + Allure + Jenkins)

Проект содержит автотесты (Smoke, API, Regression, UI) и локальный mock API, упакованные в Docker и настроенные для запуска в CI/CD (Jenkins).

## 📋 Требования к агенту Jenkins
*   **ОС:** Linux-агент.
*   **Git:** Установлен и доступен в `$PATH`.
*   **Docker:** Установлен Docker Engine (v20.10+) и Docker Compose v2.
*   **Права:** Пользователь, под которым работает Jenkins, должен иметь доступ к Docker (добавлен в группу `docker` или запущен от `root`).
*   *Примечание:* В текущей учебной конфигурации используется паттерн **Docker-in-Docker (DinD)**. Контейнер Jenkins запущен с флагами `-u root` и `-v /var/run/docker.sock:/var/run/docker.sock`, а внутри установлен Docker CLI.

## 🧩 Плагины Jenkins
**Обязательные:**
*   **Pipeline** (Declarative Pipeline).
*   **Git** (для работы с SCM).
*   **Allure Jenkins Plugin** (для построения HTML-отчетов).

**Опциональные:**
*   **Credentials Binding** (для безопасной передачи токенов).
*   **NodeJS** (не требуется, так как мы используем локальную установку Allure 2.x на Java).

## ⚙️ Параметры Job
В пайплайне настроен параметр `TEST_SET` со следующими значениями:
*   `smoke` — быстрые тесты без зависимостей.
*   `api` — тесты API (требуют поднятия `mock_api`).
*   `regression` — регрессионные проверки.
*   `ui` — UI-тесты на Playwright (запускаются в браузере Chromium).

## 🐳 Локальные команды (Docker Compose)

**1. Проверка конфигурации:**
```bash
docker compose config --quiet
