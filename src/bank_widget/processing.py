def filter_by_state(operations, state="EXECUTED"):
    """
    Фильтрует список операций по значению ключа state.

    operations — список словарей с операциями
    state — нужное значение state (по умолчанию EXECUTED)

    Возвращает новый список операций.
    """
    result = []

    for operation in operations:
        if operation.get("state") == state:
            result.append(operation)

    return result


def sort_by_date(operations, reverse=True):
    """
    Сортирует операции по дате (ключ 'date').

    operations — список словарей
    reverse — порядок сортировки:
        True  — по убыванию (по умолчанию)
        False — по возрастанию

    Возвращает новый список.
    """
    return sorted(operations, key=lambda x: x["date"], reverse=reverse)
