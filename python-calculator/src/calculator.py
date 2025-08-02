from operations.addition import add
from operations.subtraction import subtract
from operations.multiplication import multiply
from operations.division import divide

class Calculator:
    def add(self, a, b):
        return add(a, b)

    def subtract(self, a, b):
        return subtract(a, b)

    def multiply(self, a, b):
        return multiply(a, b)

    def divide(self, a, b):
        return divide(a, b)