## Модуль `generators`

В проект добавлен модуль `generators`, содержащий генераторы для обработки транзакций.

### `filter_by_currency(transactions, currency_code)`
Возвращает итератор транзакций, где валюта операции соответствует `currency_code`.

Пример:
```python
from bank_widget.generators import filter_by_currency

usd_transactions = filter_by_currency(transactions, "USD")
for _ in range(2):
    print(next(usd_transactions))