# Inheritance

# Inheritance allows a class (child class) to inherit attributes and methods
# from another class (parent class). It promotes code reusability and
# establishes a natural hierarchy between classes.

# example of inheritance in a class
class Computer:
    def __init__(self, brand: str) -> None:
        self.brand = brand
        self.state = 'OFF'

    def turn_on(self) -> None:
        self.state = 'ON'
        print(f'{self.brand}: ON')

    def turn_off(self) -> None:
        self.state = 'OFF'
        print(f'{self.brand}: OFF')


class Laptop(Computer):
    def __init__(self, brand: str, battery_life: int) -> None:
        super().__init__(brand)  # Call the parent class's initializer
        self.battery_life = battery_life

    def check_battery(self) -> None:
        print(f'{self.brand} battery life: {self.battery_life} hours')


# create an object of the child class
laptop1 = Laptop('Dell', 10)
# call the methods from both parent and child classes
laptop1.turn_on()
laptop1.check_battery()
laptop1.turn_off()

# This demonstrates how the Laptop class inherits methods from the Computer
# class while adding its own functionality.

# Examples of inheritance can be found in many real-world scenarios, such as
# vehicles, where a base class Vehicle can have derived classes like Car,
# Bike, and Truck, each with their own specific attributes and methods,
# while still sharing common functionality.

# Examples used in this example of inheritance are computers to laptops,
# where a base class Computer can have derived classes like Laptop, Desktop,
# and Tablet, each with their own specific attributes and methods, while
# still sharing common functionality.
