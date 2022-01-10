"""
Constructors in Python
In any programming language, constructor is a method which, by default, is invoked whenever
an instance(object) for a class is created. It’s not required to explicitly invoke or call it.

Generally, the constructor is used for initial intializations that are required during the
object creation. In python, constructor is a method with the name ‘__init__’.

The methods first parameter should be ‘self’ (referring to the current object).

Is constructor mandatory in Python?
No, it’s not mandatory for a class to have a constructor. It completely is based on our
requirement whether to have a constructor or not. At the time of object creation if any
initialization is required then we should go for a constructor, else it’s not needed.
Without a constructor also, the python program is valid.
"""


"""
Non Parameterized Constructor or Default Constructor:
    Default constructor is one which does not accept any values. It is mainly used for 
    initialization purpose.
    The constructor doesn’t have any parameters except self. The self contains the current object address.
"""
class college:

    def __init__(self):
        self.id = 1

    def display(self):
        print('The student Id is: ', self.id)


obj = college()
obj.display()


"""
Parameterised Constructor in Python:
    Parameterised is one which initialize the instances with the given values.
    If we want different values for different instances then we need to go for a parameterised constructor.
"""

class Employee:

    def __init__(self,name,id,dept):
        self.name = name
        self.id = id
        self.dept = dept

    def displayEmployees(self):
        print(f'{self.name} with ID number {self.id} is working in {self.dept} department.')


obj1 = Employee('Akash',100,'Testing')
obj1.displayEmployees()

obj2 = Employee('Ramya',202,'Developing')
obj2.displayEmployees()


"""
Difference Between Method and Constructor:
    1. Methods are used to do operations or actions.
    while, constructors are used to initialize the instance variables.
    2. Method name can be any name, while
    constructor name must be __init__
    3. Methods we need to call explicitly while,
    constructors get called automatically.
"""

"""
Difference between a method and a function:
Functions which are written inside a class can be accessed only with the objects created 
from the class. They are called methods. 
We can say that methods are nothing but functions which can be referenced by the objects of the class.
"""