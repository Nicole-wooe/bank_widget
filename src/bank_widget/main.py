import json
from pathlib import Path
from typing import Any

import pandas as pd

from bank_widget.operations import process_bank_search

VALID_STATUSES = {"EXECUTED", "CANCELED", "PENDING"}


def read_json_file(file_path: str) -> list[dict[str, Any]]:
    """Read transactions from JSON file."""
    with open(file_path, encoding="utf-8") as file:
        return json.load(file)


def read_csv_file(file_path: str) -> list[dict[str, Any]]:
    """Read transactions from CSV file."""
    return pd.read_csv(file_path, sep=";").to_dict(orient="records")


def read_excel_file(file_path: str) -> list[dict[str, Any]]:
    """Read transactions from Excel file."""
    return pd.read_excel(file_path).to_dict(orient="records")


def filter_by_status(transactions: list[dict[str, Any]], status: str) -> list[dict[str, Any]]:
    """Filter transactions by status."""
    return [
        transaction
        for transaction in transactions
        if str(transaction.get("state", "")).upper() == status
    ]


def sort_transactions_by_date(
    transactions: list[dict[str, Any]],
    reverse: bool,
) -> list[dict[str, Any]]:
    """Sort transactions by date."""
    return sorted(
        transactions,
        key=lambda transaction: str(transaction.get("date", "")),
        reverse=reverse,
    )


def filter_rub_transactions(transactions: list[dict[str, Any]]) -> list[dict[str, Any]]:
    """Filter transactions by RUB currency."""
    return [
        transaction
        for transaction in transactions
        if get_currency_code(transaction) == "RUB"
    ]


def get_currency_code(transaction: dict[str, Any]) -> str:
    """Return transaction currency code."""
    operation_amount = transaction.get("operationAmount")

    if isinstance(operation_amount, dict):
        currency = operation_amount.get("currency", {})
        if isinstance(currency, dict):
            return str(currency.get("code", "")).upper()

    return str(transaction.get("currency_code", "")).upper()


def get_amount(transaction: dict[str, Any]) -> str:
    """Return transaction amount."""
    operation_amount = transaction.get("operationAmount")

    if isinstance(operation_amount, dict):
        return str(operation_amount.get("amount", ""))

    return str(transaction.get("amount", ""))


def get_description(transaction: dict[str, Any]) -> str:
    """Return transaction description."""
    return str(transaction.get("description", ""))


def print_transactions(transactions: list[dict[str, Any]]) -> None:
    """Print transactions to console."""
    print("Распечатываю итоговый список транзакций...")

    if not transactions:
        print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации")
        return

    print(f"Всего банковских операций в выборке: {len(transactions)}")

    for transaction in transactions:
        print()
        print(f"{transaction.get('date', '')} {get_description(transaction)}")
        print(f"Сумма: {get_amount(transaction)} {get_currency_code(transaction)}")


def get_transactions_by_user_choice() -> list[dict[str, Any]]:
    """Return transactions from selected file type."""
    print(
        "Привет! Добро пожаловать в программу работы с банковскими транзакциями.\n"
        "Выберите необходимый пункт меню:\n"
        "1. Получить информацию о транзакциях из JSON-файла\n"
        "2. Получить информацию о транзакциях из CSV-файла\n"
        "3. Получить информацию о транзакциях из XLSX-файла"
    )

    user_choice = input("Пользователь: ")

    if user_choice == "1":
        print("Для обработки выбран JSON-файл.")
        return read_json_file("data/operations.json")

    if user_choice == "2":
        print("Для обработки выбран CSV-файл.")
        return read_csv_file("data/transactions.csv")

    if user_choice == "3":
        print("Для обработки выбран XLSX-файл.")
        return read_excel_file("data/transactions_excel.xlsx")

    print("Выбран неверный пункт меню.")
    return []


def get_status_from_user() -> str:
    """Return correct transaction status from user input."""
    while True:
        status = input(
            "Введите статус, по которому необходимо выполнить фильтрацию.\n"
            "Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING\n"
            "Пользователь: "
        ).upper()

        if status in VALID_STATUSES:
            print(f'Операции отфильтрованы по статусу "{status}"')
            return status

        print(f'Статус операции "{status}" недоступен.')


def main() -> None:
    """Run main program logic."""
    transactions = get_transactions_by_user_choice()

    if not transactions:
        print_transactions([])
        return

    status = get_status_from_user()
    transactions = filter_by_status(transactions, status)

    sort_answer = input("Отсортировать операции по дате? Да/Нет\nПользователь: ").lower()
    if sort_answer == "да":
        sort_order = input("Отсортировать по возрастанию или по убыванию?\nПользователь: ").lower()
        transactions = sort_transactions_by_date(
            transactions,
            reverse=sort_order == "по убыванию",
        )

    rub_answer = input("Выводить только рублевые транзакции? Да/Нет\nПользователь: ").lower()
    if rub_answer == "да":
        transactions = filter_rub_transactions(transactions)

    search_answer = input(
        "Отфильтровать список транзакций по определенному слову в описании? Да/Нет\n"
        "Пользователь: "
    ).lower()

    if search_answer == "да":
        search = input("Введите строку для поиска в описании:\nПользователь: ")
        transactions = process_bank_search(transactions, search)

    print_transactions(transactions)


if __name__ == "__main__":
    if Path("data").exists():
        main()
    else:
        print("Папка data не найдена.")
