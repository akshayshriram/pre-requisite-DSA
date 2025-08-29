a = ["banana", "apple", "cherry"]

# a.sort()
print(a)

res = sorted(a)
print(res)

rev = sorted(a, reverse=True)
print(rev)

b = ["Banana", "apple", "kiwi"]

print(sorted(b))

# Case Insensitive sorting

print(sorted(b, key=str.lower))

# Sorting by length 
print(sorted(b, key=len))

# Custom Logic using function

# sort by last charachter

print(sorted(b, key=lambda s: s[-1]))
