class dog():
    name=None
    id=None
    def __init__(self,dog_name,dog_id):
        self.name=dog_name
        self.id=dog_id
    def play(self):
        print("Is playing ")

    def sing(self):
        print(f"Who is singing - {self.name}")
#
# dog1=dog()
# dog1.name="Chow Chow"
# print(dog1.name)
#
# dog2=dog()
# dog2.name="Mow Mow"
# print(dog2.name)
#Instead of assigning names everytime , we use constructor

dog1=dog("Chow","2")
dog2=dog("Mow","4")
print(f"{dog1.name} has Id {dog1.id}")
print(f"{dog2.name} has Id {dog2.id}")
dog1.sing()
dog2.sing()