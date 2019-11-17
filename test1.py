'''Exercise 1: Object Oriented Programming'''
from math import pi

class Circle :
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return pi*(self.radius)**2
    def perimeter(self):
        return 2*pi*self.radius

# exemple
cercle=Circle(5)
print(cercle.perimeter())
print(cercle.area())
