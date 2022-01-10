n = 4
while n>1:
    if n != 3:
        print(n)
        #continue
    n -= 1

"""
    In for loop we iterate in given range ie for i in range(1,10)
but in while loop if iterate until the condition fails.
"""
# Use of break statements
print("USe of break: ")
m = 10
while m>1:
    if m==3:
        break
    print(m)
    m -= 1


# Use of continue
# continue is used to skip current iteration and proceed to next iterations
print("inside continue loop: ")
num = 10
while num>1:
    if num == 7:             # skip 7, not prints 7
        num -=1
        continue
    if num == 3:
        break
    print(num)
    num -=1