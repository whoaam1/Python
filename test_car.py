
import unittest

from cars import *


class CarManagerTest(unittest.TestCase):

    def setUp(self):
        self.bmw = Bmw()
        self.daf = Daf()
        self.mercedes = Mercedes()
        self.manager = CarManager()
        self.manager.add_vehicle(self.daf)
        self.manager.add_vehicle(self.mercedes)
        self.manager.add_vehicle(self.bmw)

    def test_find_by_standard_EURO_5(self):
        expected_vehicles = [self.daf, self.bmw]

        result = self.manager.find_by_standard(Standard.EURO_5)
        self.assertNotIn(self.mercedes, result)
        self.assertEqual(result, expected_vehicles)

    def test_find_by_standard_EURO_6(self):
        expected_vehicles = [self.mercedes]

        result = self.manager.find_by_standard(Standard.EURO_6)
        self.assertIn(self.mercedes, result)
        self.assertEqual(result, expected_vehicles)

    def test_sort_by_price(self):
        expected_vehicle = [self.bmw, self.daf, self.mercedes]

        result = self.manager.sort_by_price(vehicles=expected_vehicle)

        self.assertEqual(result, sorted(expected_vehicle, key=lambda s: s.price))

    def test_sort_by_volume(self):
        expected_vehicle = [self.bmw, self.daf, self.mercedes]

        result = self.manager.sort_by_volume(vehicles=expected_vehicle)

        self.assertEqual(result, sorted(expected_vehicle, key=lambda s: s.volume))


class CarTest(unittest.TestCase):

    def setUp(self):
        self.bmw = Bmw()
        self.daf = Daf()
        self.mercedes = Mercedes()

    def test_bmw(self):
        expected_vehicle = Bmw(2500.2, "Black", 3.0, 2993.5, 45000, 4, "Sedan", 419, "M5", "Hydraulic")

        self.assertEqual(expected_vehicle.weight, 2500.2)
        self.assertEqual(expected_vehicle.color, "Black")
        self.assertEqual(expected_vehicle.volume, 3.0)
        self.assertEqual(expected_vehicle.engine_capacity, 2993.5)
        self.assertEqual(expected_vehicle.price, 45000)
        self.assertEqual(expected_vehicle.number_of_wheels, 4)
        self.assertEqual(expected_vehicle.vehicle_type, "Sedan")
        self.assertEqual(expected_vehicle.volume_of_trunk, 419)
        self.assertEqual(expected_vehicle.sport_series, "M5")
        self.assertEqual(expected_vehicle.type_of_brakes, "Hydraulic")

    def test_daf(self):
        expected_vehicle = Daf(4500.5, "Silver", 2.0, 1150.1, 36000, 8, "On-board", "Truck", 3, 70)

        self.assertEqual(expected_vehicle.weight, 4500.5)
        self.assertEqual(expected_vehicle.color, "Silver")
        self.assertEqual(expected_vehicle.volume, 2.0)
        self.assertEqual(expected_vehicle.engine_capacity, 1150.1)
        self.assertEqual(expected_vehicle.price, 36000)
        self.assertEqual(expected_vehicle.number_of_wheels, 8)
        self.assertEqual(expected_vehicle.type_of_trailer, "On-board")
        self.assertEqual(expected_vehicle.type_of_trucks, "Truck")
        self.assertEqual(expected_vehicle.torque, 3)
        self.assertEqual(expected_vehicle.top_speed, 70)

    def test_mercedes(self):
        expected_vehicle = Mercedes(3500.7, "White", 2.3, 1555.3, 25000, 4, 3, 550, "AMG", 31)

        self.assertEqual(expected_vehicle.weight, 3500.7)
        self.assertEqual(expected_vehicle.color, "White")
        self.assertEqual(expected_vehicle.volume, 2.3)
        self.assertEqual(expected_vehicle.engine_capacity, 1555.3)
        self.assertEqual(expected_vehicle.price, 25000)
        self.assertEqual(expected_vehicle.number_of_wheels, 4)
        self.assertEqual(expected_vehicle.number_of_rows, 3)
        self.assertEqual(expected_vehicle.volume_of_trunk, 550)
        self.assertEqual(expected_vehicle.sport_series, "AMG")
        self.assertEqual(expected_vehicle.clearance, 31)


if __name__ == '__main__':
    unittest.main()
