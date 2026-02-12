# bank_widget

Учебный проект: виджет банковских операций.

## Функции обработки (processing)

Файл: `src/bank_widget/processing.py`

### filter_by_state(operations, state="EXECUTED")
Возвращает новый список операций, у которых `state` совпадает с переданным значением.

### sort_by_date(operations, reverse=True)
Возвращает новый список операций, отсортированный по ключу `date`.
По умолчанию сортировка по убыванию (сначала более новые).
