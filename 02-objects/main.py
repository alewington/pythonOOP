# classes

# Objects are instances of a class. They are created from the class blueprint.

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


# <- instances or objects called samething i.e Dell computer is an obejct in a
# office or home, but also the made by the class.
dell: PersonnalComputer = PersonnalComputer('Dell')
lenovo: PersonnalComputer = PersonnalComputer('lenovo')

# lets turn instance of 'Dell' ON and OFF.
dell.turn_on()
dell.turn_off()

print('Dell', dell.state)

# Each object has its own state and behavior.
