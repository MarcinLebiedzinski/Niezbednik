class Calculator:

    def __init__(self):
        self.a = 0
        self.b = 0

    def add(self, a, b):
        return a + b

    def sub(self, a, b):
        return a - b

    def mul(self, a, b):
        return a * b

    def div(self, a, b):
        try:
            return a / b
        except ZeroDivisionError:
            print("Can't divide by Zero")
            return None

class LoggingCalculator(Calculator):

    def __init__(self):
        super().__init__()
        self.history = []

    def add(self, a, b):
        add = super().add(a, b)
        self.history.append(f"{a} + {b} = {a + b}")
        return add

    def sub(self, a, b):
        sub = super().sub(a, b)
        self.history.append(f"{a} - {b} = {a - b}")
        return sub

    def mul(self, a, b):
        mul = super().mul(a, b)
        self.history.append(f"{a} * {b} = {a * b}")
        return mul

    def div(self, a, b):
        try:
            div = super().div(a, b)
            self.history.append(f"{a} / {b} = {a / b}")
            return div
        except ZeroDivisionError:
            return None

    def history(self):
        return self.history


calc = LoggingCalculator()
print(calc.add(2, 3))
print(calc.mul(3, 3))
print(calc.sub(7, 4))
print(calc.div(5, 2))
print(calc.history)

