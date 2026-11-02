## Diplom_1 — тесты модели бургера

Проект содержит модель бургера и unit-тесты классов `Bun`, `Burger`, `Ingredient` и `Database`.

### Установка

```text
python -m venv .venv
```

В Windows активируйте окружение командой `.\.venv\Scripts\Activate.ps1`, затем установите зависимости:

```text
pip install -r requirements.txt
```

### Запуск тестов

```text
pytest
```

### Отчет о покрытии

```text
pytest --cov=bun --cov=burger --cov=ingredient --cov=database --cov-report=term-missing --cov-report=html --cov-report=xml
```

Табличный отчет выводится в терминал, HTML-отчет создается в `htmlcov/index.html`, XML-отчет — в `coverage.xml`. Сводка последнего полного прогона сохранена в `coverage_report.txt`.
