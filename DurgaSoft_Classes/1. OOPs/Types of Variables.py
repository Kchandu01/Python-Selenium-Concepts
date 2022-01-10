"""
Types of variables:
     1. Instance variables : declared inside init method
     2. class variable or static variable: declared outside init and inside class
"""


class Car:
    wheels = 4         # class variable

    def __init__(self):
        self.milage = 10            # instance variable
        self.company = 'BMW'        # instance variable

    # These two variables are called as instance variables.
    # why bcz as the object changes these values changes

c1 = Car()
c2 = Car()

print(c1.milage, c1.company)
print(c2.milage,c2.company)

# now when i change object parameters these changes
c1.milage = 20
c1.company = 'VW'

print(c1.milage, c1.company)

# access class parameter
print(c1.wheels)
print(c2.wheels)              # common for both objects

"""
    The instance variables are different for different objects
To make the values common for all objects define variables outside init and inside the class.
bcz if you define the variables inside init it becomes instance variables.
"""

# to change the class variables
Car.wheels = 5         # the value is changed for all objects

print(c1.wheels)
print(c2.wheels)

