# Class Properties

# Class properties are used to define attributes that are shared across all
# instances of a class. They are defined using the @property decorator, and
# are accessed using the class name rather than an instance of the class.
# example of class properties in a class MyClass:

class PersonnalComputer:
    # class property
    _brand = 'Generic'
    _state = 'OFF'

    # getter method for brand
    @property
    def brand(cls) -> str:
        return cls._brand

    # setter method for brand
    @brand.setter
    def brand(cls, value: str) -> None:
        if not isinstance(value, str):
            raise ValueError('Brand must be a string')
        cls._brand = value

    # getter method for state
    @property
    def state(cls) -> str:
        return cls._state

    # setter method for state
    @state.setter
    def state(cls, value: str) -> None:
        if value not in ['ON', 'OFF']:
            raise ValueError('State must be ON or OFF')
        cls._state = value

    # method - adds functionality
    def turn_on(self) -> None:
        self.state = 'ON'
        print(f'{self.brand}: ON')

    # method
    def turn_off(self) -> None:
        self.state = 'OFF'
        print(f'{self.brand}: OFF')


# create an object of the class
pc1 = PersonnalComputer()
# call the method
pc1.turn_on()
pc1.turn_off()

# class properties are used to define attributes that are shared across all
# instances of a class. They are defined using the @property decorator, and
# are accessed using the class name rather than an instance of the class. They
# are useful for defining attributes that are common to all instances of a
# class, such as a default value or a constant. They can also be used to
# define attributes that are computed based on other attributes of the class.

# The examples used in this program are creating a personal computer object and
# turning it on and off.
