myList = [1, 2, 3, 1, 1,1,1,1,2, 4, 5, 6, 5]

setList = set()

duplicateList = []

for val in myList:
    if val in setList and val not in duplicateList:
        duplicateList.append(val)
    else:
        setList.add(val)

print("Duplicate list Using for loop", duplicateList)

# Nest for loop - Not efficient

nestedDuplicateList = []

for i in range(len(myList)):
    for j in range(i+1, len(myList)):

        if myList[i] == myList[j] and myList[j] not in nestedDuplicateList:
            nestedDuplicateList.append(myList[j])

print("Using Nested for loop", nestedDuplicateList)