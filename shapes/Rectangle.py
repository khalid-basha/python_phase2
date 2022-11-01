import Shape
import logging as log

log.basicConfig(format='%(asctime)s - %(message)s', level=log.INFO)

class Rectangle(Shape):
    def __init__(self, id, length=0, breadth=0):
        Shape.__init__(self, "Rectangle", id)
        self.length = length
        self.breadth = breadth
        log.info("New Rectangle ["+str(self.length)+ ", "+ str(self.breadth)+'].')

    def area(self):
        return self.length*self.breadth

    def perimeter (self):
        return 2 * (self.lenght + self.breadth)

    def __call__(self,lenght,breadth):
        self.breadth=breadth
        self.lenght=lenght

if __name__== 'main':
    r= Rectangle(1,5,3)
