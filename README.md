## Модуль `decorators`

В проект добавлен модуль `decorators` с декоратором `log`.

### `log(filename: str | None = None)`

Логирует результат выполнения функции:
- при успехе: `<имя_функции> ok`
- при ошибке: `<имя_функции> error: <тип ошибки>. Inputs: <args>, <kwargs>`

Пример:

```python
from bank_widget.decorators import log

@log(filename="mylog.txt")
def my_function(x, y):
    return x + y

my_function(1, 2)