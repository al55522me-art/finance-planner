import pytest
from datetime import datetime

from src.models import Category, Income, Expense, TransactionType

def test_income_creation():
    category = Category("Salary")
    income = Income(50000, category, "Monthly salary", datetime(2026, 4, 1))

    assert income.amount == 50000
    assert income.category.name == "Salary"
    assert income.transaction_type == TransactionType.INCOME


def test_expense_creation():
    category = Category("Food")
    expense = Expense(1500, category, "Lunch", datetime(2026, 4, 2))

    assert expense.amount == 1500
    assert expense.category.name == "Food"
    assert expense.transaction_type == TransactionType.EXPENSE


def test_negative_amount_raises():
    category = Category("Test")

    with pytest.raises(ValueError):
        Income(-100, category)
