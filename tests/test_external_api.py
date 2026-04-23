from unittest.mock import Mock, patch

import pytest

from src.bank_widget.external_api import convert_to_rub


def test_convert_to_rub_for_rub():
    transaction = {
        "operationAmount": {
            "amount": "100.50",
            "currency": {"code": "RUB"},
        }
    }

    result = convert_to_rub(transaction)

    assert result == 100.50


@patch("src.bank_widget.external_api.requests.get")
@patch("src.bank_widget.external_api.os.getenv")
def test_convert_to_rub_for_usd(mock_getenv, mock_get):
    mock_getenv.return_value = "test_key"

    mock_response = Mock()
    mock_response.json.return_value = {"rates": {"RUB": 90.0}}
    mock_response.raise_for_status.return_value = None
    mock_get.return_value = mock_response

    transaction = {
        "operationAmount": {
            "amount": "10",
            "currency": {"code": "USD"},
        }
    }

    result = convert_to_rub(transaction)

    assert result == 900.0
    mock_get.assert_called_once()


@patch("src.bank_widget.external_api.requests.get")
@patch("src.bank_widget.external_api.os.getenv")
def test_convert_to_rub_for_eur(mock_getenv, mock_get):
    mock_getenv.return_value = "test_key"

    mock_response = Mock()
    mock_response.json.return_value = {"rates": {"RUB": 100.0}}
    mock_response.raise_for_status.return_value = None
    mock_get.return_value = mock_response

    transaction = {
        "operationAmount": {
            "amount": "5",
            "currency": {"code": "EUR"},
        }
    }

    result = convert_to_rub(transaction)

    assert result == 500.0
    mock_get.assert_called_once()


def test_convert_to_rub_missing_fields():
    with pytest.raises(ValueError):
        convert_to_rub({})


@patch("src.bank_widget.external_api.os.getenv")
def test_convert_to_rub_without_api_key(mock_getenv):
    mock_getenv.return_value = None

    transaction = {
        "operationAmount": {
            "amount": "10",
            "currency": {"code": "USD"},
        }
    }

    with pytest.raises(ValueError):
        convert_to_rub(transaction)


def test_convert_to_rub_unsupported_currency():
    transaction = {
        "operationAmount": {
            "amount": "10",
            "currency": {"code": "GBP"},
        }
    }

    with pytest.raises(ValueError):
        convert_to_rub(transaction)
