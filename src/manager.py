from datetime import datetime
from typing import List, Optional

from models import Category, Expense, Income, Transaction, TransactionType


class FinanceManager:
    def __init__(self):
        self.transactions: List[Transaction] = []

    def add_income(
        self,
        amount: float,
        category_name: str,
        description: str = "",
        date: Optional[datetime] = None
    ) -> Income:
        category = Category(category_name)
        income = Income(
            amount=amount,
            category=category,
            description=description,
            date=date or datetime.now()
        )
        self.transactions.append(income)
        return income

    def add_expense(
        self,
        amount: float,
        category_name: str,
        description: str = "",
        date: Optional[datetime] = None
    ) -> Expense:
        category = Category(category_name)
        expense = Expense(
            amount=amount,
            category=category,
            description=description,
            date=date or datetime.now()
        )
        self.transactions.append(expense)
        return expense

    def get_all_transactions(self) -> List[Transaction]:
        return sorted(self.transactions, key=lambda t: t.date)

    def get_transactions_by_type(self, transaction_type: TransactionType) -> List[Transaction]:
        return [
            t for t in self.transactions
            if t.transaction_type == transaction_type
        ]

    def get_transactions_by_category(self, category_name: str) -> List[Transaction]:
        return [
            t for t in self.transactions
            if t.category.name.lower() == category_name.lower()
        ]

    def get_income_total(self) -> float:
        return sum(t.amount for t in self.get_transactions_by_type(TransactionType.INCOME))

    def get_expense_total(self) -> float:
        return sum(t.amount for t in self.get_transactions_by_type(TransactionType.EXPENSE))

    def get_balance(self) -> float:
        return self.get_income_total() - self.get_expense_total()

    def get_transactions_by_period(self, start_date: datetime, end_date: datetime) -> List[Transaction]:
        return [
            t for t in self.transactions
            if start_date <= t.date <= end_date
        ]
