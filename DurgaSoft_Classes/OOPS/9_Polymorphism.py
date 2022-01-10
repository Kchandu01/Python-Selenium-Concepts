"""
What is Polymorphism in Python?
The word ‘Poly’ means many and ‘Morphs’ means forms. The process of representing “one form in many forms”
is called a polymorphism.

Types of Polymorphism in Python:
The following are the examples, or implementations, of polymorphism:

1.Duck Typing Philosophy of Python
2.Overloading
        Operator Overloading
        Method Overloading
        Constructor Overloading
3.Overriding
        Method overriding
        Constructor overriding


Duck Typing Philosophy of Python:
Duck typing refers to the programming style, in which the object passed to a method supports
all the attributes expected from it, at the runtime. The important thing here is not about
the object type, but about what attributes and methods the object supports.

In duck typing, while creating a data, it’s not required to declare the argument type explicitly.
At runtime, based on provided value the type will be considered automatically. Since Python is
considered as a Dynamically Typed Programming Language, it follows Duck Typing.

“If it walks like a duck, swims like a duck, and quacks like a duck, then it probably is a duck.”

Duck Typing originates from the above saying. For example, let’s consider a class “Car” which has
an attribute ‘engine_name’ and a method ‘start_engine’ which takes the ‘engine_name’ attribute and
does the action of starting the engine. A ‘Truck’ is different from a ‘Car’ but for the duck typing
it actually doesn’t matter. We can create any truck object for the ‘Car’ and use the ‘start_engine’
method to start it.
"""


#### Duck Typing Philosophy :


class Duck:
    def talk(self):
        print("Quack......Quack")


class Dog:
    def talk(self):
        print("Bow......Bow")


class Cat:
    def talk(self):
        print("Meow.....Meow")


#
def m(obj):
    obj.talk()


# The function ‘m’ takes an object and calls for the talk() method of it.
# With duck typing, the function is not worried about what object type of object it is.
# The only thing that matters is whether the object has a method with name ‘talk()’ supported or not.


duck = Duck()
m(duck)

dog = Dog()
m(dog)

cat = Cat()
m(cat)

"""
Overloading in Python:
We can use the same operator or methods for different purposes. There are 3 types of overloading:

1. Operator Overloading
2. Method Overloading
3. Constructor Overloading

1. Operator overloading in Python:
If we use the same operator for multiple purposes, then it is nothing but operator overloading.

‘+’- addition operator can be used for Arithmetic addition and String concatenation as well
* multiplication operator can be used for multiplication for numbers and repetition for strings, lists, tuples etc
"""
# 1. Operator Overloading:
# Operator overloading( + ) example:
print(10 + 20)
print("Python" + "Automation")
print([1, 2, 3] + [4, 5, 6])

# Operator overloading( * ) example:
print(10 * 20)
print("Python" * 4)
print([1, 2, 3, 4] * 5)

# 2. Method Overloading:
"""
If 2 methods have the same name but different types of arguments, then those methods are 
said to be overloaded methods.

But in Python Method overloading is not possible. If we are trying to declare multiple 
methods with the same name and different number of arguments, 
then Python will always consider only the last method.
"""


class Demo:
    def m1(self):
        print("No arg Method")

    def m1(self, a):
        print("One arg Method")

    def m1(self, a, b):
        print("Two arg Methods")


obj = Demo()
# obj.m1()
# obj.m1(10)
# Outputs: TypeError: m1() missing 2 required positional arguments: 'a' and 'b'
# so in Python method overloading is not possible bcz python will consider last method
obj.m1(10, 29)
"""
Conclusion
If we are trying to declare multiple methods with the same name and different number of arguments, 
then Python will always consider only the method which was last declared. In the above program 
python will consider only the method with two arguments, the last method.
"""
"""
How we can handle overloaded method requirements in Python?
Most of the time, if a method with a variable number of arguments is required then we can handle 
it with default arguments or with a variable length of argument methods.
"""


class Addition:
    def total(self, *a):
        sum = 0
        for i in a:
            sum = sum + i
        print("The sum is ", sum)


a = Addition()
a.total(5)
a.total(5, 10)
a.total(5, 10, 20)


# 3.Constructor Overloading in Python:
# Constructor overloading is also not possible in Python.
# If we define multiple constructors, only the last constructor will be considered.
# So we can try in two ways
#   1. Constructor with Default Arguments
class Demo:
    def __init__(self, a=None, b=None, c=None):
        print(a)
        print(b)
        print(c)


d1 = Demo(10, 20)


# 2. Constructor with Variable Length Arguments:
class Demo:
    def __init__(self, *a):
        print('Constructor with variable number of arguments')


d1 = Demo()
d2 = Demo(10)
d3 = Demo(10, 20)
d4 = Demo(10, 20, 30)
d5 = Demo(10, 20, 30, 40, 50, 60)

############################## Method Overriding ####################################################
"""
Overriding in Python:
Overriding refers to the process of implementing something again, which already exists in parent class, 
in child class.

All the members available in the parent class, those are by-default available to the child class through 
inheritance. If the child class is not satisfied with parent class implementation, then child class is 
allowed to redefine that method in the child class based on its requirement. This concept is called overriding. 
Overriding concept applicable for both methods and constructors.
"""


# 1. Method Overriding:
class A:
    def Add(self, x, y):
        print(x + y)

    def Sub(self, x, y):
        print(x - y)


class B(A):
    def Sub(self, x, y):  # Sub Method Overriding
        print(y - x)

    def Mul(self, x, y):
        print(x * y)


b = B()
b.Sub(10, 20)
b.Mul(10, 10)
b.Add(20, 30)


# 2. Constructor Overriding
"""
We have already discussed in detail about the constructor concepts in the inheritance chapter. 
Those concepts also include overriding concepts. Let’s remember some points from there:

1. If child class does not have constructor, then parent class constructor will be executed at 
the time of child class object creation.
2. If child class has a constructor, then child class constructor will be executed at the time of 
child class object creation.
3. From child class constructor we can call parent class constructor by using super() method
"""
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Employee(Person):
    def __init__(self, name, age, eno, esal):
        super().__init__(name, age)
        self.eno = eno
        self.esal = esal

    def display(self):
        print('Employee Name:', self.name)
        print('Employee Age:', self.age)
        print('Employee Number:', self.eno)
        print('Employee Salary:', self.esal)


e1 = Employee('Surabhi', 16, 872425, 26000)
e1.display()
e2 = Employee('Ranjith', 20, 872426, 36000)
e2.display()
