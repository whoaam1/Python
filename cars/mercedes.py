from .minivans import Minivans
from .Car import Standard, Fuel


class Mercedes(Minivans):
    def __init__(self, weight: float = 0, color: str = "", volume: float = 0, engine_capacity: float = 0,
                 price: int = 0, number_of_wheels: int = 0, number_of_rows: int = 0,
                 volume_of_trunk: int = 0, sport_series: str = "", clearance: int = 0):
        super().__init__(Standard.EURO_6, Fuel.GASOLINE, weight, color, volume, engine_capacity, price,
                         number_of_wheels, number_of_rows, volume_of_trunk)
        self.sport_series = sport_series
        self.clearance = clearance

    def __str__(self):
        output = ("Weight: " + str(self.weight) + "\nColor: " + str(self.color) + "\nVolume: "
                  + str(self.volume) + "\nStandard type: " + str(self._standard_type)
                  + "\nEngine capacity: " + str(self.engine_capacity)
                  + "\nPrice($): " + str(self.price)
                  + "\nFuel: " + str(self.fuel)
                  + "\nNumber of wheels: " + str(self.number_of_wheels)
                  + "\nNumber of rows: " + str(self.number_of_rows)
                  + "\nVolume of trunk: " + str(self.volume_of_trunk)
                  + "\nSport series: " + str(self.sport_series)
                  + "\nClearance: " + str(self.clearance) + "\n")
        return output
