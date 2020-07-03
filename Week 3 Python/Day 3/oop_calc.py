class Calculator:
    classification: "arithmetic operator"

    def __init__(self, add, multiply, divide, subtract, on, off, name):
        self.add = add
        self.multiply = multiply
        self.divide = divide
        self.subtract = subtract
        self.on = on
        self.off = off
        self.name = name

    def on(self):
        print(self.name + " is on, what would you like to do?")

    def add(self, num1, num2):
        return num1 + num2
    print(add())


