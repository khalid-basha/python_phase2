from .Shape import Shape
import math
import logging as log
log.basicConfig(format='%(asctime)s - %(message)s', level=log.INFO)

class Circle(Shape):
    def __init__(self, id, radius=0):
        Shape.__init__(self,"Circle",id)
        self.radius = abs(radius)
        log.info("New Circle ["+str(self.radius)+'].')

    def area(self):
        return round((self.radius**2) *math.pi,2)

    def perimeter(self):
        return round(2 * math.pi * self.radius,2)

    def __call__(self,radius):
        self.radius=abs(radius)
