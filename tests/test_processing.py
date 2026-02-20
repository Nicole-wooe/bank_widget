import pytest

from bank_widget.processing import filter_by_state, sort_by_date


@pytest.mark.parametrize(
    "state, expected_ids",
    [
        ("EXECUTED", [1, 3]),
        ("CANCELED", [2]),
        ("UNKNOWN", []),
    ],
)
def test_filter_by_state_parametrized(operations, state, expected_ids):
    result = filter_by_state(operations, state=state)
    assert [op["id"] for op in result] == expected_ids


def test_filter_by_state_default_state_executed(operations):
    result = filter_by_state(operations)
    assert [op["id"] for op in result] == [1, 3]


def test_sort_by_date_desc(operations):
    result = sort_by_date(operations, reverse=True)
    assert [op["id"] for op in result] == [1, 2, 3]


def test_sort_by_date_asc(operations):
    result = sort_by_date(operations, reverse=False)
    assert [op["id"] for op in result] == [3, 2, 1]