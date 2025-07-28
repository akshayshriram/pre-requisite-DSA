from functools import reduce

myList = [23,43,21,64,7]

# Using max func
print("using max func", max(myList))

maxVal = myList[0]

for val in myList:
    if maxVal < val:
        maxVal = val
print("using Loop", maxVal)

# Using sorting
myList.sort()
print("Using sorting",myList[-1])

# Using reduce func
v2List = [14,10,22,90,32]

largestVal = reduce(lambda x , y: x if x > y else y, v2List)
print("Using reduce and lambda in v2List", largestVal)