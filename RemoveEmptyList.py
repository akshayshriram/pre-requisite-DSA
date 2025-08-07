a = [[1, 2], [], [3, 4], [], [5]]

result = []

for val in a:
    if val:
        result.append(val)

print("Using loop", result)

# Using List comprehension
print("Using List Comprehension", [item for item in a if item])

# using lambda
print("Using lmabda", list(filter(lambda val: val, a)))