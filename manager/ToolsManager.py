from model.FurnitureType import FurnitureType


class ToolsManager:
    def __init__(self, list_tools=None):
        self.list_tools = list_tools

    def find_by_furniture_type(self, furniture_type):
        return list(filter(lambda tools: tools.furniture_type == FurnitureType.IRON, self.list_tools))

    def sort_by_voltage(self, voltage, reverse=False):
        return sorted(self.list_tools, key=lambda tools: tools.voltage, reverse=reverse)

    def sort_by_producer(self, price, reverse=True):
        return sorted(self.list_tools, key=lambda tools: tools.price, reverse=reverse)

    def print_tools(self, tools):
        for item in tools:
            print(item)
