myList = [10,20,30]

myList.append(40)
print("Append",myList)
myList.insert(2,50)
print("Insert",myList)
removedElement = myList.pop(-1)
print("List after pop:",myList)
print("removedElement", removedElement)

# inputList = []

# n = int(input())
# for i in range(n):
#     inputElement = int(input())
#     inputList.append(inputElement)

# print(inputList)

# take input in single line
newList = input().split(" ")
print(newList)

for i in range(len(newList)):
    print(i)
    print(newList[i])
    newList[i] = int(newList[i])
print(newList)