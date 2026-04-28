class WeightConverter():
    def __init__(self, pound, conversion):
        self.pound = pound
        self.conversion = conversion

    def kg(self, pound):
        kg = self.pound * 0.45
        return str(kg)

    def stone(self, pound):
        stone = self.pound * 0.07
        return str(stone)

    def ounce(self, pound):
        ounce = self.pound * 16
        return str(ounce)

    def logic(self):
        if self.conversion == 1:
            print(f"{self.pound} lbs converted to KG is: {self.kg(self.pound)} KG")
        elif self.conversion == 2:
            print(f"{self.pound} lbs converted to Stone is: {self.stone(self.pound)} Stone")
        elif self.conversion == 3:
            print(f"{self.pound} lbs converted to Ounces is: {self.ounce(self.pound)} Ounce")
        else:
            print("please choose a valid operator")


def retry():
    redo = input("Would you like to convert. Type 'quit' to exit: ")
    if redo == 'quit':
        return False
    else:
        return True

while retry():
    pound = int(input("Please enter how much your item weighs in lbs: "))
    convert = int(input("Please choose a weight you wish to convert to \n1) KG\n2) Stone\n3) Ounces\n"))
    converter = WeightConverter(pound, convert)
    converter.logic()

