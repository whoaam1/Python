from .Car import Car, Standard, Fuel


class Truck(Car):
    def __init__(self, standard_type: Standard, fuel: Fuel, weight: float = 0, color: str = "", volume: float = 0,
                 engine_capacity: float = 0, price: int = 0, number_of_wheels: int = 0,
                 type_of_trailer: str = "", type_of_trucks: str = ""):
        super().__init__(Standard.EURO_5, Fuel.GAS, weight, color, volume, engine_capacity,
                         price, number_of_wheels)
        self.standard_type = standard_type
        self.fuel = fuel
        self.type_of_trailer = type_of_trailer
        self.type_of_trucks = type_of_trucks

    def __str__(self):
        output = ("Weight: " + str(self.weight) + "\nColor: " + str(self.color) + "\nVolume: "
                  + str(self.volume) + "\nType Drive: " + str(self._standard_type)
                  + "\nEngine capacity: " + str(self.engine_capacity)
                  + "\nPrice($): " + str(self.price)
                  + "\nFuel: " + str(self.fuel)
                  + "\nNumber of wheels: " + str(self.number_of_wheels)
                  + "\nType of trailer: " + str(self.type_of_trailer)
                  + "\nType of trucks: " + str(self.type_of_trucks))
        return output
