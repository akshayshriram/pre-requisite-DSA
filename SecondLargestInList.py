import heapq

myList = [29,43,54,26,75,23]

# using sorting
print("Using myList",myList)
myList.sort()
print(myList)
print("using sorting", myList[-2])

# Using heapq nlargeest
v2List =[12,32,2,23,18,67]

topTwo = heapq.nlargest(2,v2List)
print("print v2List", v2List)
print(topTwo)
# [67, 32]
# Second largest is at index 1
print("Using heapq nlargest", topTwo[1])


# Using For loop
v3List = [47,34,22,67,34,77]
max1 = max2 = float('-inf')

for val in v3List:
    if val > max1:
        max2 = max1
        max1 = val
    elif val > max2 and val != max1:
        max2 = val

print(max2)