"""Utility functions for processing dates and account/card strings."""

import logging
from datetime import datetime

from bank_widget.masks import get_mask_account, get_mask_card_number

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

file_handler = logging.FileHandler("logs/utils.log", mode="w", encoding="utf-8")
file_handler.setLevel(logging.DEBUG)

file_formatter = logging.Formatter(
    "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)

file_handler.setFormatter(file_formatter)

if not logger.handlers:
    logger.addHandler(file_handler)


def get_date(date_str: str) -> str:
    """Convert ISO date string to DD.MM.YYYY format."""
    logger.info(f"Formatting date: {date_str}")

    try:
        dt = datetime.fromisoformat(date_str)
    except ValueError:
        logger.error(f"Invalid date format: {date_str}")
        raise

    logger.info("Date formatted successfully")
    return dt.strftime("%d.%m.%Y")


def mask_account_card(account_or_card: str) -> str:
    """Mask account or card number from a string."""
    logger.info(f"Masking account/card string: {account_or_card}")

    try:
        name_and_number = account_or_card.rsplit(" ", maxsplit=1)
        if len(name_and_number) != 2:
            raise ValueError("Expected string with name and number")

        name, number_str = name_and_number
        number_int = int(number_str)

        if name.lower().startswith("счет"):
            masked_number = get_mask_account(number_int)
        else:
            masked_number = get_mask_card_number(number_int)

    except ValueError:
        logger.error(f"Invalid account/card string: {account_or_card}")
        raise

    logger.info("Account/card string masked successfully")
    return f"{name} {masked_number}"

def mask_email(email: str) -> str:
    """Mask email so only first 2 characters are visible."""
    logger.info(f"Masking email: {email}")

    try:
        name, domain = email.split("@")
    except ValueError:
        logger.error("Invalid email format")
        raise

    if len(name) <= 2:
        result = email
    else:
        result = name[:2] + "*" * (len(name) - 2) + "@" + domain

    logger.info("Email masked successfully")
    return result
