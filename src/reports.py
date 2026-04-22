from collections import defaultdict
from datetime import datetime
from typing import Dict, List

from manager import FinanceManager
from models import Transaction, TransactionType


class ReportGenerator:
    def __init__(self, manager: FinanceManager):
        self.manager = manager

    def generate_summary(self) -> str:
        income_total = self.manager.get_income_total()
        expense_total = self.manager.get_expense_total()
        balance = self.manager.get_balance()

        return (
            f"ФИНАНСОВЫЙ ОТЧЁТ\n"
            f"Доходы: {income_total:.2f}\n"
            f"Расходы: {expense_total:.2f}\n"
            f"Баланс: {balance:.2f}\n"
        )

    def generate_period_report(self, start_date: datetime, end_date: datetime) -> str:
        transactions = self.manager.get_transactions_by_period(start_date, end_date)
        income_total = sum(
            t.amount for t in transactions if t.transaction_type == TransactionType.INCOME
        )
        expense_total = sum(
            t.amount for t in transactions if t.transaction_type == TransactionType.EXPENSE
        )

        lines = [
            f"ОТЧЁТ ЗА ПЕРИОД {start_date.date()} — {end_date.date()}",
            f"Доходы: {income_total:.2f}",
            f"Расходы: {expense_total:.2f}",
            f"Баланс: {(income_total - expense_total):.2f}",
            "",
            "Операции:"
        ]

        for t in sorted(transactions, key=lambda x: x.date):
            lines.append(
                f"{t.date.strftime('%Y-%m-%d %H:%M')} | "
                f"{t.transaction_type.value.upper()} | "
                f"{t.category.name} | {t.amount:.2f} | {t.description}"
            )

        return "\n".join(lines)

    def generate_category_report(self) -> str:
        expenses = self.manager.get_transactions_by_type(TransactionType.EXPENSE)
        category_totals: Dict[str, float] = defaultdict(float)

        for expense in expenses:
            category_totals[expense.category.name] += expense.amount

        lines = ["ОТЧЁТ ПО КАТЕГОРИЯМ"]
        for category, total in sorted(category_totals.items(), key=lambda x: x[1], reverse=True):
            lines.append(f"{category}: {total:.2f}")

        return "\n".join(lines)
