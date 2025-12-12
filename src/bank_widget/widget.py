"""High-level helpers for working with masked card/account data and dates."""

from datetime import datetime

from bank_widget.masks import get_mask_account, get_mask_card_number


def get_date(date_str: str) -> str:
    """Преобразует ISO-дату в формат ДД.ММ.ГГГГ."""
    dt = datetime.fromisoformat(date_str)
    return dt.strftime("%d.%m.%Y")


def mask_account_card(account_or_card: str) -> str:
    """
    Принимает строку вида:
      - 'Visa Platinum 7000792283946897'
      - 'Счет 40817810009910004312'

    Возвращает:
      - 'Visa Platinum 7000 79** **** 6897'
      - 'Счет **4312'
    """
    # Разделяем на "имя" и "номер" по последнему пробелу
    name_and_number = account_or_card.rsplit(" ", maxsplit=1)
    if len(name_and_number) != 2:
        raise ValueError("Ожидаю строку с названием и номером, разделёнными пробелом")

    name, number_str = name_and_number
    number_int = int(number_str)

    # если начинается со слова "счет" — значит банковский счёт
    if name.lower().startswith("счет"):
        masked_number = get_mask_account(number_int)
    else:
        masked_number = get_mask_card_number(number_int)

    return f"{name} {masked_number}"
