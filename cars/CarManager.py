from typing import List
from .Car import Car, Standard


class CarManager:
    def __init__(self):
        self.vehicles = []

    def add_vehicle(self, vehicle: Car):
        self.vehicles.append(vehicle)

    def add_vehicles(self, vehicles: List[Car]):
        self.vehicles += vehicles

    def sort_by_price(self, reverse: bool = False, vehicles: List[Car] = None):
        return sorted(vehicles if vehicles else self.vehicles, key=lambda s: s.price, reverse=reverse)

    def sort_by_volume(self, reverse: bool = False, vehicles: List[Car] = None):
        return sorted(vehicles if vehicles else self.vehicles, key=lambda s: s.volume, reverse=reverse)

    def find_by_standard(self, standard_type: Standard):
        return [vehicles for vehicles in self.vehicles if vehicles.get_type() == standard_type]
