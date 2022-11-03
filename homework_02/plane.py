from homework_02.base import Vehicle
from homework_02.exceptions import CargoOverload

class Plane(Vehicle):
    cargo = 0
    max_cargo = 0

    def __init__(self, weight, fuel, fuel_consumption, max_cargo):
        # super().__init__(weight, fuel, fuel_con)
        self.weight = weight
        self.fuel = fuel
        self.fuel_consumption = fuel_consumption
        self.max_cargo = max_cargo

    def load_cargo(self, cargo_amount):
        if self.cargo + cargo_amount > self.max_cargo:
            raise CargoOverload("BRUH U DESTROYED A $7MIL PLANE")
        else:
            self.cargo += cargo_amount

    def remove_all_cargo(self):
        removed_cargo = self.cargo
        self.cargo = 0
        return removed_cargo
