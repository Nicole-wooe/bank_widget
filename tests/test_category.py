import pytest

from src.bank_widget.category import Category
from src.bank_widget.product import Product, Smartphone


def test_category_init():
    product_1 = Product("Samsung Galaxy S23 Ultra", "256GB", 180000.0, 5)

    category = Category(
        "Смартфоны",
        "Современные смартфоны",
        [product_1]
    )

    assert category.name == "Смартфоны"
    assert category.description == "Современные смартфоны"


def test_category_count():
    Category.category_count = 0

    product_1 = Product("Samsung", "Описание", 100000.0, 5)

    Category("Телефоны", "Описание", [product_1])

    assert Category.category_count == 1


def test_product_count():
    Category.product_count = 0

    product_1 = Product("Samsung", "Описание", 100000.0, 5)
    product_2 = Product("iPhone", "Описание", 120000.0, 3)

    Category("Телефоны", "Описание", [product_1, product_2])

    assert Category.product_count == 2


def test_products_property():
    product_1 = Product("Samsung", "Описание", 100000.0, 5)

    category = Category("Телефоны", "Описание", [product_1])

    assert (
        category.products
        == "Samsung, 100000.0 руб. Остаток: 5 шт.\n"
    )


def test_category_str():
    product_1 = Product("Samsung", "Описание", 100000.0, 5)
    product_2 = Product("iPhone", "Описание", 120000.0, 3)

    category = Category(
        "Телефоны",
        "Описание",
        [product_1, product_2]
    )

    assert str(category) == "Телефоны, количество продуктов: 8 шт."


def test_add_product():
    category = Category("Телефоны", "Описание", [])

    product = Product("Samsung", "Описание", 100000.0, 5)

    category.add_product(product)

    assert "Samsung" in category.products


def test_add_smartphone():
    category = Category("Смартфоны", "Описание", [])

    smartphone = Smartphone(
        "Samsung",
        "Смартфон",
        100000.0,
        2,
        90.0,
        "S23",
        256,
        "Черный"
    )

    category.add_product(smartphone)

    assert "Samsung" in category.products


def test_add_wrong_product():
    category = Category("Смартфоны", "Техника", [])

    with pytest.raises(TypeError):
        category.add_product("не продукт")


def test_middle_price():
    product_1 = Product("Samsung", "Описание", 100000.0, 5)
    product_2 = Product("iPhone", "Описание", 120000.0, 3)

    category = Category(
        "Телефоны",
        "Описание",
        [product_1, product_2]
    )

    assert category.middle_price() == 110000.0


def test_middle_price_empty_category():
    category = Category("Пусто", "Нет товаров", [])

    assert category.middle_price() == 0
