# Polymorphism

# Polymorphism allows objects of different classes to be treated as objects of
# a common superclass.
# It promotes flexibility and code reusability by enabling a single interface
# to represent different types of objects.

# example of polymorphism in a class
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


class Desktop(Computer):
    def __init__(self, brand: str, has_dedicated_gpu: bool) -> None:
        super().__init__(brand)  # Call the parent class's initializer
        self.has_dedicated_gpu = has_dedicated_gpu

    def check_gpu(self) -> None:
        if self.has_dedicated_gpu:
            gpu_status = "has a dedicated GPU"
        else:
            gpu_status = "does not have a dedicated GPU"
        print(f'{self.brand} {gpu_status}')


# create objects of the child classes
laptop1 = Laptop('Dell', 10)
desktop1 = Desktop('HP', True)

# demonstrate polymorphism
for computer in (laptop1, desktop1):
    computer.turn_on()
    computer.turn_off()


# This demonstrates how both Laptop and Desktop classes can be treated as
# objects of the Computer class, allowing for a unified interface to interact
# with different types of computers. The turn_on and turn_off methods are
# called on both objects, showcasing polymorphism in action.
