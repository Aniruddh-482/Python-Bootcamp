# Inheritance allows us to define a class that inherits all the methods and properties from another class.
# Parent class is the class being inherited from, also called Base Class.
# Child class is the class that inherits from another class, also called Derived Class.

# For Example:

class Animal:  # Parent Class or Super Class
    def __init__(self):
        self.num_eyes = 2

    def breathe(self):
        print("Inhale, exhale.")

class Fish(Animal):  # Child Class or Sub Class
    def __init__(self):
        super().__init__()  # Initialiser
#         \
# Refers super class(Animal) or Parent Class.
# By this we can inherit the methods and attributes of the super class.
# The call to super() in the initialiser is recommended, but not strictly required.

    def breathe(self):
        super().breathe()
        print("doing this underwater.")
# We are extending the functionality of the breathe() method.
# By this we can do the tasks which are in super class and add something more to do. 

    def swim(self):
        print("moving in water.")

nemo = Fish()
nemo.breathe()

