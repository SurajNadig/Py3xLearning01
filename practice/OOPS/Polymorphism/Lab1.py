# Polymorphism
# Polymorphism allows objects of different classes to be treated as objects of a common superclass.

# Pramod -> Mentor, Husband, Brother.
# Object -Method -> Mother, Matenal She is, sister, parent -

# Method Overriding - Same name in the parent and child
# child always override the parent functions


class shape:
    def area(self):
        print("Area of the shape")


class Rectangle(shape):
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def area(self):
        return self.length * self.breadth


class Circle(shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius


shape1 = Rectangle(6, 8)
print("Area of Rectangle is ", shape1.area())

shape2 = Circle(7)
print("Area of Circle is ", shape2.area())

shape3 = shape()
shape3.area()
