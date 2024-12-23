from constants import SEPARATOR

class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return f"{self.name}{SEPARATOR}{self.price:.2f}"
