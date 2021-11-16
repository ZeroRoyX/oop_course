from car import Car

class UberBlack(Car):
    car_type_accepted = []
    seats_material = []

    def __init__(self, license, driver, car_type_accepted, seats_material):
        super().__init__(license, driver)
        self.car_type_accepted = car_type_accepted
        self.seats_material = seats_material