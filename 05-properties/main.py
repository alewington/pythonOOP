# Properties

# Properties are used to control access to the attributes of a class. They
# allow you to define getter and setter methods for an attribute, which
# can be used to control how the attribute is accessed and modified.
# Properties are defined using the @property decorator, which is used to
# define a getter method for an attribute. The setter method is defined
# using the @<attribute>.setter decorator, which is used to define a setter
# method for an attribute. Properties are used to control access to the
# attributes of a class, and can be used to add validation logic.

# example of properties in a class
class PersonnalComputer:
    # initialiser
    def __init__(self, brand: str) -> None:
        self._brand = brand
        self._state = 'OFF'

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
