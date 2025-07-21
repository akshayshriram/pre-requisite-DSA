myList = [10,20,30,40,50,20]
# remove() - This removes only first element
myList.remove(20)
print(myList)

val = myList.pop(3)
print("val",val)
print("myList",myList)

# If we do not pass the index it will remove last element
myList.pop()
print(myList)

# The del removes element by specifing the index or range of indices
del myList[1:2]
print(myList)

# Clear all element from list
myList.clear()
print(myList)
