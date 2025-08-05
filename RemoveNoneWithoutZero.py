myList = [1, None, 3, None, 5, 0]

print("Using list comprehension",[item for item in myList if item is not None])

print("Using filter()", list(filter(lambda val: val is not None, myList)))


i = 0
while i < len(myList):
    if myList[i] is None:
        del myList[i]
    else:
        i += 1
print(myList)