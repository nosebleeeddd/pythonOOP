# Temperature converter

class Temperature:
    def __init__(self, celcius, fahrenheit):
        self.celcius = celcius
        self.fahrenheit = fahrenheit

    def celtofah(self, celcius):
        self.fahrenheit = (self.celcius * (9/5)) + 32
        self.fahrenheit = round(self.fahrenheit, 2)
        return f"{self.celcius}C converted to Fahrenheit is {self.fahrenheit} degrees"

    def fahtocel(self, fahrenheit):
        self.celcius = (self.fahrenheit - 32) * (5/9)
        self.celicus = round(self.celcius, 2)
        return f"{self.fahrenheit}F converted to Celcius is {self.celcius} degrees"


def ready():
    redo = input("Press Enter to convert Temp, or Type 'quit to exit")
    if redo == 'quit':
        return False
    else:
        return True

start = ready()

while start:
    convert = int(input("Which conversion would you like to use?\n1) Celcius\n2) Fahrenheit\n"))
    if convert == 1:
        celcius = float(input("What temperature would you like to convert?"))
        temp = Temperature(celcius, 0)
        print(temp.celtofah(celcius))
    elif convert == 2:
        fahrenheit = float(input("What temperature would you like to convert?"))
        temp = Temperature(0, fahrenheit)
        print(temp.fahtocel(fahrenheit))
    else:
        print("Enter a valid number")
    start = ready()
