myList = [(1, 2), (), (3, 4), (), (5,)]

# using List Comprehension
print("using List Comprehension",[item for item in myList if item])

result = list(filter(lambda item : item , myList))
print("Using filter() lambda",result)

# list(filter(None, a)) filters out empty tuples from a by retaining only elements that evaluate to True, as empty tuples are False in Python.
print("Using filter None attribute", list(filter(None, myList)))

# usng for loop
res = []
for val in myList:
    if val:
        res.append(val)

print("Using for loop", res)