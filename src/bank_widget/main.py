from src.bank_widget.product import Product, Smartphone, LawnGrass
from src.bank_widget.category import Category


def main() -> None:
    product_1 = Product("Apple", "Смартфон", 100000.0, 5)

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
        "Электроника",
        [product_1, smartphone]
    )

    print(product_1)
    print(smartphone)
    print(grass)

    print(category)

    print("Средняя цена:",
          category.middle_price())

    empty_category = Category(
        "Пусто",
        "Нет товаров",
        []
    )

    print("Средняя цена пустой категории:",
          empty_category.middle_price())

    try:
        Product(
            "Ошибка",
            "Тест",
            100.0,
            0
        )
    except ValueError as error:
        print(error)


if __name__ == "__main__":
    main()
