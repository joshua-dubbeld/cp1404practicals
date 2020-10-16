from prac_08.car import Car
from random import randint


class UnreliableCar(Car):
    """Specialised version of Car that includes reliability"""

    def __init__(self, name, fuel, reliability):
        super().__init__(name, fuel)
        self.reliability = reliability

    def __str__(self):
        return "{}".format(super().__str__())

    def drive(self, distance):
        if randint(0, 100) > self.reliability:
            distance_driven = super().drive(distance)
            return distance_driven
