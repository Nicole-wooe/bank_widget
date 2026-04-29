from src.bank_widget.product import Product


def test_product_init():
    product = Product("Телефон", "Смартфон", 1000.0, 5)

    assert product.name == "Телефон"
    assert product.description == "Смартфон"
    assert product.price == 1000.0
    assert product.quantity == 5
