from unittest.mock import Mock, patch

from src.transaction_readers import (
    read_transactions_from_csv,
    read_transactions_from_excel,
)


@patch("src.transaction_readers.pd.read_csv")
def test_read_transactions_from_csv(mock_read_csv: Mock) -> None:
    """Test reading transactions from CSV file."""
    mock_dataframe = Mock()
    mock_dataframe.to_dict.return_value = [
        {"id": 1, "amount": 100},
        {"id": 2, "amount": 200},
    ]
    mock_read_csv.return_value = mock_dataframe

    result = read_transactions_from_csv("transactions.csv")

    mock_read_csv.assert_called_once_with("transactions.csv", sep=";")
    mock_dataframe.to_dict.assert_called_once_with(orient="records")
    assert result == [
        {"id": 1, "amount": 100},
        {"id": 2, "amount": 200},
    ]


@patch("src.transaction_readers.pd.read_excel")
def test_read_transactions_from_excel(mock_read_excel: Mock) -> None:
    """Test reading transactions from Excel file."""
    mock_dataframe = Mock()
    mock_dataframe.to_dict.return_value = [
        {"id": 1, "amount": 100},
        {"id": 2, "amount": 200},
    ]
    mock_read_excel.return_value = mock_dataframe

    result = read_transactions_from_excel("transactions_excel.xlsx")

    mock_read_excel.assert_called_once_with("transactions_excel.xlsx")
    mock_dataframe.to_dict.assert_called_once_with(orient="records")
    assert result == [
        {"id": 1, "amount": 100},
        {"id": 2, "amount": 200},
    ]
