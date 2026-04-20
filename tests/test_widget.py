from src.bank_widget.main import get_mask_account as main_get_mask_account
from src.bank_widget.main import \
    get_mask_card_number as main_get_mask_card_number
from src.bank_widget.main import main
from src.bank_widget.masks import mask_email
from src.bank_widget.widget import get_date
from src.bank_widget.widget import get_mask_account as widget_get_mask_account
from src.bank_widget.widget import \
    get_mask_card_number as widget_get_mask_card_number
from src.bank_widget.widget import mask_account_card


def test_mask_account_card_for_card() -> None:
    assert (
        mask_account_card("Visa Platinum 7000792283946897")
        == "Visa Platinum 7000 79** **** 6897"
    )


def test_mask_account_card_for_account() -> None:
    assert mask_account_card("Счет 40817810099910004312") == "Счет **4312"


def test_get_date() -> None:
    assert get_date("2024-03-11T02:26:18.671407") == "11.03.2024"


def test_mask_email() -> None:
    assert mask_email("nikol@gmail.com") == "ni***@gmail.com"


def test_widget_extra():
    # тестируем widget.py
    assert widget_get_mask_card_number(1234567812345678)
    assert widget_get_mask_account(12345678)


def test_main_module_functions(capsys):
    # тестируем main.py функции
    assert main_get_mask_card_number(1234567812345678) == "1234 56** **** 5678"
    assert main_get_mask_account(12345678) == "**5678"

    main()
    captured = capsys.readouterr()
    output = captured.out

    assert "Visa" in output
    assert "gmail" in output


def test_main_output(capsys):
    main()
    captured = capsys.readouterr()
    output = captured.out

    assert "Visa" in output
    assert "gmail" in output
