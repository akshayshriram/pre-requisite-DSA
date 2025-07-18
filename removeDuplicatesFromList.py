myList = [1,2,2,3,3,2,1,4,5,7,2,9,3,1]
uniqueList = []

for item in myList:
    if item not in uniqueList:
        uniqueList.append(item)

print(uniqueList)

print(set(myList))