# Reverse string
# Using a while loop

str1 = 'selenium'
str2 = ''

#str2 = str1[::-1]
#print(str2)

count = len(str1)

while count>0:
    str2 = str2 + str1[count-1]
    count -= 1

print(str2)


# using for loop

def reverse_string(str):
    str1 = ""  # Declaring empty string to store the reversed string
    for i in str:
        str1 = i + str1
    return str1  # It will return the reverse string to the caller function


str = "123210"  # Given String
print("The original string is: ", str)
print("The reverse string is", reverse_string(str))  # Function call