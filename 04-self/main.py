# self

# The self parameter is a reference to the current instance of the class. It
# is used to access the attributes and methods of the class. It must be the
# first parameter of any method in the class.

# example of self parameter in a class
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

# why use it?
# The self parameter is used to access the attributes and methods of the class.
# It is used to differentiate between instance variables and local variables.
# It is also used to call other methods of the class. It is used to access
# the current instance of the class.
