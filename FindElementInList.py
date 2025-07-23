myList = [10,20,30,40,50]

if 30 in myList:
    print("Element Exists in the list.")
else:
    print("Element Doesn't Exists in the list.")


# Using Loop
key = 60
flag = False

for val in myList:
    if val == key:
        flag = True

print("Element " + ("Exists" if flag else "Does not Exist") + " in the list.")

# Using any()

print("Element " + ("exists" if any(x == 50 for x in myList) else "doesn't exist") + " in the list")

# Using Count
print("Element " + ("exists" if myList.count(31) > 0 else "doesn't exist") + " in the list")
