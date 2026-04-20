# src/bank_widget/decorators.py
"""Module with decorators for logging function execution."""

from __future__ import annotations

from functools import wraps
from pathlib import Path
from typing import Callable, Optional, ParamSpec, TypeVar

P = ParamSpec("P")
R = TypeVar("R")


def _write_log(message: str, filename: Optional[str] = None) -> None:
    """Write log message to console or append it to a file."""
    if filename is None:
        print(message)
        return

    with Path(filename).open("a", encoding="utf-8") as file:
        file.write(f"{message}\n")


def log(
    filename: Optional[str] = None,
) -> Callable[[Callable[P, R]], Callable[P, R]]:
    """
    Decorate a function and log its execution result.

    If filename is provided, logs are written to a file.
    Otherwise logs are printed to console.
    """

    def decorator(func: Callable[P, R]) -> Callable[P, R]:
        """Wrap function with logging."""

        @wraps(func)
        def wrapper(*args: P.args, **kwargs: P.kwargs) -> R:
            """Execute function and log success or error."""
            _write_log(
                f"Calling {func.__name__} with args={args}, kwargs={kwargs}",
                filename,
            )

            try:
                result = func(*args, **kwargs)
                _write_log(f"{func.__name__} ok, result={result}", filename)
                return result
            except Exception as error:
                _write_log(
                    (
                        f"{func.__name__} error: {type(error).__name__}. "
                        f"Inputs: args={args}, kwargs={kwargs}"
                    ),
                    filename,
                )
                raise

        return wrapper

    return decorator
