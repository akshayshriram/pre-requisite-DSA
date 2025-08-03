a = [1, 2, 3]
b = [4, 5, 6]

# Concatinate
result = a + b
print("Using concatinate +",result)

# Using extend
# a.extend(b)

# print(a)

# Using * operator
result1 = [*a,*b]

print("Using *operator",result1)

# Using for loop
result2 = []
for val in a :
    result2.append(val)
for val in b :
    result2.append(val)

print("Using for loop",result2)

# Using list comprehension

print("Using List comprehension",[item for item in a] + [item for item in b])

# using lambda

print("using lamda func",list(filter(lambda val: val, a)) + list(filter(lambda val: val, a)))