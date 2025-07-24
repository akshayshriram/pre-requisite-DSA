myList = [12,23,34,45,56]
myList.reverse()
print(myList)

# Create a new list that is reverse of myList using slicing

reverseList = myList[::-1]

print(reverseList)

myv2List = [1,2,3,4,5]
# use reversed() to create a iterator
# and then convert back to the list
reversed1 = reversed(myv2List)
print(list(reversed1))

reversed2 = []

for val in myv2List:
    reversed2.insert(0, val)

print(reversed2)

v3List = [90,80,70,60,50]
print([v3List[i] for i in range(len(v3List)-1, -1, -1)])