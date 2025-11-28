# Тестирование проекта Hotel Management System

## Обзор

В проект добавлены комплексные юнит-тесты для всех 71 класса системы управления отелем.

## Статистика тестирования

- **Всего тестов**: 1251
- **Успешных тестов**: 1251 (100%)
- **Покрытие кода**: 99%
- **Тестовый фреймворк**: pytest 7.4.3

## Структура тестов

```
tests/
├── __init__.py
├── conftest.py                    # Конфигурация pytest
├── core/                          # Тесты для core модуля (11 классов)
│   ├── test_base_model.py
│   ├── test_cache_manager.py
│   ├── test_config.py
│   ├── test_config_exception.py
│   ├── test_database_manager.py
│   ├── test_hotel_exception.py
│   ├── test_logger.py
│   ├── test_notifier.py
│   ├── test_security_manager.py
│   ├── test_task_scheduler.py
│   └── test_validator.py
│
├── booking_management/            # Тесты для booking_management (12 классов)
│   ├── test_booking.py
│   ├── test_cancellation.py
│   ├── test_checkin.py
│   ├── test_checkout.py
│   ├── test_discount.py
│   ├── test_discount_exception.py
│   ├── test_invoice.py
│   ├── test_invoice_exception.py
│   ├── test_payment.py
│   ├── test_rate_plan.py
│   ├── test_reservation.py
│   └── test_season.py
│
├── hotel_entities/                # Тесты для hotel_entities (10 классов)
│   ├── test_amenity.py
│   ├── test_building.py
│   ├── test_equipment.py
│   ├── test_facility.py
│   ├── test_floor.py
│   ├── test_hotel.py
│   ├── test_inventoryitem.py
│   ├── test_location.py
│   ├── test_room.py
│   └── test_roomtype.py
│
├── user_management/               # Тесты для user_management (10 классов)
│   ├── test_admin.py
│   ├── test_attendance.py
│   ├── test_department.py
│   ├── test_employee.py
│   ├── test_guest.py
│   ├── test_permission.py
│   ├── test_profile.py
│   ├── test_role.py
│   ├── test_shift.py
│   └── test_user.py
│
├── services/                      # Тесты для services (10 классов)
│   ├── test_conferenceroom.py
│   ├── test_event.py
│   ├── test_housekeeping.py
│   ├── test_maintenance.py
│   ├── test_menu.py
│   ├── test_order.py
│   ├── test_restaurant.py
│   ├── test_spa.py
│   ├── test_transportation.py
│   └── test_treatment.py
│
└── reports_analytics/             # Тесты для reports_analytics (18 классов)
    ├── test_analytics.py
    ├── test_analyticsexception.py
    ├── test_dashboard.py
    ├── test_employeereport.py
    ├── test_employeereportexception.py
    ├── test_financereportexception.py
    ├── test_financialreport.py
    ├── test_forecast.py
    ├── test_guestreport.py
    ├── test_guestreportexception.py
    ├── test_inventoryreport.py
    ├── test_inventoryreportexception.py
    ├── test_occupancyreport.py
    ├── test_occupancyreportexception.py
    ├── test_revenuereport.py
    ├── test_revenuereportexception.py
    ├── test_servicereport.py
    └── test_servicereportexception.py
```

## Установка и настройка

### 1. Создание виртуального окружения

```bash
python3 -m venv venv
```

### 2. Активация виртуального окружения

**Linux/Mac:**
```bash
source venv/bin/activate
```

**Windows:**
```bash
venv\Scripts\activate
```

### 3. Установка зависимостей

```bash
pip install -r requirements-test.txt
```

Устанавливаются следующие пакеты:
- pytest==7.4.3
- pytest-cov==4.1.0
- pytest-mock==3.12.0

## Запуск тестов

### Запустить все тесты

```bash
./venv/bin/pytest tests/
```

### Запустить тесты с подробным выводом

```bash
./venv/bin/pytest tests/ -v
```

### Запустить тесты с покрытием кода

```bash
./venv/bin/pytest tests/ --cov=. --cov-report=html --cov-report=term
```

После выполнения откройте `htmlcov/index.html` в браузере для просмотра детального отчета о покрытии.

### Запустить тесты конкретного модуля

```bash
./venv/bin/pytest tests/core/
./venv/bin/pytest tests/booking_management/
./venv/bin/pytest tests/hotel_entities/
./venv/bin/pytest tests/user_management/
./venv/bin/pytest tests/services/
./venv/bin/pytest tests/reports_analytics/
```

### Запустить конкретный тестовый файл

```bash
./venv/bin/pytest tests/core/test_logger.py
```

### Запустить конкретный тест

```bash
./venv/bin/pytest tests/core/test_logger.py::TestLogger::test_log_enabled
```

## Покрытие кода по модулям

| Модуль | Классов | Тестов | Покрытие |
|--------|---------|--------|----------|
| core | 11 | ~130 | 100% |
| booking_management | 12 | ~120 | 100% |
| hotel_entities | 10 | ~270 | 99% |
| user_management | 10 | ~260 | 100% |
| services | 10 | ~250 | 100% |
| reports_analytics | 18 | ~220 | 100% |
| **ИТОГО** | **71** | **1251** | **99%** |

## Что покрывают тесты

Каждый тест-файл включает проверки для:

1. **Инициализация классов** - проверка корректного создания объектов
2. **Все методы** - тестирование всех публичных методов
3. **Граничные случаи** - пустые строки, нулевые значения, отрицательные числа
4. **Обработка ошибок** - проверка ValueError для некорректных входных данных
5. **Валидация типов** - проверка типов параметров
6. **Изменение состояния** - тестирование взаимодействия методов
7. **Бизнес-логика** - проверка специфичных правил (скидки, расчеты, сортировка)

## Конфигурация pytest

Файл `pytest.ini` содержит настройки для pytest:

```ini
[pytest]
testpaths = tests
python_files = test_*.py
python_classes = Test*
python_functions = test_*
addopts =
    -v
    --strict-markers
    --tb=short
    --cov=.
    --cov-report=html
    --cov-report=term-missing
markers =
    unit: Unit tests
    integration: Integration tests
    slow: Slow running tests
```

## Примеры использования маркеров

```bash
# Запустить только юнит-тесты
pytest -m unit

# Запустить все кроме медленных тестов
pytest -m "not slow"
```

## Continuous Integration

Тесты готовы для интеграции в CI/CD пайплайны (GitHub Actions, GitLab CI, Jenkins и т.д.).

Пример для GitHub Actions:

```yaml
name: Tests
on: [push, pull_request]
jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - uses: actions/setup-python@v2
        with:
          python-version: '3.12'
      - run: pip install -r requirements-test.txt
      - run: pytest tests/ --cov=. --cov-report=xml
      - uses: codecov/codecov-action@v2
```

## Поддержка

Для вопросов и предложений по улучшению тестов обращайтесь к команде разработки.
