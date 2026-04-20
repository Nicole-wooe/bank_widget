"""Tests for decorators module."""

from pathlib import Path

import pytest

from src.bank_widget.decorators import log


def test_log_console_ok(capsys: pytest.CaptureFixture[str]) -> None:
    """Test successful logging to console."""

    @log()
    def add(x: int, y: int) -> int:
        return x + y

    assert add(1, 2) == 3

    captured = capsys.readouterr()
    output = captured.out.strip().splitlines()

    assert output[0] == "Calling add with args=(1, 2), kwargs={}"
    assert output[1] == "add ok, result=3"


def test_log_console_error(capsys: pytest.CaptureFixture[str]) -> None:
    """Test error logging to console."""

    @log()
    def div(x: int, y: int) -> float:
        return x / y

    with pytest.raises(ZeroDivisionError):
        div(1, 0)

    captured = capsys.readouterr()
    output = captured.out.strip().splitlines()

    assert output[0] == "Calling div with args=(1, 0), kwargs={}"
    assert output[1] == (
        "div error: ZeroDivisionError. " "Inputs: args=(1, 0), kwargs={}"
    )


def test_log_file_ok(tmp_path: Path) -> None:
    """Test successful logging to file."""
    log_file = tmp_path / "mylog.txt"

    @log(filename=str(log_file))
    def add(x: int, y: int) -> int:
        return x + y

    assert add(1, 2) == 3

    output = log_file.read_text(encoding="utf-8").strip().splitlines()

    assert output[0] == "Calling add with args=(1, 2), kwargs={}"
    assert output[1] == "add ok, result=3"


def test_log_file_error(tmp_path: Path) -> None:
    """Test error logging to file."""
    log_file = tmp_path / "mylog.txt"

    @log(filename=str(log_file))
    def div(x: int, y: int) -> float:
        return x / y

    with pytest.raises(ZeroDivisionError):
        div(1, 0)

    output = log_file.read_text(encoding="utf-8").strip().splitlines()

    assert output[0] == "Calling div with args=(1, 0), kwargs={}"
    assert output[1] == (
        "div error: ZeroDivisionError. " "Inputs: args=(1, 0), kwargs={}"
    )
