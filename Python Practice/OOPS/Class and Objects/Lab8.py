class car:
    Color = None
    Model = None
    Price = None

    def __init__(self, car_Color, car_Model, car_Price):
        self.Color = car_Color
        self.Model = car_Model
        self.Price = car_Price

    def details(self):
        print("Car Color is ", self.Color)
        print("Car Model is ", self.Model)
        print("Car price is ", self.Price)


BMW = car("Black","1987","2 Crore")
Audi = car("Red","1999","1.5 Crore")
BMW.details()
Audi.details()
# print(BMW.details()) #None will print along with details of car