from src.bank_widget.product import Product


def test_product_init():
    product = Product("Телефон", "Смартфон", 1000.0, 5)

    assert product.name == "Телефон"
    assert product.description == "Смартфон"
    assert product.price == 1000.0
    assert product.quantity == 5


def test_price_setter_invalid():
    p = Product("Test", "Desc", 100, 1)
    p.price = -10
    assert p.price == 100


def test_product_str():
    product = Product("Телефон", "Смартфон", 1000.0, 5)

    assert str(product) == "Телефон, 1000.0 руб. Остаток: 5 шт."


def test_product_add():
    product_1 = Product("Телефон", "Смартфон", 1000.0, 5)
    product_2 = Product("Ноутбук", "Мощный", 2000.0, 3)

    assert product_1 + product_2 == 11000.0
