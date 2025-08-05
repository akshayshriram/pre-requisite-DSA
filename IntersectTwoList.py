from collections import Counter

a = [4, 9, 1, 17, 11, 26, 28, 54, 69]
b = [9, 9, 74, 21, 45, 11, 63, 28, 26]

# using set
print("Using Set",list(set(a) & set(b)))

result = [item for item in a if item in b]
print("Using List comprehension", result)

# Using filter
print("Using filter()", list(filter(lambda val: val in a,b)))

# Using Counter
print("Using Counter",list((Counter(a) & Counter(b)).elements()))