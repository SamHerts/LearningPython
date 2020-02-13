"""
    Your task is to create a Circle constructor that creates a circle with a radius provided 
    by an argument. The circles constructed must have two getters getArea() (PIr^2) 
    and getPerimeter() (2PI*r) which give both respective areas and perimeter (circumference).
"""
from math import pi
class Circle:
    def __init__(self, radius=0):
        self.radius = radius
    
    def getArea(self):
        return pi*self.radius**2
    def getPerimeter(self):
        return 2*pi*self.radius

circy = Circle(11)
print (circy.getArea())