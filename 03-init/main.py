# init

# initialiser, the init method is a special method that is called when an
# object is created. it is used to initialise the object's state.
# tell me more about the init method, it is a special method that is called
# when an object is created. It is used to initialise the object's state.
# It is called automatically when an object is created. It is defined using
# the __init__ method. It takes self as the first parameter, which refers
# to the object itself. It can take other parameters as well, which can be
# used to initialise the object's state.

# example of init method in a class
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
