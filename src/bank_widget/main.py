from bank_widget.utils import get_date, mask_account_card, mask_email


def main() -> None:
    print(mask_account_card("Visa Platinum 70007922839466897"))
    print(mask_account_card("Счет 40817810099910004312"))
    print(get_date("2024-03-11T02:26:18.671407"))
    print(mask_email("nikol@gmail.com"))


if __name__ == "__main__":
    main()
