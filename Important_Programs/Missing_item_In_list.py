# from collections package import Counter class

from collections import Counter

input = [1, 2, 4, 5, 7, 8, 10]

output = [1, 2, 3, 3, 4, 5, 6, 7, 8, 9, 10]


missing_items = Counter(output) - Counter(input)
print(missing_items)

# Output : Counter({3: 2, 6: 1, 9: 1})

# here output shows 3 is missing 2 times in input list and 6 is missing 1 times
# and 9 is missing 1 times





########################################################################################################
# for strings
target_list = ["one", "two", "three", "four", "five"]
output_list = ['two','three','four', 'five']

print(set(target_list).difference(set(output_list)))