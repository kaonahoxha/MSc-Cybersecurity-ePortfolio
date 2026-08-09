from abc import ABC, abstractmethod


# Abstract product
class Car(ABC):
    @abstractmethod
    def drive(self):
        pass


# Concrete products
class Sedan(Car):
    def drive(self):
        return "Driving a Sedan."


class SUV(Car):
    def drive(self):
        return "Driving an SUV."


class Hatchback(Car):
    def drive(self):
        return "Driving a Hatchback."


# Abstract factory
class CarFactory(ABC):
    @abstractmethod
    def create_car(self):
        pass


# Concrete factories
class SedanFactory(CarFactory):
    def create_car(self):
        return Sedan()


class SUVFactory(CarFactory):
    def create_car(self):
        return SUV()


class HatchbackFactory(CarFactory):
    def create_car(self):
        return Hatchback()


# Client code
def demonstrate_car(factory):
    car = factory.create_car()
    print(car.drive())


# Demonstration
factories = [
    SedanFactory(),
    SUVFactory(),
    HatchbackFactory()
]

for factory in factories:
    demonstrate_car(factory)
