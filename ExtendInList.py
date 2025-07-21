mylist = [12,23,34,45,56]

myNewList = [10,20,30,40]
mylist.extend(myNewList)
print(mylist)

# Using += operator
mylist += myNewList
print(mylist)

# Using slicing, can add to any index
v2List = [1,2,3,4,5]

# At the end
mylist[len(mylist):] = v2List
print(mylist)

print(mylist)