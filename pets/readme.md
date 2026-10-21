# API-тесты Swagger Petstore (pytest + requests)

## 1. Назначение проекта

Автоматизированные тесты REST API сервиса управления питомцами (Swagger Petstore).
Проверяются: создание питомца, получение по ID, создание с заданным статусом,
обновление данных, обновление статуса, поиск по статусу, поиск созданного питомца
среди результатов поиска и обработка несуществующего питомца (404).

Тесты разделены маркерами на дымовой набор (smoke) и регрессионный (regression).

## 2. Используемый API и документация

API: Swagger Petstore (тестовое окружение).
База: https://petstore.swagger.io/v2

Документация:
- https://petstore.swagger.io/
- https://editor.swagger.io/?url=https://petstore.swagger.io/v2/swagger.json

Используемые эндпоинты:
- POST   /pet                    — создать питомца
- GET    /pet/{petId}            — получить питомца
- PUT    /pet                    — обновить питомца
- GET    /pet/findByStatus       — поиск по статусу
- DELETE /pet/{petId}            — удалить питомца

## 3. Версия Python

Python 3.10 или новее (проверялось на 3.10/3.11).

## 4. Виртуальное окружение и зависимости

Создание и активация:

    python -m venv venv
    source venv/bin/activate        # Linux / macOS

    venv\Scripts\activate           # Windows

Зависимости, файл requirements.txt:

    pytest>=7.4
    requests>=2.31

Установка:

    python -m pip install --upgrade pip
    pip install -r requirements.txt

Конфигурация, файл config.py (базовый URL и таймаут):

    BASE_URL = "https://petstore.swagger.io/v2"
    TIMEOUT = 10

Все запросы читают эти значения из config.py, менять URL в тестах не нужно.

## 5. Запуск всех тестов

Из корня проекта:

    pytest

С кратким отчётом по каждому тесту:

    pytest -v

## 6. Запуск только smoke и только regression

    pytest -m smoke
    pytest -m regression

Маркеры объявлены в pytest.ini:

    [pytest]
    markers =
        smoke: Дымовые тесты для критического функционала
        regression: Полный набор регрессионных тестов
        slow: Медленные тесты (например, с доступом к сети)

Отступы перед строками маркеров обязательны (4 пробела).

## 7. Запуск одного файла и одного теста

Один файл:

    pytest test_pet.py

Один тест:

    pytest test_pet.py::test_create_pet

Один параметризованный пример:

    pytest "test_pet.py::test_create_pet_with_status[available]"

## 8. Структура проекта

    .
    ├── config.py               # BASE_URL, TIMEOUT
    ├── conftest.py             # фикстуры: pet_client, pet_factory, created_pet
    ├── pytest.ini              # маркеры smoke / regression / slow
    ├── requirements.txt        # pytest, requests
    ├── test_pet.py             # тест-кейсы
    ├── clients/
    │   └── pet_clients.py      # HTTP-клиент на requests.Session
    ├── data/
    │   └── pet_factory.py      # генерация payload питомца
    ├── README.md
    └── .gitignore

Пакеты clients/ и data/ должны быть импортируемы:
from clients.pet_clients import PetClient
from data.pet_factory import create_data

## 9. Генерация и очистка данных

Генерация:
- Фабрика create_data() в data/pet_factory.py формирует словарь payload:
  id, name, photoUrls, status.
- Если id не передан — генерируется случайное число в диапазоне
  1234567890123..9999999999999, чтобы не перезаписывать чужие питомцы
  на общем публичном стенде.
- Если name не передан — генерируется уникальный суффикс вида Laich_xxxxxx
  (случайные латинские буквы и цифры).
- Если status не передан — выбирается случайный из available / pending / sold.
- Все значения передаются в API без лишних пробелов в ключах и значениях.

Очистка:
- Фикстура pet_factory накапливает ID всех созданных внутри теста питомцев
  в список pet_ids. После завершения теста (в том числе при падении.assert)
  блок после yield удаляет каждый из них через DELETE /pet/{id}.
- Фикстура created_pet создаёт одного питомца, передаёт тесту (pet_id, response)
  и после yield удаляет его.
- В test_get_nesuchestvuyuchiy_pet питомец удаляется внутри теста намеренно,
  чтобы проверить ответ 404; повторное удаление в teardown игнорируется
  как ожидаемое (404 не является ошибкой очистки).

Принцип: тест сам создаёт свои данные и сам их удаляет, зависимость от
предварительно заполненной базы отсутствует.

## 10. Область действия фикстур (scope)

- pet_client — function. Новый requests.Session на каждый тест,
  после теста session.close() освобождает соединения.
- pet_factory — function. Список созданных ID не утекает между тестами,
  очистка выполняется строго после своего теста.
- created_pet — function. Изолированный питомец для каждого теста,
  параллельные тесты не мешают друг другу.

Session/клиент можно было бы сделать session-scoped для скорости,
но выбран function: это гарантирует независимость тестов и предсказуемый
teardown, что важнее для небольшого набора сетевых тестов.

## 11. Результаты последнего запуска и известные проблемы

Фактический прогон в этом окружении не выполнялся, поэтому численные
результаты (passed/failed, время) здесь не выдумываются.
После запуска заполнить строку:

    pytest -v  ->  собрано: ___, passed: ___, failed: ___, время: ___

Ожидаемое распределение маркеров:
- smoke: test_create_pet, test_create_pet_with_status (3 примера),
         test_get_nesuchestvuyuchiy_pet
- regression: все перечисленные smoke-тесты плюс test_update_pet,
              test_update_status (3 примера), test_find_by_status (3 примера),
              test_find_by_status_created (3 примера)

