from bank_widget.masks import mask_email
from bank_widget.widget import get_date, mask_account_card


def test_mask_account_card_for_card() -> None:
    assert (
        mask_account_card("Visa Platinum 7000792283946897")
        == "Visa Platinum 7000 79** **** 6897"
    )


def test_mask_account_card_for_account() -> None:
    assert mask_account_card("Счет 40817810099910004312") == "Счет **4312"


def test_get_date() -> None:
    assert get_date("2024-03-11T02:26:18.671407") == "11.03.2024"


def test_mask_email() -> None:
    assert mask_email("nikol@gmail.com") == "ni***@gmail.com"
