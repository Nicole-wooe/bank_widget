"""Utilities for loading financial operations from JSON files."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


def load_operations_from_json(file_path: str) -> list[dict[str, Any]]:
    """
    Load financial operations from a JSON file.

    Args:
        file_path: Path to the JSON file.

    Returns:
        A list of dictionaries with financial operations data.
        Returns an empty list if:
        - file does not exist
        - file is empty
        - JSON is invalid
        - JSON is not a list
    """
    path = Path(file_path)

    if not path.exists():
        return []

    try:
        content = path.read_text(encoding="utf-8")
    except OSError:
        return []

    if not content.strip():
        return []

    try:
        data = json.loads(content)
    except json.JSONDecodeError:
        return []

    if not isinstance(data, list):
        return []

    if not all(isinstance(item, dict) for item in data):
        return []

    return data
