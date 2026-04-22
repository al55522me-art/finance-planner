# Personal Finance Planner

Консольное приложение на Python для учёта личных финансов.  
Проект позволяет добавлять доходы и расходы, распределять траты по категориям и формировать отчёты.

## Возможности

- Добавление доходов.
- Добавление расходов.
- Категоризация операций.
- Просмотр всех транзакций.
- Подсчёт баланса.
- Отчёт по категориям.
- Отчёт за выбранный период.

## Стек технологий

- Python 3.x
- ООП
- datetime
- dataclasses
- enum
- typing

## Структура проекта

```text
personal-finance-planner/
├── README.md
├── .gitignore
├── pyproject.toml
├── src/
│   └── finance_planner/
│       ├── __init__.py
│       ├── models.py
│       ├── manager.py
│       ├── reports.py
│       └── cli.py
└── tests/
    ├── test_models.py
    ├── test_manager.py
    └── test_reports.py
