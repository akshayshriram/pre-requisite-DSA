myList = [1, 3, 4, 5, 7]

# Using insert
myList.insert(0,6)
print("Using insert", myList)

# Using slicing
print("Using slicing", [8] + myList[:])

# using List concatenation
print("using List concatenation", [9] + myList)