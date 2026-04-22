from datetime import datetime

from manager import FinanceManager
from reports import ReportGenerator


def parse_date(date_str: str) -> datetime:
    return datetime.strptime(date_str, "%Y-%m-%d")


def show_menu():
    print("\n=== Личный финансовый планировщик ===")
    print("1. Добавить доход")
    print("2. Добавить расход")
    print("3. Показать все операции")
    print("4. Показать баланс")
    print("5. Отчёт по категориям")
    print("6. Отчёт за период")
    print("0. Выход")


def main():
    manager = FinanceManager()
    reports = ReportGenerator(manager)

    while True:
        show_menu()
        choice = input("Выберите пункт: ").strip()

        if choice == "1":
            amount = float(input("Сумма дохода: "))
            category = input("Категория: ")
            description = input("Описание: ")
            manager.add_income(amount, category, description)
            print("Доход добавлен.")

        elif choice == "2":
            amount = float(input("Сумма расхода: "))
            category = input("Категория: ")
            description = input("Описание: ")
            manager.add_expense(amount, category, description)
            print("Расход добавлен.")

        elif choice == "3":
            transactions = manager.get_all_transactions()
            if not transactions:
                print("Операций пока нет.")
            else:
                for t in transactions:
                    print(
                        f"{t.date.strftime('%Y-%m-%d %H:%M')} | "
                        f"{t.transaction_type.value.upper()} | "
                        f"{t.category.name} | {t.amount:.2f} | {t.description}"
                    )

        elif choice == "4":
            print(f"Баланс: {manager.get_balance():.2f}")

        elif choice == "5":
            print(reports.generate_category_report())

        elif choice == "6":
            start_date = parse_date(input("Дата начала (YYYY-MM-DD): "))
            end_date = parse_date(input("Дата конца (YYYY-MM-DD): "))
            print(reports.generate_period_report(start_date, end_date))

        elif choice == "0":
            print("Выход из программы.")
            break

        else:
            print("Неверный выбор. Попробуйте ещё раз.")


if __name__ == "__main__":
    main()
