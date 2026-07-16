# classes

# written in pascal case for class names

# class
class PersonnalComputer:
    # initialiser
    def __init__(self, brand: str) -> None:
        self.brand = brand
        self.state = 'OFF'

    # method - adds functionality
    def turn_on(self) -> None:
        self.state = 'ON'
        print(f'{self.brand}: ON')

    # method
    def turn_off(self) -> None:
        self.state = 'OFF'
        print(f'{self.brand}: OFF')

# What are classes?
# Classes are blueprints for objects.

# What are objects?
# Objects are instances of a class.

# What is an instance variable?
# Instance variables are variables that belong to the object itself.
# It's not shared between other objects.

# What is a method?
# Methods are functions that belong to an object.
# They can be used to change the state of the object.
