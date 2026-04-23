"""Module for currency conversion via external API."""

import os
from typing import Any

import requests
from dotenv import load_dotenv

load_dotenv()

API_URL = "https://api.apilayer.com/exchangerates_data/latest"


def convert_to_rub(transaction: dict[str, Any]) -> float:
    """
    Convert transaction amount to rubles.

    Args:
        transaction: Dictionary with transaction data.

    Returns:
        Transaction amount in RUB as float.
    """
    operation_amount = transaction.get("operationAmount", {})
    amount_str = operation_amount.get("amount")
    currency_info = operation_amount.get("currency", {})
    currency_code = currency_info.get("code")

    if amount_str is None or currency_code is None:
        raise ValueError("Transaction does not contain required fields")

    amount = float(amount_str)

    if currency_code == "RUB":
        return amount

    if currency_code not in ("USD", "EUR"):
        raise ValueError("Unsupported currency")

    api_key = os.getenv("EXCHANGE_API_KEY")
    if not api_key:
        raise ValueError("EXCHANGE_API_KEY is not set")

    headers = {"apikey": api_key}
    params = {"base": currency_code, "symbols": "RUB"}

    response = requests.get(API_URL, headers=headers, params=params, timeout=10)
    response.raise_for_status()
    data = response.json()

    rate = data["rates"]["RUB"]
    return float(amount * rate)
