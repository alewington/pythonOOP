# python oop

# OOP is Object orientated language.
# This focuses on making objects that are highly reuseable.
# This is a class and an object of the class.

class Person:
    def __init__(self, name):
        self.name = name

# Methods are functions inside classes.

    def sayHi(self):
        print("Hi " + self.name)


# Objects are instances of a class.
p1 = Person("Steve")
p2 = Person("Alex")
p3 = Person("Wolf")

# Methods can be called by the object.
p1.sayHi()
p2.sayHi()
p3.sayHi()

# OOP

# 1. provides a clear structure to your programs
# 2. DRY (Don't Repeat Yourself), avoid repeating code, put them into
# functions and classes.
# 3. Build reusuable applications but with less code.
# 4. Code is easier to maintain.
# 5. Code is easier to reuse ( differences to reusable applications)
# 6. Code is easier to debug
