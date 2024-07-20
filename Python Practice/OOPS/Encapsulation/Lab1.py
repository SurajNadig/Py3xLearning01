# Encapsulation -
# bind the data variables with the methods
# Data Member - / Class Variables
# Methods - Def function within the class
# Wrapping or binding the data variables with the methods - Encapsulation.

# Hide the data members(class variables, instance variables) by using only the methods.

class Car:
    name = None

    def __init__(self):
        self.public_var = "public"
        self._protected_var = "protected123"
        self.__private_var = "pass@123"

    def __private_method(self):
        print("Protected!")

    def printName(self):
        # self.__private_method()
        if self.__private_var == "123":
            print("Hi, 123")
        print("I am allowed public")

# This is end of the class

alto = Car()
alto.printName()
# alto.__private_var

#Public can be acceessed anywhere
#Private can onlybe acceessed by the methods within class
#Protected can only be acceessed within the module..