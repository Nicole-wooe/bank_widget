from bank_widget.masks import mask_email
from bank_widget.widget import get_date, mask_account_card


def main() -> None:
    print(mask_account_card("Visa Platinum 70007922839466897"))
    print(mask_account_card("Счет 40817810099910004312"))
    print(get_date("2024-03-11T02:26:18.671407"))
    print(mask_email("nikol@gmail.com"))


if __name__ == "__main__":
    main()


"""Utility functions for masking card and account numbers."""


def get_mask_card_number(card_number: int) -> str:
    """Return masked bank card number in format ``"XXXX XX** **** XXXX"``.

    The function shows the first 6 and the last 4 digits of the card number.
    All middle digits are masked with asterisks.

    Parameters
    ----------
    card_number:
        Card number as an integer.

    Returns
    -------
    str
        Masked card number string.
    """
    card_str = str(card_number)
    # Для стандартной 16-значной карты получится: XXXX XX** **** XXXX
    return f"{card_str[:4]} {card_str[4:6]}** **** {card_str[-4:]}"


def get_mask_account(account_number: int) -> str:
    """Return masked bank account number in format ``"**XXXX"``.

    The function shows only the last 4 digits of the account number.

    Parameters
    ----------
    account_number:
        Bank account number as an integer.

    Returns
    -------
    str
        Masked account number string.
    """
    account_str = str(account_number)
    last_four = account_str[-4:]
    return f"**{last_four}"
