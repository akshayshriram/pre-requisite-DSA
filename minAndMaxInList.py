n = int(input())

myList = list(map(int, input().split()))

minElement = myList[0]
maxElement = myList[0]

for val in myList:
    if val < minElement:
        minElement = val
    if val > maxElement:
        maxElement = val

print(minElement, maxElement)

print(min(myList), max(myList))