from src.bank_widget.product import Product


class Category:
    category_count = 0
    product_count = 0

    def __init__(
        self,
        name: str,
        description: str,
        products: list[Product]
    ) -> None:
        self.name = name
        self.description = description
        self.__products = products

        Category.category_count += 1
        Category.product_count += len(products)

    def add_product(self, product: Product) -> None:
        if not isinstance(product, Product):
            raise TypeError(
                "Можно добавлять только объекты Product или его наследников"
            )

        self.__products.append(product)
        Category.product_count += 1

    @property
    def products(self) -> str:
        result = ""

        for product in self.__products:
            result += f"{str(product)}\n"

        return result

    def middle_price(self) -> float:
        try:
            total_price = 0

            for product in self.__products:
                total_price += product.price

            return total_price / len(self.__products)
        except ZeroDivisionError:
            return 0

    def __str__(self) -> str:
        total_quantity = 0

        for product in self.__products:
            total_quantity += product.quantity

        return f"{self.name}, количество продуктов: {total_quantity} шт."
