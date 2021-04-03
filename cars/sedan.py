from .Car import Car, Standard, Fuel


class Sedan(Car):
    def __init__(self, standard_type: Standard, fuel: Fuel, weight: float = 0, color: str = "", volume: float = 0,
                 engine_capacity: float = 0, price: int = 0, number_of_wheels: int = 0,
                 vehicle_type: str = "", volume_of_trunk: int = 0):
        super().__init__(Standard.EURO_5, Fuel.DIESEL, weight, color, volume, engine_capacity,
                         price, number_of_wheels)
        self.standard_type = standard_type
        self.fuel = fuel
        self.vehicle_type = vehicle_type
        self.volume_of_trunk = volume_of_trunk

    def __str__(self):
        output = ("Weight: " + str(self.weight) + "\nColor: " + str(self.color) + "\nVolume: "
                  + str(self.volume) + "\nType Drive: " + str(self._standard_type)
                  + "\nEngine capacity: " + str(self.engine_capacity)
                  + "\nPrice($): " + str(self.price)
                  + "\nFuel: " + str(self.fuel)
                  + "\nNumber of wheels: " + str(self.number_of_wheels)
                  + "\nVehicle type: " + str(self.vehicle_type)
                  + "\nVolume of trunk: " + str(self.volume_of_trunk))
        return output
