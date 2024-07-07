class myclass():
    def __init__(self):
        self.name = "Suraj"
        self.__address = "Jayanagar"

    def public_func(self):  # Public
        print("Hi, I am public function")

    def __private_func(self):  # Private bcz it starts with __
        print("I am Private function and i can only access me via a another method in same class")

    def privateInPublic(self):
        self.__private_func()
        print(self.__address) # Private fucntion leaked by public function


RCB = myclass()
RCB.public_func()
RCB.privateInPublic()
