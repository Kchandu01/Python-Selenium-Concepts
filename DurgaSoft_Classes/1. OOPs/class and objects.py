"""
Class :
    Class is a blueprint of objects. Every class has its own Attributes and Behaviour.
    Attributes - Variables are used for storing data.
    Behaviour - Methods are used describe behaviour.

Objects:
    Objects is an instance of class.
    One class can have multiple objects.
    Ex: If i am a company then every employee is an object.
    Employee name, id are Attributes.
    and Employee is speaking,walking,running are Behaviours.
"""


class Computer:

    def __init__(self, cpu, ram):

        # object Attributes
        self.CPU = cpu
        self.RAM = ram

    def config(self):
        print(f"Cpu is {self.CPU} and Ram is {self.RAM}")


# Create objects of class
# com1 = Computer()

# for accessing class method we have two methods,
# Computer.config(com1)
# com1.config()              # we prefer the second method

"""
if we have to define class variable or to initialize the class variables
we use __init__ method
So passing variables to init method create object and pass variables in class itself.
init methods calls automatically when we create objects of class.
"""
com2 = Computer('i5', 16)
com2.config()

# we can have multiple objects of different data
com3 = Computer('i7', 256)
com3.config()
