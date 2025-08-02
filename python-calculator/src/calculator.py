from operations.addition import add
from operations.subtraction import subtract

class Calculator:
    def add(self, a, b):
        return add(a, b)

    def subtract(self, a, b):
        return subtract(a, b)