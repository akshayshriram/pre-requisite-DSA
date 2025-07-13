n = int(input())

list = []
sum = 0
for i in range(n):
    currElement = int(input())
    list.append(currElement)    
    sum += currElement

print(sum)