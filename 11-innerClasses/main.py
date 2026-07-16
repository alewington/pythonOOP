# Inner Classes

# Inner classes are classes defined within another class. They are used to
# logically group classes that are only used in one place, increasing
# encapsulation and readability.

# example of inner classes in a class
class PersonnalComputer:
    # initialiser
    def __init__(self, brand: str) -> None:
        self._brand = brand
        self._state = 'OFF'

    # inner class
    class Processor:
        def __init__(self, model: str) -> None:
            self.model = model

        def get_model(self) -> str:
            return self.model

    # method - adds functionality
    def turn_on(self) -> None:
        self._state = 'ON'
        print(f'{self._brand}: ON')

    # method
    def turn_off(self) -> None:
        self._state = 'OFF'
        print(f'{self._brand}: OFF')


# create an object of the class
pc1 = PersonnalComputer('Dell')
# create an object of the inner class
processor1 = pc1.Processor('Intel i7')
# call the method of the inner class
print(f'Processor model: {processor1.get_model()}')

# Inner classes are classes defined within another class. They are used to
# logically group classes that are only used in one place, increasing
# encapsulation and readability. They can be used to create a hierarchy of
# classes, where the inner class is a part of the outer class. They can also
# be used to create a namespace for the inner class, preventing name clashes
# with other classes.

# In this program example the inner class Processor is defined within the
# outer class PersonnalComputer. The inner class Processor has a method
# get_model that returns the model of the processor. The outer class
# PersonnalComputer has methods turn_on and turn_off that change the
# state of the computer. An object of the inner class Processor is created
# using an object of the outer class PersonnalComputer, and the method
# get_model is called on the inner class object.

# Examples of this are the collections module in the standard library, which
# defines several inner classes such as namedtuple and defaultdict, which are
# used to create specialized data structures.

# Another example is the tkinter module, which defines several inner classes
# such as Frame and Button, which are used to create GUI applications. Inner
# classes can also be used to create a hierarchy of classes, where the inner
# class is a part of the outer class. For example, a Car class could have an
# inner Engine class,# which would be used to represent the engine of the car.
