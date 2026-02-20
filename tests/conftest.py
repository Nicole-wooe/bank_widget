import pytest


@pytest.fixture
def operations():
    return [
        {"id": 1, "state": "EXECUTED", "date": "2024-03-11T10:26:18.671407Z"},
        {"id": 2, "state": "CANCELED", "date": "2024-01-01T00:00:00.000000Z"},
        {"id": 3, "state": "EXECUTED", "date": "2023-12-31T23:59:59.000000Z"},
    ]