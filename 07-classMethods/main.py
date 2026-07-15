# Class Methods

# Class methods are used to define methods that are bound to the class rather
# than an instance of the class. They are defined using the @classmethod
# decorator, and the first parameter is always cls, which refers to the
# class itself.

# example of class methods in a class MyClass:
class PersonnalComputer:
    # class property
    _brand = 'Generic'
    _state = 'OFF'

    # class method to get brand
    @classmethod
    def get_brand(cls) -> str:
        return cls._brand

    # class method to set brand
    @classmethod
    def set_brand(cls, value: str) -> None:
        if not isinstance(value, str):
            raise ValueError('Brand must be a string')
        cls._brand = value

    # class method to get state
    @classmethod
    def get_state(cls) -> str:
        return cls._state

    # class method to set state
    @classmethod
    def set_state(cls, value: str) -> None:
        if value not in ['ON', 'OFF']:
            raise ValueError('State must be ON or OFF')
        cls._state = value

# method - adds functionality
    def turn_on(self) -> None:
        self.set_state('ON')
        print(f'{self.get_brand()}: ON')

# method
    def turn_off(self) -> None:
        self.set_state('OFF')
        print(f'{self.get_brand()}: OFF')


# create an object of the class
pc1 = PersonnalComputer()
# call the method
pc1.turn_on()
pc1.turn_off()

# Class methods are used to define methods that are bound to the class rather
# than an instance of the class. They are defined using the @classmethod
# decorator, and the first parameter is always cls, which refers to the
# class itself. They are useful for defining methods that operate on
# class-level data, such as class properties or class-level constants.
# They can also be used to define factory methods that create instances of the
# class. They can be called using the class name or an instance of the class.
# They can also be used to define methods that operate on class-level data,
# such as class properties or class-level constants.

# The examples of class methods used in this program are creating a personal
# computer object and calling the turn_on and turn_off methods. The class
# methods get_brand, set_brand, get_state, and set_state are used to get and
# set the class properties _brand and _state.
