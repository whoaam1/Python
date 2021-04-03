from enum import Enum, auto


class Standard(Enum):
    EURO_5 = auto()
    EURO_6 = auto()


class Fuel(Enum):
    DIESEL = auto()
    GAS = auto()
    GASOLINE = auto()


class Car:
    def __init__(self, _standard_type: Standard, fuel: Fuel, weight: float = 0, color: str = "", volume: float = 0,
                 engine_capacity: float = 0, price: int = 0, number_of_wheels: int = 0):
        self.weight = weight
        self.color = color
        self.volume = volume
        self._standard_type = _standard_type
        self.engine_capacity = engine_capacity
        self.price = price
        self.fuel = fuel
        self.number_of_wheels = number_of_wheels

    def __str__(self):
        output = ("Weight: " + str(self.weight) + "\nColor: " + str(self.color) + "\nVolume: "
                  + str(self.volume) + "\nType Drive: " + str(self._standard_type)
                  + "\nEngine capacity: " + str(self.engine_capacity)
                  + "\nPrice($): " + str(self.price)
                  + "\nFuel: " + str(self.fuel)
                  + "\nNumber of wheels: " + str(self.number_of_wheels))
        return output

    def get_type(self):
        return self._standard_type
