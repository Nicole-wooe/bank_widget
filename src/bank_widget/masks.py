import logging

# src/masks.py
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

file_handler = logging.FileHandler("logs/masks.log", mode="w", encoding="utf-8")
file_handler.setLevel(logging.DEBUG)

file_formatter = logging.Formatter(
    "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)

file_handler.setFormatter(file_formatter)

if not logger.handlers:
    logger.addHandler(file_handler)

def get_mask_card_number(card_number: int) -> str:
    """
    Return masked bank card number in format 'XXXX XX** **** XXXX'.

    The function shows the first 6 and the last 4 digits of the card number.
    All middle digits are masked with asterisks.

    :param card_number: Card number as an integer.
    :return: Masked card number string.
    """
    card_str = str(card_number)

    logger.info(f"Masking card number: {card_number}")

    # Предполагаем, что длина >= 10, как в примере (обычное число цифр карты — 16).
    first_four = card_str[:4]
    next_two = card_str[4:6]
    last_four = card_str[-4:]

    logger.info("Card number masked successfully")

    return f"{first_four} {next_two}** **** {last_four}"


def get_mask_account(account_number: int) -> str:
    """
    Return masked bank account number in format '**XXXX'.

    The function shows only the last 4 digits of the account number.

    :param account_number: Bank account number as an integer.
    :return: Masked account number string.
    """
    account_str = str(account_number)
    logger.info(f"Masking account number: {account_number}")
    last_four = account_str[-4:]
    logger.info("Account number masked successfully")
    return f"**{last_four}"


def mask_email(email: str) -> str:
    """
    Mask email so that only the first 2 characters of the name are visible.

    Examples:
    nikol@gmail.com -> ni***@gmail.com
    ab@mail.ru -> ab@mail.ru
    a@mail.ru -> a@mail.ru
    """
    logger.info(f"Masking email: {email}")

    try:
        name, domain = email.split("@")
    except ValueError:
        logger.error("Invalid email format")
        raise
    # Если имя слишком короткое — ничего не меняем
    if len(name) <= 2:
        return email

    masked_name = name[:2] + "*" * (len(name) - 2)

    logger.info("Email masked successfully")
    return masked_name + "@" + domain
