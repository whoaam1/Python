from .truck import Truck
from .Car import Standard, Fuel


class Daf(Truck):
    def __init__(self, weight: float = 0, color: str = "", volume: float = 0,
                 engine_capacity: float = 0, price: int = 0, number_of_wheels: int = 0,
                 type_of_trailer: str = "", type_of_trucks: str = "", torque: int = 0, top_speed: int = 0):
        super().__init__(Standard.EURO_5, Fuel.GAS, weight, color, volume, engine_capacity, price,
                         number_of_wheels, type_of_trailer, type_of_trucks)
        self.torque = torque
        self.top_speed = top_speed

    def __str__(self):
        output = ("Weight: " + str(self.weight) + "\nColor: " + str(self.color) + "\nVolume: "
                  + str(self.volume) + "\nStandard type: " + str(self._standard_type)
                  + "\nEngine capacity: " + str(self.engine_capacity)
                  + "\nPrice($): " + str(self.price)
                  + "\nFuel: " + str(self.fuel)
                  + "\nNumber of wheels: " + str(self.number_of_wheels)
                  + "\nType of trailer: " + str(self.type_of_trailer)
                  + "\nType of trucks: " + str(self.type_of_trucks)
                  + "\nTorque: " + str(self.torque)
                  + "\nTop speed: " + str(self.top_speed) + "\n")
        return output
