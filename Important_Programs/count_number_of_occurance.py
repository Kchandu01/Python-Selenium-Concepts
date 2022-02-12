# for numbers
import collections

numbers = [1, 2, 3, 1, 2, 1, 5, 3, 1, 4, 3]
occurance = numbers.count(1)
print(occurance)

# for strings
strings = ['a', 'b', 'a', 'c', 'a']
# occurs = strings.count('a')
# print(occurs)
# in dictionary format
occurances = collections.Counter(strings)
print(occurances)


str = [1,2,3,1,2,3,5,5,6,7,7,8]
# output = {1:2, 2:2, 3:2, 5:2,6:1,7:2,8:1}

occ = collections.Counter(str)
print(occ)