"""
Types of Methods in a Class:

1. Instance Methods
2. Class Methods
3. Static Methods

"""
"""
1. Instance Methods in Python:

Instance methods are methods which act upon the instance variables of the class. 
They are bound with instances or objects, that”s why called as instance methods. 
The first parameter for instance methods should be self variable which refers to instance. 
Along with the self variable it can contain other variables as well.
"""


class Student:
    def __init__(self, a):
        self.a = a

    def display(self):  # Instance method
        print(self.a)


obj = Student(10)
obj.display()
obj1 = Student('Maths')
obj1.display()

## There two types of methods in Instance Methods:
# Setter and Getter methods in Python:
#
"""
# 1. Setter Method or Mutator Method:
Setter methods can be used to set values to the instance variables.
They are also known as mutator methods.
Their main aim is to only set values to instance variables, hence they don’t return anything.

Syntax: def set_value(self,variable):
            self.variable = variable
"""


class Employee:
    def set_name(self, name):
        self.name = name

    def set_id(self, id):
        self.id = id


e = Employee()
e.set_name('Akash')
e.set_id(100)
print(e.name)
print(e.id)

"""
2. Getter Method:
 Getter methods are used to get the values of instance variables. They return the value in
 the instance variable. Getter methods also known as accessor methods.
 Syntax: def get_variable(self):
            return self.variable
"""


class Customer:
    def set_name(self, name):
        self.name = name

    def set_id(self, id):
        self.id = id

    def get_name(self):
        return self.name

    def get_id(self):
        return self.id


c = Customer()
c.set_name("Rockyy")
c.set_id(1)

print("My name is :", c.get_name())
print("My id is :", c.get_id())
##########################################################################################################

"""
2. Class Method:
Class methods are methods which act upon the class variables or static variables of the class. 
We can go for class methods when we are using only class variables (static variables) within the method.

1. Class methods should be declared with @classmethod.
2. Just as instance methods have ‘self’ as the default first variable, class method should have ‘cls’ as the 
first variable. Along with the cls variable it can contain other variables as well.
3. Class methods are rarely used in python
"""


class College:
    college_name = 'BMIT'

    @classmethod
    def studentinfo(cls):
        # print(College.college_name)
        return cls.college_name


co = College()
co.studentinfo()
print(College.studentinfo())

#########################################################################################################

"""
3. Static Methods in Python:
The static methods, in general, utility methods. Inside these methods we won’t use any instance 
or class variables. No arguments like cls or self are required at the time of declaration.

We can declare static method explicitly by using @staticmethod decorator.
We can access static methods by using class name or object reference
"""


class Demo:
    @staticmethod
    def sum(x, y):
        print(x + y)

    @staticmethod
    def multilpy(x, y):
        print(x * y)


Demo.sum(2, 3)
Demo.multilpy(3, 4)
