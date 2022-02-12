from collections import Counter
li1 = [1,2,3,5,6,7]

max_length = max(li1)
minimum = min(li1)

target_elements = []
for i in range(minimum, max_length+1):
    target_elements.append(i)
print(target_elements)

missing_elements = Counter(target_elements)- Counter(li1)

print(missing_elements)



