myList = [10,20,34,12,23]

# Using min func
print("Using min func",min(myList))

# Using loop
minVal = myList[0]

for val in myList:
    if minVal > val:
        minVal = val

print("Using loop",minVal)

# Using sorting

v2List = [12,32,4,15,40]
v2List.sort()
print("Using Sort", v2List[0])
