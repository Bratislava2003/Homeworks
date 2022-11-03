from abc import ABC
from homework_02.exceptions import LowFuelError, NotEnoughFuel

class Vehicle(ABC):
    started = False
    weight = 0
    fuel = 0
    fuel_consumption = 0

    def __init__(self, weight, fuel, fuel_con):
        self.weight = weight
        self.fuel = fuel
        self.fuel_consumption = fuel_con

    def start(self):
        if self.started is False:
            if self.fuel > 0:
                self.started = True
            else:
                raise LowFuelError("No fuel to use vehicle!")

    def move(self, distance):
        if self.fuel // self.fuel_consumption < distance:
            raise NotEnoughFuel("Not enough fuel to go this far")
        else:
            self.fuel -= distance * self.fuel_consumption
