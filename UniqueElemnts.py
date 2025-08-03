myList = [1, 2, 1, 1, 3, 4, 3, 3, 5]

result = list(set(myList))

print(result)

result1 = []

for val in myList:
    if val not in result1:
        result1.append(val)

print(result1)
