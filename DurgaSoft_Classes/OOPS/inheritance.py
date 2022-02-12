class A:

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def add(self):
        return self.a + self.b

class B(A):

    def __init__(self, c, d):

        #super().__init__(c,d)
        self.c = c
        self.d = d

    def mul(self):
        return self.c * self.d

#obj1 = A(2,3)
obj = B(4,5)
#print(obj1.a)
print(obj.mul())
print(obj.add())