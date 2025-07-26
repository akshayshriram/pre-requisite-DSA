myList = [10,20,30,40,50]

print("Using Sum func:",sum(myList))
print("average:",sum(myList) / len(myList) if myList else 0)

# Using Loop
sum = 0
length = 0

for val in myList:
    length += 1
    sum += val

print("Sum using Loop",sum)
print("Average", sum / length)