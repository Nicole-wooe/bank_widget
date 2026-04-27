import re
from collections import Counter


def process_bank_search(data: list[dict], search: str) -> list[dict]:
    """Возвращает операции, в описании которых есть строка поиска."""
    return [
        operation
        for operation in data
        if re.search(search, str(operation.get("description", "")), re.IGNORECASE)
    ]


def process_bank_operations(data: list[dict], categories: list[str]) -> dict:
    """Считает количество операций по категориям из поля description."""
    descriptions = [
        operation.get("description", "")
        for operation in data
    ]

    counter = Counter()

    for category in categories:
        counter[category] = sum(
            1 for description in descriptions if category.lower() in description.lower()
        )

    return dict(counter)
