myList = [22,33,44,55,66,77]

myList[2] = 99
print(myList)

# Using slicing for multiple items
myList[1:3] = [12,23]
print(myList)

# Using List comprehension double the even number
print([item * 2 if item % 2 == 0 else item for item in myList])

# Using loop add 5 to the odd number
for i, val in enumerate(myList):
    if val % 2 != 0:
        myList[i] += 5

    
print(list(enumerate(myList)))

# Using map funciton
print("Updated List:", myList)
print("Add by 1 using map lambda function")
myList = list(map(lambda x: x+1, myList))

print(myList)

