""" when you think the code may fail but you dont want testcase to stop
    when you come across that failure,
    then you wrap that code which you think that fail in try block.
    So when exception is raised in try block your test will be sent into another block called except.
    In except block you can write why the test case failed and add some description about error or exception.
"""
"""
try:
    a= 10
    b= 20
    assert(a+b == 60)
except:
    print("Addition must be equal to 30")

"""
"""
Real time example:
    while handling pop-ups we can use. when you land on a page where pop-ups comes or may not come
    So you write a code using pop-ups handling method but when there are no any pop-ups then in that 
    case my test case will fail. when i remove that code then pop-ups may raise.
    So, write code in try block if pop-up is there then it will handle if not then it will go in except block 
    and testcase will not fail.
"""
try:
    with open('file.txt','r') as reader:
        reader.read()

# Instead of customized message in except block if you want to show the actual exception msg or error
# in except block
except Exception as e:
    print(e)

finally:                          # it will executes in both cases
    print("cleaning up resources")

"""
The finally keyword is used in try...except blocks. It defines a block of code 
to run when the try...except...else block is final.
The finally block will be executed no matter if the try block raises an error or not.

This can be useful to close objects and clean up resources.

Why we need Finally Block?
In any project after completing the tasks, it is recommended to destroy all the unwanted things that are created for 
the completion of the task. For example, if I have opened a database connection in my code and done some tasks 
related to the database. After the tasks are completed, it is recommended to close the connection. 
These clean-up activities are very important and should be handled in our code.

finally Block in Python:
finally is a keyword in python which can be used to write a finally block to do clean-up activities.

Why not ‘try except’ block for clean-up activities?
try block: There is no guarantee like every statement will be executed inside the try block. 
If an exception is raised at the second line of code in the try block at, then the remaining 
lines of code in that block will not execute. So, it is not recommended to write clean up code 
inside the try block.

except block: There is no guarantee that an except block will execute. If there is no exception 
then except block won’t be executed. Hence, it is also not recommended to write clean up code 
inside except block

Conclusion:
So, a separate block is required to write clean-up activities. This block of code should always 
execute irrespective of the exceptions. If no exception, then clean-up code should execute. 
If an exception is raised and is also handled , then also clean-up code should execute. 
If an exception is raised, but not handled, then also clean-up code should execute.

All the above requirements, which can’t be achieved by try except block, can be achieved by 
finally block. The finally block will be executed always, irrespective of the exception raised or not, 
exception handled or not.
"""

# Multiple except blocks
try:
   x=int(input("Enter First Number: "))
   y=int(input("Enter Second Number: "))
   print(x/y)
except ZeroDivisionError:
   print("Can't Divide with Zero")
except ValueError:
   print("please provide int value only")


# Default except block
try:
   x=int(input("Enter First Number: "))
   y=int(input("Enter Second Number: "))
   print(x/y)

except ZeroDivisionError:
   print("ZeroDivisionError: Can't divide with zero")

except:             # This is called default except and it must be in last
   print("Default Except: Please provide valid input only")

# default except will execute only if other except block will not execute