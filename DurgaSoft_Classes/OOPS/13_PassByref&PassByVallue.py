"""
Pass by reference – It is used in some programming languages, where values to the argument of the function
are passed by reference which means that the address of the variable is passed and then the operation is
done on the value stored at these addresses.


Pass by value – It means that the value is directly passed as the value to the argument of the function.
Here, the operation is done on the value and then the value is stored at the address. Pass by value
is used for a copy of the variable.

"""
"""
Python pass by reference example
When we pass something by reference any change we make to the variable inside the function then those changes are reflected to the outside value as well.

Example:
"""


# pass by reference:
def test(student):
    new = ['x','y','z']
    student += new
    print("student inside function", student)
    return student

student = ['A','B','C']
test(student)
print("student outside function", student)

"""
Output:
student inside function ['A', 'B', 'C', 'x', 'y', 'z']
student outside function ['A', 'B', 'C', 'x', 'y', 'z']
"""


"""
Python pass by value example
When we pass something by value then the changes made to the function or copying of the variable are not reflected back to the calling function.

Example:
"""


# pass by value:

def test(student):
    student = ['p','q','r']
    print("student inside function", student)
    return


student = ['a','b','c']
test(student)
print("student outside function", student)

"""
Output:
student inside function ['p', 'q', 'r']
student outside function ['a', 'b', 'c']
"""