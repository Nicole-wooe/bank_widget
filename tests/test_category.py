from src.bank_widget.product import Product
from src.bank_widget.category import Category


def test_category_init():
    p1 = Product("Телефон", "Смартфон", 1000.0, 5)
    p2 = Product("Ноутбук", "Мощный", 2000.0, 3)

    category = Category("Техника", "Электроника", [p1, p2])

    assert category.name == "Техника"
    assert category.description == "Электроника"
    assert len(category.products) == 2


def test_counts():
    Category.category_count = 0
    Category.product_count = 0

    p1 = Product("Телефон", "Смартфон", 1000.0, 5)
    p2 = Product("Ноутбук", "Мощный", 2000.0, 3)

    Category("Техника", "Электроника", [p1, p2])

    assert Category.category_count == 1
    assert Category.product_count == 2
