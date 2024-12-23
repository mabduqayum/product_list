from constants import SEPARATOR
from product import Product
from memo import Memo


class ProductList(Memo):
    def __init__(self, filename):
        super().__init__(filename)
        self.products = []
        self.load_products()

    def load_products(self):
        self.products.clear()
        lines = self.load_from_file()
        for line in lines:
            try:
                name, price = line.strip().split(SEPARATOR)
                self.products.append(Product(name, float(price)))
            except ValueError:
                print(f"Error parsing line: {line.strip()}. Skipping.")

    def save_products(self):
        content = [f"{product}\n" for product in self.products]
        self.save_to_file(content)
        self.load_products()

    def save_product(self, product):
        self.append_to_file(str(product))
        self.load_products()

    def add_product(self, name, price):
        for product in self.products:
            if product.name == name:
                print(f"Product {name} already added.")
                return
        product = Product(name, price)
        self.save_product(product)
        print(f"ADDED: {product}")

    def update_product(self, name, new_price):
        for product in self.products:
            if product.name == name:
                product.price = new_price
                self.save_products()
                print(f"UPDATED: {product}")
                return
        print(f"Product '{name}' not found.")

    def delete_product(self, name):
        for product in self.products:
            if product.name == name:
                self.products.remove(product)
                self.save_products()
                print(f"DELETED: {name}")
                return
        print(f"Product '{name}' not found.")

    def print_total(self):
        total = sum(product.price for product in self.products)
        print(f"Total sum: {total:.2f}")

    def list_products(self):
        if len(self.products) == 0:
            print("There are no products.")
            return
        for product in self.products:
            print(product)
