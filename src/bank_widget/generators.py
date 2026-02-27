from collections.abc import Iterator
from typing import Any


def filter_by_currency(
    transactions: list[dict[str, Any]],
    currency_code: str,
) -> Iterator[dict[str, Any]]:
    """Yield transactions where operationAmount.currency.code equals currency_code."""
    for tx in transactions:
        code = tx.get("operationAmount", {}).get("currency", {}).get("code")
        if code == currency_code:
            yield tx


def transaction_descriptions(
    transactions: list[dict[str, Any]],
) -> Iterator[str]:
    """Yield transaction descriptions one by one."""
    for tx in transactions:
        yield str(tx.get("description", ""))


def card_number_generator(start: int, stop: int) -> Iterator[str]:
    """Generate card numbers in 'XXXX XXXX XXXX XXXX' format for range [start, stop]."""
    if start < 1 or stop > 9999_9999_9999_9999 or start > stop:
        raise ValueError("Invalid range")

    for number in range(start, stop + 1):
        s = f"{number:016d}"
        yield f"{s[0:4]} {s[4:8]} {s[8:12]} {s[12:16]}"
