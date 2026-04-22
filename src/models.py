from dataclasses import dataclass, field
from datetime import datetime
from enum import Enum


class TransactionType(Enum):
    INCOME = "income"
    EXPENSE = "expense"


@dataclass
class Category:
    name: str


@dataclass
class Transaction:
    amount: float
    category: Category
    description: str = ""
    date: datetime = field(default_factory=datetime.now)
    transaction_type: TransactionType = field(init=False)

    def __post_init__(self):
        if self.amount <= 0:
            raise ValueError("Сумма операции должна быть больше 0")


@dataclass
class Income(Transaction):
    def __post_init__(self):
        super().__post_init__()
        self.transaction_type = TransactionType.INCOME


@dataclass
class Expense(Transaction):
    def __post_init__(self):
        super().__post_init__()
        self.transaction_type = TransactionType.EXPENSE
