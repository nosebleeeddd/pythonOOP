import random

class Dice():
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def roll(self):
        result = self.num1 + self.num2
        print(f"you just rolled {self.num1} and {self.num2}!")
        if result == 12:
            print(f"You rolled the highest number! : {result}")
        elif result == 10 or result == 11:
            print(f"High roller, you rolled an: {result}!")
        elif result <= 9:
            print(f"An OK roll! : {result}")
        else:
            print(f"you rolled a {result}")

def retry():
    redo = input("Would you like to roll? Type 'quit' to end: ")
    if redo == 'quit':
        return False
    else:
        return True

while retry():
    num1 = random.randint(1, 6)
    num2 = random.randint(1, 6)
    dice = Dice(num1, num2)
    dice.roll()


