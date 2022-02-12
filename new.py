numbers = [1,2,3,4,5,6]

Dict = {}

Dict[numbers[0]] = numbers[1]
Dict[numbers[2]] = numbers[3]
Dict[numbers[4]] = numbers[5]
print(Dict)
Dict1 = {i: numbers[i] for i in range(1,len(numbers)-1)}
print(Dict1)


Dict2 = {i : numbers[i] for i in range(len(numbers))}
print(Dict2)
