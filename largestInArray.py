numbers = list(map(int, input().split()))

largestNumber = numbers[0]

for num in numbers:
    if num > largestNumber:
        largestNumber = num 
    
print(largestNumber)