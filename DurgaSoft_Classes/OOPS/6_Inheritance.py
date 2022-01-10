"""
What is Inheritance in Python:
Inheritance, in general, is the passing of properties to someone. In programming languages,
the concept of inheritance comes with classes.

1. Creating new classes from already existing classes is called inheritance.
2. The existing class is called a super class or base class or parent class.
3. The new class is called a subclass or derived class or child class.
4. Inheritance allows sub classes to inherit the variables, methods and constructors of their super class.


Advantages of Inheritance:
1. The main advantage of inheritance is code re-usability.
2. Time taken for application development will be less.
3. Redundancy (repetition) of the code can be reduced.

Implementation of Inheritance in Python:
While declaring subclass, we need to pass super class name into subclass’s parenthesis
"""

# 1. Single Inheritance:
class Parent:
    def one(self):
        print("This is Parent class Method")

class Child(Parent):
    def two(self):
        print("This is child class method")

p = Parent()
p.one()
c = Child()
c.one()
c.two()

# 2. Multilevel Inheritance:
class A:
    def sum(self):
        print("A class method")

class B(A):
    def sub(self):
        print("B class Method")

class C(B):
    def mul(self):
        print("C class method")

c = C()
c.sum()
c.sub()
c.mul()

# 3. Multiple Inheritance:

class P1:
    def sum(self):
        print("Parent 1 method")

class P2:
    def sum(self):
        print("Parent 2 Method(with same name)")
    def sub(self):
        print("Parent 2 method")

class P3(P1,P2):
    def mul(self):
        print("child class method")

z= P3()
z.sum()
z.sub()
z.mul()


"""
What if both parent classes have a method with the same name?
There may be a chance that two parent classes can contain methods which are having the 
same method name in both classes. Syntactically this is valid.

In the above scenario, which method will child class inherit?
The answer for this depends on the order of inheritance of parent classes in the child class.

class C(P1, P2): ===>P1”s class method will be considered
class C(P2, P1): ===>P2”s class method will be considered


"""
class P1:
    def sum(self):
        print("Parent 1 method")

class P2:
    def sum(self):
        print("Parent 2 Method(with same name)")
    def sub(self):
        print("Parent 2 method")

class P3(P2,P1):
    def mul(self):
        print("child class method")

z= P3()
z.sum()
z.sub()
z.mul()



######### CONSTRUCTORS in INHERITANCE:
# By default, the super class‟s constructor will be available to the subclass.

class A:
    def __init__(self):
        print("super class A constructor")
class B(A):
    def m1(self):
        print("Child Class B: m1 method from B")
b=B()

"""
If child class and super class both have constructors, then?
If child class and super class both have constructors, if you create an object to child class then 
child class constructor will be executed. While creating object for a class, that class’s 
constructor is first priority.
"""


class A:
    def __init__(self):
        print("super class A constructor")


class B(A):
    def __init__(self):
        print("Child class B constructor")


b = B()

"""
Can we call super class constructor from child class constructor?
Yes, we can call super class constructor from child class constructor by using super() function. 
super() is a predefined function which is useful to call the superclass constructors, variables 
and methods from the child class.
"""
class A:
    def __init__(self):
        print("super class A constructor")

class B(A):
    def __init__(self):
        print("child class B constructor")
        super().__init__()

b = B()