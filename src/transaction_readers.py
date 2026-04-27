import pandas as pd


def read_transactions_from_csv(file_path: str) -> list[dict]:
    """Считывает транзакции из CSV файла."""
    data = pd.read_csv(file_path, sep=";")
    return data.to_dict(orient="records")


def read_transactions_from_excel(file_path: str) -> list[dict]:
    """Считывает транзакции из Excel файла."""
    data = pd.read_excel(file_path)
    return data.to_dict(orient="records")
