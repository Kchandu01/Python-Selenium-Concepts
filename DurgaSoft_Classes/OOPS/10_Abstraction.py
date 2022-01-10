"""
What is an Abstract Class in Python?
An abstract class is the class which contains one or more abstract methods.
An abstract method is the one which is just defined but not implemented.

The above statements may seem unclear with the new terms. Let’s discuss them in detail in this article.

Types of Methods in Python:
Based on the implementation the methods can be divided into two types:

1. Implemented methods.
2. Un-implemented method.

1. Implemented methods:
A method which has a both method name and method body, that method is called an implemented method.
They are also called concrete methods or non-abstract methods. The methods which we have seen in the
previous chapters are implemented i.e having method name and body as well.

2. Un-implemented methods:
A method which has only method name and no method body, that method is called an unimplemented method.
They are also called as non-concrete or abstract methods.

How to declare an abstract method in Python:
Abstract methods, in python, are declared by using @abstractmethod decorator.

Syntax for abstract class:

class Demo:
    @abstractmethod
    def one(self):                   # Un-implemented method
        pass
    def two(self):
        print("Implemented Method")

Method ‘one’ is abstract method. Method ‘two’ is non-abstract method.
Since one abstract method is present in class ‘Demo’, it is called Abstract class
"""
"""
Abstract Method in Python
From the above example, we can understand that an abstract class is the one which does not have implementation. 
Few points about it:

1. By using @abstractmethod decorator we can declare a method as an abstract method.
2. @abstractmethod decorator presents in abc module. We should import the abc module in order to use the decorator.
3. Since abstract method is an unimplemented method, we need to put a pass statement, else it will result in error.
4. Class which contains abstract methods is called an abstract class.
5. For abstract methods, implementation must be provided in the subclass of abstract class.
"""

from abc import *


class Demo1(ABC):
    @abstractmethod
    def m1(self):
        pass

    @abstractmethod
    def m2(self):
        pass

    def m3(self):
        print("Implemented method")


# Output: No Output because no object is created. Just a demo to show abstract methods

"""
Abstract Classes in Python:
1. Every abstract class in Python should be derived from the ABC class which is present in the abc module. 
2. Abstract class can contain Constructors, Variables, abstract methods, non-abstract methods, and Subclass.
3. Abstract methods should be implemented in the subclass or child class of the abstract class. (demo2.py)
4. If in subclass the implementation of the abstract method is not provided, then that subclass, automatically, 
will become an abstract class. (demo3.py)
5. Then, if any class is inheriting this subclass, then that subclass should provide the implementation for 
abstract methods. (demo4.py)
6. Object creation is not possible for abstract class. (demo4.py or demo8.py)
7. We can create objects for child classes of abstract classes to access implemented methods.
"""
from abc import ABC, abstractmethod


# Abstract Class
class Bank(ABC):
    def bank_info(self):
        print("Welcome to bank")

    @abstractmethod
    def interest(self):
        "Abstarct Method"
        pass


# Sub class/ child class of abstract class
class SBI(Bank):

    def interest(self):
        "Implementation of abstract method"
        print("In sbi bank 5 rupees interest")


s = SBI()
s.bank_info()
s.interest()

"""
In the above example, Bank is an abstract class which having intertest() abstract method. 
SBI class is a child class to Bank class, so SBI class should provide implementation for 
abstract method which is available in Bank abstract class. An object is created to subclass, 
which is SBI, and the implemented method interest() is called.

If child class misses to provide abstract methods’ implementation
If a child class inherits an abstract class, doesn’t provide the implementation for abstract methods, 
then that child class also will be considered as an abstract class. Object creation for such child 
classes is also not possible. Even, if we try to create an object an error will be thrown.
"""
from abc import ABC, abstractmethod


# Abstract Class
class Bank(ABC):
    def bank_info(self):
        print("Welcome to bank")

    @abstractmethod
    def interest(self):
        "Abstarct Method"
        pass


# Sub class/ child class of abstract class
class SBI(Bank):
    def interest(self):
        print("In SBI bank 5 rupees interest")

    def balance(self):
        print("Balance is 100")


s = SBI()
s.bank_info()
s.balance()

# Output: Can't instantiate abstract class SBI with abstract method interest

# Different cases for Abstract class object creation:

# 1. Case1: If any class is inheriting ABC class, and that class doesn’t contain an abstract method,
# then happily we can create an object to that class.

from abc import *


class Demo(ABC):
    def m(self):
        print("calling")


d = Demo()
d.m()

# 2. Case2: If any class is inheriting ABC class, then that class will become an abstract class.
# If that class contains an abstract method, then the object creation is not possible for abstract class.
from abc import *


class Demo(ABC):
    @abstractmethod
    def m(self):
        pass

    def n(self):
        print("Implemented method")


# t=Demo()   # cant create object

# 3.Case3: If any class is not inheriting ABC class, then we can create an object for that class
# even though it contains an abstract method. As per below example, class not inheriting ABC class,
# but it contains abstract methods.
from abc import *


class Demo:
    @abstractmethod
    def m(self):
        pass

    def n(self):
        print("Implemented method")


t = Demo()
t.m()
t.n()

"""
When should we go for abstract class?
An abstract class is a class which can contains few implemented methods and few unimplemented methods as well. 
When we know about requirements partially, but not completely, then we should go for abstract class.

When should we go for concrete class?
Concrete class is a class which is fully implemented. It contains only implemented methods. 
When we know complete implementation about requirements, then we should go for concrete class.
"""