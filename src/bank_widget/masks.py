# src/masks.py


def get_mask_card_number(card_number: int) -> str:
    """
    Return masked bank card number in format 'XXXX XX** **** XXXX'.

    The function shows the first 6 and the last 4 digits of the card number.
    All middle digits are masked with asterisks.

    :param card_number: Card number as an integer.
    :return: Masked card number string.
    """
    card_str = str(card_number)

    # Предполагаем, что длина >= 10, как в примере (обычное число цифр карты — 16).
    first_four = card_str[:4]
    next_two = card_str[4:6]
    last_four = card_str[-4:]

    return f"{first_four} {next_two}** **** {last_four}"


def get_mask_account(account_number: int) -> str:
    """
    Return masked bank account number in format '**XXXX'.

    The function shows only the last 4 digits of the account number.

    :param account_number: Bank account number as an integer.
    :return: Masked account number string.
    """
    account_str = str(account_number)
    last_four = account_str[-4:]
    return f"**{last_four}"


def mask_email(email: str) -> str:
    """
    Mask email so that only the first 2 characters of the name are visible.

    Examples:
    nikol@gmail.com -> ni***@gmail.com
    ab@mail.ru -> ab@mail.ru
    a@mail.ru -> a@mail.ru
    """
    name, domain = email.split("@")

    # Если имя слишком короткое — ничего не меняем
    if len(name) <= 2:
        return email

    masked_name = name[:2] + "*" * (len(name) - 2)

    return masked_name + "@" + domain
