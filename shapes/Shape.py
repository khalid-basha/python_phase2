from abc import ABCMeta, abstractmethod
import logging as log


log.basicConfig(format='%(asctime)s - %(message)s', level=log.INFO)

class Shape:

    __metaclass__ = ABCMeta
    def __init__ (self, shapeType, shapeId):
        self.shapeType = shapeType
        self.shapeId= int(shapeId)
        log.info("New shape: "+self.shapeType+ ". Shape ID: "+ str(self.shapeId))

    @abstractmethod
    def area(self) :
        pass

    @abstractmethod
    def perimeter (self):
        pass

    def __repr__(self):
        log.info("Shape of Type: "+self.shapeType + ". Shape ID: "+ str(self.shapeId))
        return ("Shape of Type: "+self.shapeType+ ". Shape ID: "+ str(self.shapeId))

    def __str__(self):
        log.info("Shape of Type: "+self.shapeType+ ". Shape ID: "+ str(self.shapeId))
        return ("Shape of Type: "+self.shapeType+ ". Shape ID: "+ str(self.shapeId))

    def __index__(self):
        return self.shapeId
