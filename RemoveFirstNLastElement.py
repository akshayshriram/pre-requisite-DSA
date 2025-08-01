from collections import deque

myList = [1,2,3,4,5,6,7,8,9]
print(myList)
myList.pop(0)
print(myList)

del myList[0]

print(myList)

myList = myList[1:]
print(myList)

# Using collections.deque
# myList = deque(myList)
# myList.popleft()
# print(myList)


# remove last element from list

del myList[-1]
print(myList)

myList.pop(-1)
print(myList)

myList = myList[:-1]
print(myList)