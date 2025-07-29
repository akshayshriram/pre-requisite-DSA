from collections import Counter

myList = [23,15,72,55,73,45,78,98,23,44,51,60]

even = 0
odd = 0

for val in myList:
    if val % 2 == 0:
        even += 1
    elif val % 2 != 0:
        odd += 1
print("Even", even)
print("Odd", odd)

# Using count
counts = Counter(['even' if val % 2 == 0 else 'odd' for val in myList])

print("Even Counts", counts['even'])
print("Odd Counts", counts['odd'])

filterEven = len(list(filter(lambda val: val % 2 == 0, myList)))
fitlerOdd = len(list(filter(lambda val: val % 2 != 0, myList)))



print("filterEven", filterEven)
print("filterOdd", fitlerOdd)