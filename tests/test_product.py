import pytest

from src.bank_widget.product import Product, Smartphone, LawnGrass


def test_product_init():
    product = Product("Samsung Galaxy S23 Ultra", "256GB", 180000.0, 5)

    assert product.name == "Samsung Galaxy S23 Ultra"
    assert product.description == "256GB"
    assert product.price == 180000.0
    assert product.quantity == 5


def test_product_price_setter_positive():
    product = Product("Товар", "Описание", 100.0, 5)

    product.price = 300

    assert product.price == 300


def test_product_price_setter_negative(capsys):
    product = Product("Товар", "Описание", 100.0, 5)

    product.price = -100

    captured = capsys.readouterr()

    assert "Цена не должна быть нулевой или отрицательной" in captured.out


def test_new_product():
    data = {
        "name": "iPhone 15",
        "description": "Новый смартфон",
        "price": 150000.0,
        "quantity": 8
    }

    product = Product.new_product(data)

    assert product.name == "iPhone 15"
    assert product.price == 150000.0
    assert product.quantity == 8


def test_product_str():
    product = Product("Телефон", "Описание", 50000.0, 3)

    assert str(product) == "Телефон, 50000.0 руб. Остаток: 3 шт."


def test_add_products():
    product_1 = Product("Товар 1", "Описание", 100.0, 2)
    product_2 = Product("Товар 2", "Описание", 200.0, 3)

    assert product_1 + product_2 == 800.0


def test_smartphone_init():
    smartphone = Smartphone(
        "Samsung Galaxy S23",
        "Смартфон",
        100000.0,
        5,
        95.5,
        "S23",
        256,
        "Черный"
    )

    assert smartphone.efficiency == 95.5
    assert smartphone.model == "S23"
    assert smartphone.memory == 256
    assert smartphone.color == "Черный"


def test_lawn_grass_init():
    grass = LawnGrass(
        "Газон",
        "Трава",
        500.0,
        20,
        "Россия",
        "7 дней",
        "Зеленый"
    )

    assert grass.country == "Россия"
    assert grass.germination_period == "7 дней"
    assert grass.color == "Зеленый"


def test_add_different_classes():
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

    grass = LawnGrass(
        "Газон",
        "Трава",
        500.0,
        10,
        "Россия",
        "7 дней",
        "Зеленый"
    )

    with pytest.raises(TypeError):
        smartphone + grass
