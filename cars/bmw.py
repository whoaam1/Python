from .sedan import Sedan
from .Car import Standard, Fuel


class Bmw(Sedan):
    def __init__(self, weight: float = 0, color: str = "", volume: float = 0,
                 engine_capacity: float = 0, price: int = 0, number_of_wheels: int = 0,
                 vehicle_type: str = "", volume_of_trunk: int = 0, sport_series: str = "", type_of_brakes: str = ""):
        super().__init__(Standard.EURO_5, Fuel.DIESEL, weight, color, volume, engine_capacity, price,
                         number_of_wheels, vehicle_type, volume_of_trunk)
        self.sport_series = sport_series
        self.type_of_brakes = type_of_brakes

    def __str__(self):
        output = ("Weight: " + str(self.weight) + "\nColor: " + str(self.color) + "\nVolume: "
                  + str(self.volume) + "\nStandard type: " + str(self._standard_type)
                  + "\nEngine capacity: " + str(self.engine_capacity)
                  + "\nPrice($): " + str(self.price)
                  + "\nFuel: " + str(self.fuel)
                  + "\nNumber of wheels: " + str(self.number_of_wheels)
                  + "\nVehicle type: " + str(self.vehicle_type)
                  + "\nVolume of trunk: " + str(self.volume_of_trunk)
                  + "\nSport series: " + str(self.sport_series)
                  + "\nType of brakes: " + str(self.type_of_brakes) + "\n")
        return output
