mySet = {1,2,4,6,"asd",2}
print(mySet,type(mySet))

mySet.add("new")

mySet2 = {3,5,"new1"}

mySet.update(mySet2)

print(mySet)

mySet.remove("asd")
print(mySet)

mySet.discard("new1")
print(mySet)

mySet.pop()

print(mySet)

mySet.clear()
print(mySet)
