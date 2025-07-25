import copy
myList = [10,20,30,40,50]

newList = myList.copy()

print("newList", newList)

# clone the myList using slice
usingSlice = myList[:]

print("usingSlice", usingSlice)

# copy myList using list()
usingList = list(myList)
print("usingList", usingList)

# Using List comprehension

print("List Comprehension",[item for item in myList])


# using copy.deepcopy() It ensures that changes to nested objects in the clone do not affect the original.
print("Using copy.deepcopy():", copy.deepcopy(myList))