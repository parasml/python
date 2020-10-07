from abc import ABC, abstractmethod

class shape(ABC):
    
    
    @abstractmethod
    def Area():
        print("Inside Area function")

class Rectangle(shape):

    def Area(self):
        print("Inside PrintArea")


class smallRectangle(Rectangle):

    def Area(self):
        print("Inside SMAll PrintArea")

# ---------------------------------

oRectangle = Rectangle()
oRectangle.Area()

osmallRectangle = smallRectangle()
osmallRectangle.Area()