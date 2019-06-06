from model.Function import Function
from model.FurnitureType import FurnitureType
from model.Tools import Tools


class HammerMachine(Tools):
    def __init__(self, name="", voltage=0, function=Function, producer="", price=0,
                 furniture_type=FurnitureType, weight=0, temperature=0):
        super().__init__(name, voltage, function, producer, price, furniture_type)
        self.weight = weight
        self.temperature = temperature

    def __str__(self):
        return "HammerMachine" + str(self.__dict__)
