from model.Function import Function
from model.FurnitureType import FurnitureType


class Tools():

    def __init__(self, name="", voltage=0, function=Function.CUTTING, producer="", price=0,
                 furniture_type=FurnitureType):
        self.name = name
        self.voltage = voltage
        self.function = function
        self.producer = producer
        self.price = price
        self.furniture_type = furniture_type

    def __del__(self):
        print("Destructor was called")

    def __str__(self):
        return str(self.__dict__)
