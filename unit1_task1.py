class Vehicle:
    def __init__(self, brand, fuel_type):
        self.brand = brand
        self.fuel_type = fuel_type

class Car(Vehicle):
    def __init__(self, brand, fuel_type, num_doors):
        super().__init__(brand, fuel_type)
        self.num_doors = num_doors

my_car = Car("BMW", "Petrol", 4)
print(my_car.brand)
print(my_car.fuel_type)
print(my_car.num_doors)
