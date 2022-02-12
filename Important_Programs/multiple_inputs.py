#Taking multiple inputs from user in Python
# 1. Using split() method : input().split(separator, maxsplit)
# 2. Using List comprehension :

x,y,z = input('Enter values: ').split()

print(x)
print(y)
print(z)
print(type(z))

# Python program showing
# how to take multiple input
# using List comprehension

# taking two input at a time
x, y = [int(x) for x in input("Enter two values: ").split()]
print("First Number is: ", x)
print("Second Number is: ", y)
print()


"""
end= ” ” statement
The end keyword is used to specify the content that is to be printed at the end 
of the execution of the print() function. By default, it is set to “\n”, which 
leads to the change of line after the execution of print() statement.
"""