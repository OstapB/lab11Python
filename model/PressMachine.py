from model.Function import Function
from model.FurnitureType import FurnitureType
from model.Tools import Tools


class PressMachine(Tools):
    def __init__(self, name="", voltage=0, function=Function, producer="", price=0,
                 furniture_type=FurnitureType, power=0):
        super().__init__(name, voltage, function, producer, price, furniture_type)
        self.speed = power

    def __str__(self):
        return "PressMachine" + str(self.__dict__)
