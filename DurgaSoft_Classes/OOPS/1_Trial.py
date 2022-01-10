class Employee:

    def __init__(self):
        self.name = "Akash"
        self.college = "BMIT"

    def firstdata(self):
        print(f'My name is {self.name} and I am from {self.college}')

    def display(self):
        self.name = 'Amol'
        print(f'My name is {self.name} and I am also from {self.college}')


obj = Employee()
obj.firstdata()
obj.display()
