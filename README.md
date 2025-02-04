# Тестовое задание на вакансию  на позицию разработчика в

Описание

Этот проект предназначен для автоматизированного тестирования веб-сайта SBIS с использованием Selenium и Pytest. Включает три тестовых сценария, проверяющих функциональность скачивания плагина и другие важные аспекты сайта.

## Установка и настройка

### 1. Клонирование репозитория

```sh
git clone git@github.com:NikitinEgor2119/tensor_test.git
cd tensor_test
```

### 2. Создание и активация виртуального окружения

```sh
python -m venv venv
# Для Windows
venv\Scripts\activate
# Для macOS/Linux
source venv/bin/activate
```

### 3. Установка зависимостей

```sh
pip install -r requirements.txt
```

### 4. Установка драйвера Chrome (если не установлен)

- Убедитесь, что у вас установлен Google Chrome.
- Скачайте [ChromeDriver](https://sites.google.com/chromium.org/driver/) версии, соответствующей вашему браузеру.
- Добавьте путь к `chromedriver` в переменную окружения `PATH`.

## Запуск тестов

### ВНИМАНИЕ!

## Перед запуском второго сценария:

В файле test_second.py

```initial_region = contacts_page.get_current_region()
assert "Вологодская" in initial_region, f"Ожидали 'Вологодская', получили '{initial_region}'"
Заменить область "Вологодская" на вашу область в "Пример"
```

### Запуск всех тестов

```sh
pytest tests/ -v
```

### Запуск тестов через `main.py`

```sh
python main.py
```

### Запуск конкретного теста

```sh
pytest tests/test_third.py -v
```

## Настройки `pytest`

Файл `pytest.ini` содержит конфигурацию для удобного запуска тестов.

Пример содержимого:

```ini
[pytest]
addopts = -v --tb=short
python_files = test_*.py
python_classes = Test*
python_functions = test_*
```

## Дополнительно

- Убедитесь, что браузер не блокирует загрузку файлов.
- В случае проблем с `webdriver` попробуйте обновить его.
- Логи тестов можно просмотреть в терминале после выполнения команд.

## Пожелания

Буду ждать от вас обратной информации)

