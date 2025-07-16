# Sort Tuples by Last Element

# Write a Python program to get a list, sorted in increasing order by the last element in each tuple from a given list of non-empty tuples.
# Sample List : [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
# Expected Result : [(2, 1), (1, 2), (2, 3), (4, 4), (2, 5)]

myList = [(2, 5), (1, 2), (4, 4), (2,0), (2, 3), (2, 1)]

sortedList = [myList[0]]
print(myList)

# for val in myList:
#     print(val[0], val[1])

# for i in range(len(myList)-1):
#     print(myList[i][1])
#     print(myList[i])
#     print("i:", i)
#     if myList[i+1][1] < myList[i][1]:
#         print("i-1:", i-1)
#         sortedList.insert(i-1,myList[i+1])
#     else:
#         print("i:", i)
#         sortedList.insert(i,myList[i+1]) 
# print(sortedList)

for i in range(len(myList)):
    for j in range(len(myList) - i - 1):
        if myList[j][1] > myList[j+1][1]:
            myList[j], myList[j+1] = myList[j+1], myList[j]

print(myList)
    