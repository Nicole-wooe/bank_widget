from bank_widget.operations import process_bank_operations, process_bank_search


def main() -> None:
    """Main function of the program."""
    data = [
        {"description": "Перевод организации"},
        {"description": "Открытие вклада"},
        {"description": "Перевод с карты на карту"},
        {"description": "Перевод организации"},
    ]

    print("Привет! Добро пожаловать в программу работы с банковскими транзакциями.")

    search = input("Введите строку для поиска: ")
    result = process_bank_search(data, search)
    print(result)

    categories = ["Перевод организации", "Открытие вклада"]
    stats = process_bank_operations(data, categories)
    print(stats)


if __name__ == "__main__":
    main()
