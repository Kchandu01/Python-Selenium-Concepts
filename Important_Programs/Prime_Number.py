num = int(input("Enter the num: "))

if num > 1:
    for i in range(2,num):
        if num%i == 0:
            print(num," is not prime number")
            print(i)
            print(f'{i} times {num//i} is {num} ')
            break
    else:
        print(f'{num} is prime Number')
else:
    print(f'{num} is not prime number')