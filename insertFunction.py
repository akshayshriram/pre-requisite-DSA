myList = [1,2,3,4,50,6,7]

myList.insert(2,22)
print(myList)

# Insert before the value of 50

# Value to be inserted
inserElement = 10
# Before the value of 50
insertBeforeValue = 50
index = myList.index(insertBeforeValue)

myList.insert(index, inserElement)

print(myList)

# Insert tuple into the list
updatedIndex = myList.index(insertBeforeValue)
tupleValue = (20,30,40)
myList.insert(updatedIndex, tupleValue)
print(myList)

# Insert element at the Beginning and at the end - it will insert before the end because we insert before the element specified
myList.insert(0,0)
myList.insert(-1,100)
print(myList)


# Inserting a new dictionary
myDictionary=[
    {"fname":"Akshay", "lname": "Shriram","age": 25},
    {"fname":"Pratik", "lname": "Bhoodatt","age": 24},
]
newDictionary =[
    {"fname":"Vipul", "lname": "Bhairi","age": 30},
]

myDictionary.append(newDictionary)

print(myDictionary)

newList = [1,2,3]
v2List = [4,5,6]

UpdatedList= newList + v2List

print(UpdatedList)

v3List = [{7,8,9}]
UpdatedList += v3List
print(UpdatedList)