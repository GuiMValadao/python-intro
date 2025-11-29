class Calculadora:
    def __init__(self):
        self.current = 0
        self.total = 0

    def set(self, valor):
        self.current = valor

    def add(self):
        self.total += self.current

    def sub(self):
        self.total -= self.current

    def total(self):
        return self.total


def increment(x):
    return x + 1
