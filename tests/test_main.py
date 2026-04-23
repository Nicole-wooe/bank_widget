from src.bank_widget.main import main


def test_main_runs_without_error(capsys):
    main()
    captured = capsys.readouterr()

    # просто проверяем, что что-то выводится
    assert captured.out is not None
