from src.bank_widget.operations import (process_bank_operations,
                                        process_bank_search)


def test_process_bank_search() -> None:
    data = [
        {"description": "Перевод организации"},
        {"description": "Открытие вклада"},
        {"description": "Перевод с карты на карту"},
    ]

    result = process_bank_search(data, "перевод")

    assert len(result) == 2


def test_process_bank_operations() -> None:
    data = [
        {"description": "Перевод организации"},
        {"description": "Открытие вклада"},
        {"description": "Перевод с карты на карту"},
    ]

    categories = ["Перевод", "Открытие", "Оплата"]

    result = process_bank_operations(data, categories)

    assert result == {
        "Перевод": 2,
        "Открытие": 1,
        "Оплата": 0,
    }
