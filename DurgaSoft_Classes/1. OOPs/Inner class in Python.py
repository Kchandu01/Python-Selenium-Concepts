"""
Inner class in Python:
Inner Class in Python
A class defined in another class is known as inner class or nested class.
If an object is created using child class means inner class then the object
can also be used by parent class or root class. A parent class can have one
or more inner class but generally inner classes are avoided.

We can make our code even more object-oriented by using inner class. A single
object of the class can hold multiple sub-objects. We can use multiple sub-objects
 to give a good structure to our program.

Example –

First we create a class and then the constructor of the class.

After creating a class, we will create another class within that class,
the class inside another class will be called as inner class.

"""


# create a Color class
class Color:

    # constructor method
    def __init__(self):
        # object attributes
        self.name = 'Green'
        self.lg = self.Lightgreen()

    def show(self):
        print("Name:", self.name)

    # create Lightgreen class
    class Lightgreen:
        def __init__(self):
            self.name = 'Light Green'
            self.code = '024avc'

        def display(self):
            print("Name:", self.name)
            print("Code:", self.code)


# create Color class object
outer = Color()

# method calling
outer.show()

# create a Lightgreen
# inner class object
g = outer.lg

# inner class method calling
g.display()
