from DurgaSoft_Classes.OOPS.Oops_Inheritance_1 import Parent

class Child(Parent):
    # if your constructor is not default then call the parent constructor
    def __init__(self):
        Parent.__init__(self,10,20)

    def getData(self):
        return self.num1 + self.num2 + self.addition() + self.num

obj2 = Child()

print(obj2.getData())