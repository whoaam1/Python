from cars import CarManager
from cars import Standard, Bmw, Daf, Mercedes


def main():
    vehicle = CarManager()
    vehicle.add_vehicles([
        Bmw(2500.2, "Black", 3.0, 2993.5, 45000, 4, "Sedan", 419, "M5", "Hydraulic"),
        Daf(4500.5, "Silver", 2.0, 1150.1, 36000, 8, "On-board", "Truck", 3, 70),
        Mercedes(3500.7, "White", 2.3, 1555.3, 25000, 4, 3, 550, "AMG", 31)
    ])

    print('  Sorted by price\n\n' + '\n'.join([str(x) for x in vehicle.sort_by_price(True)]), '\n')
    print('  Sorted by volume:\n\n' + '\n'.join([str(x) for x in vehicle.sort_by_volume()]), '\n')
    print('  Find for Standard:\n\n' +
          '\n'.join([str(x) for x in vehicle.sort_by_volume(False, vehicle.find_by_standard(Standard.EURO_5))]), '\n')


class CarTest:
    def __init__(self):
        pass


if __name__ == '__main__':
    test = CarTest()
    main()
