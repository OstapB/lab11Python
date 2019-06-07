from manager.ToolsManager import ToolsManager
from model.Function import Function
from model.FurnitureType import FurnitureType
from model.HammerMachine import HammerMachine
from model.PressMachine import PressMachine
from model.Screwdriver import Screwdriver


def main():
    tools_hammer_machine = HammerMachine("Hummer", 100, Function.CUTTING, "Ukraine", 2500, FurnitureType.IRON, 2000, 10)
    tools_press_machine = PressMachine("Hulk", 210, Function.FASTENING, "Italy", 1500, FurnitureType.IRON, 200)
    tools_screwdriver = Screwdriver("Flash", 220, Function.CUTTING, "Germany", 1000, FurnitureType.WOODEN, 300)

    list_tools = [tools_hammer_machine, tools_press_machine, tools_screwdriver]

    manager = ToolsManager(list_tools)

    manager.print_tools(manager.sort_by_voltage(list_tools))
    manager.print_tools(manager.sort_by_producer(list_tools))
    manager.print_tools(manager.find_by_furniture_type(FurnitureType.WOODEN))
    return list_tools


main()
