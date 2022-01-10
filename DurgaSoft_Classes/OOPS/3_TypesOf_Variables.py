"""
Types of Variables:
    1. Class Variables (class level Variables)
    2. Instance Variables (Object level Variables)
    3. Local Variables
"""
""""
# 1. Class Variables (class level Variables):
        If the value of a variable is not changing from object to object, such types 
        of variables are called static variables or class level variables. We can access 
        static variables either by class name or by object name. 
        Accessing static variables with class names is highly recommended than object names.
"""


class Student1:
    college_name = 'GITAM'

    def __init__(self, name, id):
        self.name = name
        self.id = id


s1 = Student1('Nithya', 1)
s2 = Student1('Anushka', 2)

print("Student1 info:")
print("Name: ", s1.name)
print("Id : ", s1.id)
print("College name  : ", Student1.college_name)

print("\n")
print("Student2 info:")
print("Name: ", s2.name)
print("Id : ", s2.id)
print("College name : ", Student1.college_name)

"""
Declaring static variables in Python:
We can declare static variable in the following ways,

1. Inside class and outside of the method
2. Inside constructor
3. Inside instance method
4. Inside class method
5. Inside static method
"""


# 1. Inside class and outside the method
class Demo:
    a = 20  # class variable

    def m(self):
        print("this is method")


print(Demo.__dict__)


# 2. Inside constructor
class Demo:

    def __init__(self):
        Demo.b = 20  # class variable


d = Demo()
print(Demo.__dict__)


# 3. Inside instance method
class Demo:

    def m1(self):
        Demo.b = 20  # class variable


obj = Demo()
obj.m1()
print(Demo.__dict__)


# 4. Inside class method
class Demo:
    @classmethod
    def m2(cls):
        Demo.b = 30  # class variable


obj = Demo()
obj.m2()
print(Demo.__dict__)


# 5. Inside static method
class Demo:
    @staticmethod
    def m3():
        Demo.z = 10


Demo.m3()
print(Demo.__dict__)
##########################################################################################################
""" 
2. Instance Variables (Object level Variables):
       If the value of a variable is changing from object to object then such 
       variables are called as instance variables.
"""


class Student:
    def __init__(self, name, id):
        self.name = name
        self.id = id


s1 = Student('Ramya', 101)
s2 = Student('Rocky', 102)
print("Students Info: ")
print("Name: ", s1.name)
print('ID: ', s1.id)
print("Name: ", s2.name)
print("ID: ", s2.id)

"""
We can declare and initialize the instance variables in following ways,

1. By using a constructor.
2. By using instance methods
3. By using object name
"""


## 1. By using a constructor
# We can declare and initialize instance variables inside a constructor by using self variable.
class Employee:
    def __init__(self):
        self.name = 'Nitya'
        self.id = 100


e = Employee()
print('Name:', e.name)
print('id:', e.id)
print(e.__dict__)  # to print in dictionary formats as {'name': 'Nitya', 'id': 100}


## 2. By using an Instance methods:
#  We can declare and initialize instance variables inside instance method by using self variable.

class Student10:
    def m1(self):
        self.a = 11
        self.b = 21
        self.c = 34
        print(self.a)
        print(self.b)
        print(self.c)


s = Student10()
s.m1()
print(s.__dict__)


## 3. By using Object Name:
# We can declare and initialize instance variables by using object name as well
class Test:
    def __init__(self):
        print("This is constructor")

    def m1(self):
        print("This is instance method")


t = Test()
t.m1()
t.a = 10
t.b = 20
t.c = 55
print(t.a)
print(t.b)
print(t.c)
print(t.__dict__)


##########################################################################################################

# 3. Local Variables in Python:

class Demo:
    def m(self):
        a = 10  # Local Variable
        print(a)

    def n(self):
        pass
        # print(a)      #'a' is local variable of m()
        # so here it gives error as 'a' is not defined


d = Demo()
