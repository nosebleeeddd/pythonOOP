# simple bmi calculator

class BMI():
    def __init__(self, height, weight):
        self.height = height
        self.weight = weight

    def calc(self):
        result = self.weight / (self.height ** 2)
        new = round(result, 2)
        print(f"Your BMI is calculated at {new}")
        if result <= 18.5:
            print("Your results are Underweight")
        elif result > 18.5 and result <= 24.9:
            print("Your results are Healthy")
        elif result > 25 and result <= 29.9:
            print("Your results are Overweight")
        else:
            print("Your results are Obese")

def retry():
    redo = input("Would you like to use the BMI calculator? Type 'quit' to exit: ")
    if redo == 'quit':
        return False
    else:
        return True

while retry():
    height = float(input("please enter your height in meters: "))
    weight = float(input("please enter your weight in KG: "))
    person = BMI(height, weight)
    calculation = person.calc()

