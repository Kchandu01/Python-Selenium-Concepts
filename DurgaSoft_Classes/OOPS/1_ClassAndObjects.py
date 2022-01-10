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

Class in Python:
A class is a blueprint or template which contains attributes.It is a specification
of properties and action of objects.

Objects in Python:
An object is an instance of a class. Using objects we can access class members, store data etc.
They are like physical entities of class.

Self variable in Python:
In the demo1.py the display method has a parameter named ‘self’. Let’s talk about it:

self is a default variable that refers to a current class object or the current instance(object) of a class.
Generally, by using self, we can initialize the instance variables inside the constructor.
By using a self variable, we can access instance variables and instance methods.
It can also be some other name rather than ‘self’, but the most commonly used and preferred is ‘self’.
It contains the address of the current object being referred.
"""


class Employee:
    def __init__(self, name):
        self.name = name

    def display(self):
        print('Hi,My name is ', self.name)


obj = Employee("Aakash")
obj.display()

obj1 = Employee("Rani")
obj1.display()
