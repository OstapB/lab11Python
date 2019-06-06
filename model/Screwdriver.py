from model.Function import Function
from model.FurnitureType import FurnitureType
from model.Tools import Tools


class Screwdriver(Tools):
    def __init__(self, name="", voltage=0, function=Function, producer="", price=0,
                 furniture_type=FurnitureType, speed=0):
        super().__init__(name, voltage, function, producer, price, furniture_type)
        self.speed = speed

    def __str__(self):
        return "Screwdriver " + str(self.__dict__)
