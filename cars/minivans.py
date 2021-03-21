from .Car import Car, Standard, Fuel


class Minivans(Car):
    def __init__(self, standard_type: Standard, fuel: Fuel, weight: float = 0, color: str = "", volume: float = 0,
                 engine_capacity: float = 0, price: int = 0, number_of_wheels: int = 0,
                 number_of_rows: int = 0, volume_of_trunk: int = 0):
        super().__init__(Standard.EURO_6, Fuel.GASOLINE, weight, color, volume, engine_capacity,
                         price, number_of_wheels)
        self.standard_type = standard_type
        self.fuel = fuel
        self.number_of_rows = number_of_rows
        self.volume_of_trunk = volume_of_trunk

    def __str__(self):
        output = ("Weight: " + str(self.weight) + "\nColor: " + str(self.color) + "\nVolume: "
                  + str(self.volume) + "\nType Drive: " + str(self._standard_type)
                  + "\nEngine capacity: " + str(self.engine_capacity)
                  + "\nPrice($): " + str(self.price)
                  + "\nFuel: " + str(self.fuel)
                  + "\nNumber of wheels: " + str(self.number_of_wheels)
                  + "\nNumber of rows: " + str(self.number_of_rows)
                  + "\nVolume of trunk: " + str(self.volume_of_trunk))
        return output
