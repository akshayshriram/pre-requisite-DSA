a = [1, 2, 3, 4]
b = [3, 4, 5, 6]

print("Using set with union", list(set(a).union(b)))

# | -->similar to unioon with shorthand
print("using set with |", list(set(a) | set(b)))

# Using list comprenhension
print("Using list comprenhension", list(set([item for item in a + b])))