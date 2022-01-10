
class Parent:
    num = 100                    # class variable

    def __init__(self, a, b):
        self.num1 = a            # Instance variables
        self.num2 = b



    def addition(self):
        return self.num1 + self.num2 + Parent.num    # self.num also ok


obj = Parent(10,20)
print(obj.addition())



