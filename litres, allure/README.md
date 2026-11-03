# Litres UI tests (pytest + Playwright + Allure)

## Установка

```bash
python -m venv .venv
.venv\Scripts\activate          # Windows
source .venv/bin/activate       # macOS / Linux
pip install -r requirements.txt
playwright install chromium
```

Allure CLI устанавливается отдельно (нужен Java 8+):

- macOS: `brew install allure`
- Windows (Scoop): `scoop install allure`
- Linux / вручную: архив Allure 2 с https://github.com/allure-framework/allure2/releases, папку `bin` в `PATH`

Проверка: `allure --version` (ожидается 2.x)

## Запуск тестов

Все тесты с сохранением результатов Allure:

```bash
python -m pytest
```

Отдельный файл / тест:

```bash
python -m pytest tests/test_cart.py -v
python -m pytest tests/test_cart.py::test_delete_one_book_from_cart -v
```

Только smoke:

```bash
python -m pytest -m "smoke"
```

## Allure

Результаты складываются в `allure-results` (см. `pytest.ini`).

**Просмотр отчёта (временный сервер):**

```bash
allure serve allure-results
```

**Генерация статического отчёта:**

```bash
allure generate allure-results -o allure-report --clean
allure open allure-report
```

Готовый отчёт для сдачи — папка `allure-report/` (заархивировать целиком).

## Структура проекта

```
tests/              тесты
pages/              Page Object
components/         переиспользуемые компоненты (BookCard)
data.py             тестовые данные (BOOKS)
conftest.py         фикстуры
pytest.ini          конфиг pytest + Allure
allure-results/     сырые результаты (в .gitignore)
allure-report/      готовый отчёт (в .gitignore, сдаётся архивом)
```