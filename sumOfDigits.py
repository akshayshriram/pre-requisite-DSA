myList = [123,657,234]

# Our goal is to calculate the sum of digits for each number in a list in Python
demo = myList[0]%10
print("demo",demo)
# using loop
result = []
for val in myList:
    total = 0
    while val > 0:
        total += val % 10
        val //= 10 
    result.append(total)

print(result)


# using list comprehension function
result1 = [sum(int(digit) for digit in str(val)) for val in myList]
print(result1)

# Example
# Iteration 1 (val = 123):
# str(123) → '123'

# Iterates over '1', '2', '3'

# Converts to 1, 2, 3

# sum([1, 2, 3]) = 6

# Iteration 2 (val = 456):
# '456' → ['4', '5', '6'] → sum([4, 5, 6]) = 1
        

result2 = list(map(lambda val: sum(int(digit) for digit in str(val)), myList))

print(result2)