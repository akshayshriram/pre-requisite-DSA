myDict = {"student1": 40, "student2": 50}
# In Dictionary we cannot pass index as we pass in list, we need to pass key

print(myDict["student1"])
print(myDict.get("student2"))

# If we pass the invalid key directly to the myrDir["student5"], It will throw error unlikely the .get returns None
print(myDict.get("student5"))

myDict["student3"] = 30
print(myDict)


# Iteration over Dictionary

for key in myDict.keys():
    print(key, myDict[key])

for value in myDict.values():
    print(value)

for key, value in myDict.items():
    print(key, value)


print(myDict.keys())
print(myDict.values())
print(myDict.items())

targetKey = "student1"
targetValue = 40
if targetKey in myDict:
    print("ket is present")

if targetValue in myDict.values():
    print("value is present")