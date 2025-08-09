# Reverse Row sort in Lists of List

import heapq

# using heap
a = [[5, 2, 8], [9, 1, 4], [6, 7, 3]]
print("Original Array", a)
result = [heapq.nlargest(len(row), row) for row in a]

print("Resverse Array",result)

b = [[5, 2, 8], [9, 1, 4], [6, 7, 3]]
print("Original Array",b)
# Using map() + sorted()
result1 = list(map(lambda x: sorted(x, reverse=True),b))
print("Reverse Array", result1)