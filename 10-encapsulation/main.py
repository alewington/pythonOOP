# Encapsulation

# Encapsulation is the practice of restricting access to certain attributes
# and methods of an object, typically by making them private (using a
# leading underscore) and providing public getter and setter methods to
# control access and modification.

# example of encapsulation in a class
class PersonnalComputer:
    # initialiser
    def __init__(self, brand: str) -> None:
        self._brand = brand  # private attribute
        self._state = 'OFF'  # private attribute

    # getter method for brand
    @property
    def brand(self) -> str:
        return self._brand

    # setter method for brand
    @brand.setter
    def brand(self, value: str) -> None:
        if not isinstance(value, str):
            raise ValueError('Brand must be a string')
        self._brand = value

    # getter method for state
    @property
    def state(self) -> str:
        return self._state

    # setter method for state
    @state.setter
    def state(self, value: str) -> None:
        if value not in ['ON', 'OFF']:
            raise ValueError('State must be ON or OFF')
        self._state = value

    # method - adds functionality
    def turn_on(self) -> None:
        self.state = 'ON'
        print(f'{self.brand}: ON')

    # method
    def turn_off(self) -> None:
        self.state = 'OFF'
        print(f'{self.brand}: OFF')


# create an object of the class
pc1 = PersonnalComputer('Dell')
# call the method
pc1.turn_on()
pc1.turn_off()

# Encapsulation is the practice of restricting access to certain attributes
# and methods of an object, typically by making them private (using a
# leading underscore) and providing public getter and setter methods to
# control access and modification. It is used to protect the internal state
# of an object and prevent unintended interference from outside code. It is a
# fundamental principle of object-oriented programming and helps to create a
# clear separation between the internal implementation of a class and the
# external interface that it exposes to other code.

# Examples of this in this code are the private attributes _brand and _state,
# which are not directly accessible from outside the class. Instead, public
# getter and setter methods are provided to access and modify these attributes
# in a controlled manner. This allows for validation and encapsulation of the
# internal state of the object.

# For example, the setter method for state ensures that only valid values
# ('ON' or 'OFF') can be assigned to the _state attribute, preventing invalid
# states from being set.
