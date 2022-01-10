"""
Super() Function in Python:
super() is a predefined function in python. By using super() function in child class, we can call,

1. Super class constructor.
2. Super class variables.
3. Super class methods.

"""


# 1. Calling super class constructor from child class constructor using super():

class A:
    def __init__(self):
        print("super class A constructor")


class B(A):
    def __init__(self):
        print("child class B constructor")
        super().__init__()
        # super(B, self).__init__()                    # another method


b = B()

###########################
"""
## Which scenarios super() function is required?

When both superclass and child class may have the same method names, same variable names, some scenarios 
may come where we want to use both of them. In such a case, using the super() function we can call the 
parent class method.
"""


# 2.  Calling super class method from child class method using super():

class A:
    def m1(self):
        print("super class A: m1 method")


class B(A):
    def m1(self):
        print("child class B: m1 method")
        super().m1()


b = B()
b.m1()


## 3. Calling super class variable from child class method using super():

class A:
    x = 10

    def m1(self):
        print("Super class A: m1 method")


class B(A):
    x = 20

    def m1(self):
        print('Child class x variable', self.x)
        # print('Child class x variable', B.x)
        print('Super class x variable', super().x)


b = B()
b.m1()


# Example:


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print("Name: ", self.name)
        print("Age: ", self.age)


class Empolyee(Person):
    def __init__(self, name, age, id, address):
        self.id = id
        self.address = address
        super().__init__(name, age)
        # super(Empolyee, self).__init__(name,age)   # another method of a calling superclass constructor

    def display(self):
        super().display()
        # super(Empolyee, self).display()          # another method of a calling superclass method
        print("ID: ", self.id)
        print("Address: ", self.address)


obj = Empolyee('Rakhi', 28, 100, 'ABCD Colony')
obj.display()

"""
Different Approaches for Calling method of a specific superclass
We can use the following approaches:

1. NameOfTheClass.methodname(self) – It will call super class method
2. super(NameOfTheClass, self).methodname – It will call the method of super class of mentioned class name.
"""

"""
From a child if we want to access the parent class instance variable then we should use a self variable only. 
By using super() function we cannot access parent class instance variables from child class. But, the class 
variables can be accessed
"""
