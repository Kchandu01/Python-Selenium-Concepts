"""
    Constructor does not return any value.
    Default constructor :
        Default constructor does not take any parameter.
        When create an object of class and don't pass parameters inside.
        Then it is default constructor.
        ex: com1 = Computer()
    Parameterized Constructor:
        Parameterized constructor takes at least one parameter.
        I used a parameterized constructor to assign values to the properties of the class.
        ex: com1 = Computer('i5',16)
"""


class Computer:
    def __init__(self):
        self.name = 'Navin'
        self.age = 28

    def update(self):
        self.age = 30  # it will update the constructor value 28->30

    def compare(self, other):
        if self.age == other.age:
            return True
        else:
            return False


c1 = Computer()
c2 = Computer()

c1.name = 'Rashmi'
c2.age = 40
c1.update()

# for comparing objects by defining own method

if c1.compare(c2):  # compare takes two parameters
    # Here c1 is comparing with c2 so c1 becomes self and c2 becomes other
    print("they are same")
else:
    print("they are different")

print(c1.age)
print(c1.name)
print(c2.age)

"""
Why we need self?
    Self is referring to the objects. If we have 10 objects and if you
    want to refer one object you can use self.
    
"""
"""
First of all, we have to understand the __init__() built-in method for understanding 
the meaning of classes. Whenever the class is being initiated, a method namely 
__init__() is always executed. An __init__() method is used to assign the values 
to object properties or to perform the other method that is required to complete 
when the object is created.

Example of class with __init__() method –
 
# create a Geeksforgeeks class
class Geeksforgeeks:
  
 # constructor method
 def __init__(self):
  
  # object attributes
  self.course = "Campus preparation"
  self.duration = "2 months"
   
 # define a show method
 # for printing the content
 def show(self):
  print("Course:", self.course)
  print("Duration:", self.duration)
  
# create Geeksforgeeks 
# class object
outer = Geeksforgeeks()
  
# method calling
outer.show()
Output:

 Course : Campus Preparation
Duration : As per your schedule 

"""