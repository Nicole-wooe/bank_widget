import pytest

from bank_widget.masks import (get_mask_account, get_mask_card_number,
                               mask_email)


@pytest.mark.parametrize(
    "number, expected",
    [
        (1234567812345678, "1234 56** **** 5678"),
        (1111222233334444, "1111 22** **** 4444"),
    ],
)
def test_get_mask_card_number(number, expected):
    assert get_mask_card_number(number) == expected


@pytest.mark.parametrize(
    "account, expected",
    [
        (12345678901234567890, "**7890"),
        (99990000111122223333, "**3333"),
    ],
)
def test_get_mask_account(account, expected):
    assert get_mask_account(account) == expected


@pytest.mark.parametrize(
    "email, expected",
    [
        ("nikol@gmail.com", "ni***@gmail.com"),
        ("ab@mail.ru", "ab@mail.ru"),
        ("a@mail.ru", "a@mail.ru"),
    ],
)
def test_mask_email(email, expected):
    assert mask_email(email) == expected
