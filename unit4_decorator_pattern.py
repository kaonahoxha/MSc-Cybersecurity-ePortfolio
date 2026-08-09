from abc import ABC, abstractmethod


class Coffee(ABC):
    @abstractmethod
    def get_description(self):
        pass

    @abstractmethod
    def get_cost(self):
        pass


class BasicCoffee(Coffee):
    def get_description(self):
        return "Basic Coffee"

    def get_cost(self):
        return 2.00


class CoffeeDecorator(Coffee):
    def __init__(self, coffee):
        self.coffee = coffee


class MilkDecorator(CoffeeDecorator):
    def get_description(self):
        return self.coffee.get_description() + ", Milk"

    def get_cost(self):
        return self.coffee.get_cost() + 0.50


class SugarDecorator(CoffeeDecorator):
    def get_description(self):
        return self.coffee.get_description() + ", Sugar"

    def get_cost(self):
        return self.coffee.get_cost() + 0.20


# Create a basic coffee
coffee = BasicCoffee()

# Dynamically add milk
coffee = MilkDecorator(coffee)

# Dynamically add sugar
coffee = SugarDecorator(coffee)

print("Order:", coffee.get_description())
print(f"Total price: £{coffee.get_cost():.2f}")
