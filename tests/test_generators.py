import pytest

from bank_widget.generators import (
    card_number_generator,
    filter_by_currency,
    transaction_descriptions,
)


@pytest.fixture
def transactions():
    return [
        {
            "id": 1,
            "operationAmount": {"currency": {"code": "USD"}},
            "description": "Перевод организации",
        },
        {
            "id": 2,
            "operationAmount": {"currency": {"code": "RUB"}},
            "description": "Перевод со счета на счет",
        },
        {
            "id": 3,
            "operationAmount": {"currency": {"code": "USD"}},
            "description": "Перевод с карты на карту",
        },
    ]


def test_filter_by_currency_usd(transactions):
    assert [t["id"] for t in filter_by_currency(transactions, "USD")] == [1, 3]


def test_filter_by_currency_no_matches(transactions):
    assert list(filter_by_currency(transactions, "EUR")) == []


def test_filter_by_currency_empty():
    assert list(filter_by_currency([], "USD")) == []


def test_transaction_descriptions(transactions):
    assert list(transaction_descriptions(transactions)) == [
        "Перевод организации",
        "Перевод со счета на счет",
        "Перевод с карты на карту",
    ]


def test_transaction_descriptions_empty():
    assert list(transaction_descriptions([])) == []


@pytest.mark.parametrize(
    ("start", "stop", "expected"),
    [
        (
            1,
            5,
            [
                "0000 0000 0000 0001",
                "0000 0000 0000 0002",
                "0000 0000 0000 0003",
                "0000 0000 0000 0004",
                "0000 0000 0000 0005",
            ],
        ),
        (
            9999_9999_9999_9998,
            9999_9999_9999_9999,
            [
                "9999 9999 9999 9998",
                "9999 9999 9999 9999",
            ],
        ),
    ],
)
def test_card_number_generator_range(start, stop, expected):
    assert list(card_number_generator(start, stop)) == expected


@pytest.mark.parametrize(
    ("start", "stop"),
    [
        (0, 5),
        (10, 5),
        (1, 10_000_0000_0000_0000),
    ],
)
def test_card_number_generator_invalid(start, stop):
    with pytest.raises(ValueError):
        list(card_number_generator(start, stop))
