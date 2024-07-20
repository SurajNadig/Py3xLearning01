class Car:
    def __init__(self, brand, color):
        self.brand = brand
        self.color = color

    def start_engine(self):
        print("Engine started!")

    def drive(self):
        print(f"Driving the {self.color} {self.brand} car.")


my_car = Car("Toyota", "blue")
my_car.start_engine()
