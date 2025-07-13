n = int(input())

myList = list(map(int, input().split()))

sum = 0
for val in myList:
    sum += val

print("Mean:",sum/n)


# Make sure the list is sorted
# In Odd n - the middle is the median
# In even n - the average of the two middle element is the median

myList.sort()

print(myList)
# Odd middle element
# print(myList[n//2])
# 
if n%2 != 0:
    print("Median:", myList[n//2])
else:
    print("Median:", (myList[n//2] + myList[n//2 -1])/2)


# Using nested loop
# maxCount = 0
# maxElement = myList[0]

# for currElement in myList:
#     currCount = 0
#     for eachElement in myList:
#         if currElement == eachElement:
#             currCount += 1
#     if currCount > maxCount:
#         maxCount = currCount
#         maxElement = currElement

# print("maxCount:", maxCount, "maxElemet", maxElement)

# Using Single loop
maxCount = 0
maxElement = myList[0]
currCount = 1

for i in range(n-1):
    if myList[i] == myList[i+1]:
        currCount += 1
    else:
        if currCount > maxCount:
            maxCount = currCount
            maxElement = myList[i]
        currCount = 1

if currCount > maxCount:
    maxCount = currCount
    maxElement = myList[-1]
print(maxElement, maxCount)