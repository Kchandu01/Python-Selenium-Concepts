"""
Types of Methods:
    1. Instance Methods
    2. Class Methods
    3. Static Methods
    If we are using self as a function parameter or in front of a variable,
that is nothing but the calling instance itself.
As we are working with instance variables we use self keyword.
Note: Instance variables are used with instance methods.

1. Instance Method
This is a very basic and easy method that we use regularly when we create
classes in python. If we want to print an instance variable or instance
method we must create an object of that required class.

'has two types:
Accessor(Getters): If you want to fetch the value from an instance variable we call them accessors.

Mutator(Setters): If you want to modify the value we call them mutators.
'

If we are using self as a function parameter or in front of a variable,
that is nothing but the calling instance itself.

As we are working with instance variables we use self keyword.

Note: Instance variables are used with instance methods.
"""
"""


# Look at the code below
# Instance Method Example in Python
class Student:

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def avg(self):
        return (self.a + self.b) // 2


s1 = Student(10, 20)
print(s1.avg())
"""
"""
Output:
15.0

In the above program, a and b are instance variables and these 
get initialized when we create an object for the Student class. 
If we want to call avg() function which is an instance method, 
we must create an object for the class.

If we clearly look at the program, the self keyword is used so 
that we can easily say that those are instance variables and methods.

2. Class Method: 
classsmethod() function returns a class method as output for the given function.

Here is the syntax for it:

classmethod(function)
The classmethod() method takes only a function as an input parameter 
and converts that into a class method.

There are two ways to create class methods in python:

Using classmethod(function)

Using @classmethod annotation

A class method can be called either using the class (such as C.f()) or 
using an instance (such as C().f()). The instance is ignored except for its class. 
If a class method is called from a derived class, the derived class object is 
passed as the implied first argument.

As we are working with ClassMethod we use the cls keyword. Class variables are used with class methods.

Look at the code below.

# Class Method Implementation in python 
class Student:
    name = 'Student'
    def __init__(self, a, b):
        self.a = a
        self.b = b 
    
    @classmethod
    def info(cls):
        return cls.name

print(Student.info())
Output:
Student
In the above example, name is a class variable. If we want to create a class 
method we must use @classmethod decorator and cls as a parameter for that function.

3. Static Method
A static method can be called without an object for that class, 
using the class name directly. If you want to do something extra with a class we use static methods.

For example, If you want to print factorial of a number then we don't 
need to use class variables or instance variables to print the 
factorial of a number. We just simply pass a number to the static 
method that we have created and it returns the factorial.

Look at the below code

# Static Method Implementation in python
class Student:
    name = 'Student'
    def __init__(self, a, b):
        self.a = a
        self.b = b 
    
    @staticmethod
    def info():
        return "This is a student class"

print(Student.info())
Output

This a student class

"""


# 1. Instance method example

class Student:
    college = 'BMIT'

    def __init__(self, m1, m2, m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3

    def avg(self):
        return (self.m1 + self.m2 + self.m3) // 3

    # Instance method has two types
    # 1. Accessor (getter) : which only fetch the data
    # If you want to fetch the value from an instance variable we call them accessors.
    # 2. Mutator (Setter) : which modifies the value
    # If you want to modify the value we call them mutators.
    def get_m1(self):  # Accessors or getter
        return self.m1

    def set_m1(self):  # Mutators or setter
        self.m1 = 95
        return self.m1

    # Class methodd
    @classmethod
    def get_college(cls):
        return cls.college

    # Static Method
    @staticmethod
    def info():
        print("These marks of students 10th class")
s1 = Student(75, 85, 82)
s2 = Student(82, 89, 92)

print(s1.avg())
print(s2.avg())
print(s1.get_m1())
print(s1.set_m1())
print(s1.avg())

# Method - 2 : Class Method
# working with class variables that is here college = student
# Here instead of creating object class we can directly get method as,
print(Student.get_college())

# Method -3: Static Method
# no need to create object of class
Student.info()

