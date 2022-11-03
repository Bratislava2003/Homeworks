from homework_02.base import Vehicle
from homework_02.engine import Engine

class Car(Vehicle):

    engine = None

    def set_engine(self, client: Engine):
        if not isinstance(client, Engine):
            raise TypeError("Not an 'engine' object!")
        self.engine = client

# v6 = Engine(10, 6)
# mazda = Car()
# mazda.set_engine(v6)
# print(mazda.motor)
