myList = [1,2,3,4,5]

# for i in range(1):
#     firstElement = myList[i]
#     for j in range(len(myList)):
#         if j == len(myList)-1:
#             print("true")
#             myList[i], myList[j] = myList[j], myList[i]

myList[0], myList[-1] = myList[-1], myList[0]


print(myList)

def swapElements(newList):
    sizeOfList = len(newList)

    # Swap
    temp = newList[0]
    newList[0] = newList [-1]
    newList[-1] = temp

    return newList

myNewList = [12 ,53, 14,5,23]
print("NewList:", myNewList)
print(swapElements(myNewList))

# Using Tuple variable 

def TuppleVar(newList):

    # Store the values in the tupple variable - get
    get = newList[-1], newList[0]

    # Reassign the get var to the list
    newList[0], newList[-1] = get

    return newList
v2List = [42,74,2,32,55]
print("v2List", v2List)
print("Using Tupple var:", TuppleVar(v2List))

# Swap using slicing

def swapSlicing(newList):
    if len(newList) >= 2:
        newList = newList[-1:] + newList[1:-1] + newList[:1]
    return newList

v3List= [93]
print("v3List:",v3List )
print("swapSlicing",swapSlicing(v3List))