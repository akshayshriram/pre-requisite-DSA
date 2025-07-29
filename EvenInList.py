# Find out even number in the list

myList = [1,2,3,4,5,6,7,8,9,10]

result = [item for item in myList if item % 2 == 0]
print("Using list comprehension:",result)

# Using filter()

result1 = list(filter(lambda val: val % 2 == 0, myList))

print("Using filter lambda function",result1)

# Using loop
newList = []
for val in myList:
    if val % 2 == 0:
        newList.append(val)

print("Using loop", newList)
