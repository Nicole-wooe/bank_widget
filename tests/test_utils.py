from src.bank_widget.utils import load_operations_from_json


def test_load_valid_file():
    data = load_operations_from_json("data/operations.json")
    assert isinstance(data, list)


def test_file_not_found():
    data = load_operations_from_json("wrong_path.json")
    assert data == []


def test_empty_file(tmp_path):
    file = tmp_path / "empty.json"
    file.write_text("")

    data = load_operations_from_json(str(file))
    assert data == []


def test_not_list(tmp_path):
    file = tmp_path / "data.json"
    file.write_text('{"a": 1}')

    data = load_operations_from_json(str(file))
    assert data == []
