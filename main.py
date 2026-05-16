from src.bank_widget.product import Product, Smartphone, LawnGrass
from src.bank_widget.category import Category


def main() -> None:
    product = Product("Apple", "Смартфон", 100000.0, 5)

    smartphone = Smartphone(
        "Samsung Galaxy S23",
        "Смартфон",
        120000.0,
        3,
        95.5,
        "S23",
        256,
        "Черный"
    )

    grass = LawnGrass(
        "Газон",
        "Трава",
        500.0,
        20,
        "Россия",
        "7 дней",
        "Зеленый"
    )

    category = Category(
        "Техника",
        "Разные товары",
        [product, smartphone]
    )

    print(product)
    print(smartphone)
    print(grass)
    print(category)


if __name__ == "__main__":
    main()