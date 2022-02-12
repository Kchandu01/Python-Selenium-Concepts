

# Sorting a list without inbuilt function

def sortlist(a):

    b = len(a) - 1
    # -1 bcz we are comparing two adjacent values
    for i in range(b):
        for j in range(b-i):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]

    return a

list = [9,3,6,2,19,-5,7,11]
print(sortlist(list))