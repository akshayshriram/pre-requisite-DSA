# Access List Items

myList = [10,20,30,40,50]

print(myList[0])
print(myList[-1])

# List Comprehension
print([item for item in myList if item > 20] )

# List Slicing
# List[start:stop:step]
print(myList[1::2])

# List using loop
for item in myList:
    print(item)
