from __future__ import annotations

from datetime import datetime
from typing import Any


def filter_by_state(
    operations: list[dict[str, Any]], state: str = "EXECUTED"
) -> list[dict[str, Any]]:
    return [op for op in operations if op.get("state") == state]


def sort_by_date(
    operations: list[dict[str, Any]], reverse: bool = True
) -> list[dict[str, Any]]:
    def key(op: dict[str, Any]) -> datetime:
        date_str = op.get("date", "")
        return datetime.fromisoformat(date_str.replace("Z", "+00:00"))

    return sorted(operations, key=key, reverse=reverse)
