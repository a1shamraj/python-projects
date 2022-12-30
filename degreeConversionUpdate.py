# Amy Shamraj
# INF 308

# Project Description:
# Degree Conversion calucator has been updated with a start menu which allows for conversion of both types of degrees.
# It also includes serveral useful tools such as functions, tuples, etc. which improve upon code readability and reuseability.
# There is also a substantial improvement in overall functionality and efficiency which furthermore promotes good programming practices.

menu = False  # defined menu variable to false

class Conversions: # parent class
    def __init__(self, type): # instantiate
        self.type = type # type string

    def get_type(self): # get type string
        return self.type
    
class ftoc(Conversions): # child class 
    def convert(self):  # function defined for Fahrenheit to Celsius conversion
    # int for number input
        Fahrenheit = int(input("Please enter the temperature in Fahrenheit. "))
    # returns a tuple of Fahrenheit and the conversion
        return Fahrenheit, (Fahrenheit - 32) * (5/9)

class ctof(Conversions): # child class 
    def convert(self):  # function defined for Celisus to Fahrenheit conversion
    # int for number input
        Celsius = int(input("Please enter the temperature in Celsius. "))
    # returns a tuple of Celsius and the conversion
        return Celsius, ((Celsius * (9/5)) + 32)


while menu != True:  # loop for menu to return and try different conversions
    ConversionType = input(
        "Please select a conversion type. \n 1 = F to C \n 2 = C to F \n 3 = Quit \nAnswer: ")  # menu

    if ConversionType == "1":
        fartocel = Conversions("Fahrenheit to Celsius Conversion") # type = string
        print(fartocel.get_type()) # print string
        # set tuple of Fahrenheit and Celsius equal to appropraite conversion function
        Fahrenheit, Celsius = ftoc.convert(fartocel) # tuple is equal to function from child class
        print(Fahrenheit, "Fahrenheit in Celsius is", Celsius)

    elif ConversionType == "2":
        celtofar = Conversions("Celsius to Fahrenheit Conversion") # type = string
        print(celtofar.get_type()) # print string
        # set tuple of Celsius and Fahrenheit equal to appropriate conversion function
        Celsius, Fahrenheit = ctof.convert(celtofar) # tuple is equal to function from child class
        print(Celsius, "Celsius in Fahrenheit is", Fahrenheit)

    elif ConversionType == "3":
        break  # exit menu loop

    else:
        print("Invalid choice! ")  # exception for unexpected answer
