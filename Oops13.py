from abc import ABCMeta, abstractmethod


# Abstract Base Class & @abstractmethod
class Shape(metaclass=ABCMeta):
    @abstractmethod
    def print_area(self):
        return 0


class Rectangle(Shape):
    type = "Rectangle"
    sides = 4

    def __init__(self):
        self.length = int(input("Enter Rectangle Length : "))
        self.breadth = int(input("Enter Rectangle breadth : "))

    def print_area(self):
        return self.length * self.breadth


rect1 = Rectangle()

print(rect1.print_area())
