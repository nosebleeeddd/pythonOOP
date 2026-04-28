class Calculator():
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def add(self):
        result = self.num1 + self.num2
        print(f"Your answer is {result}")

    def subtract(self):
        result = self.num1 - self.num2
        print(f"Your answer is {result}")

    def multiply(self):
        result = self.num1 * self.num2
        print(f"Your answer is {result}")

    def divide(self):
        try:
            result = self.num1 / self.num2
            print(f"Your answer is {result}")
        except ZeroDivisionErrors:
            print("You can't divide by 0")

    def operator(self):
        op = int(input("Please choose a math operator.\n1) Add\n2) Subtract\n3) multiply\n4) divide"))
        return op

def retry():
    redo = input("Would you like to start? Type 'quit' to exit: ")
    if redo == 'quit':
        return False
    else:
        return True

while retry():
    num1 = int(input("Please enter a number:"))
    num2 = int(input("Please enter a number:"))
    calculation = Calculator(num1, num2)
    oper = calculation.operator()
    if oper == 1:
        calculation.add()
    elif oper == 2:
        calculation.subtract()
    elif oper == 3:
        calculation.multiply()
    elif oper == 4:
        calculation.divide()
    else:
        print("Please choose a valid number")


