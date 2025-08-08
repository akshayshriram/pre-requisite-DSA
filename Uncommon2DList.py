from collections import Counter

a = [[1, 2], [3, 4], [5, 6]]
b = [[3, 4], [5, 7], [1, 2]]

sa = set(tuple(x) for x in a)
sb = set(tuple(x) for x in b)

unCommonTuple = sa.symmetric_difference(sb)
print("Uncommon Tuple",unCommonTuple)


# Using counter
c = Counter(tuple(x) for x in a + b)

print("using counter",[list(x) for x in c if c[x] == 1])

# Using list comprehension
uncommonA = [item for item in a if item not in b]
uncommonB = [item for item in b if item not in a]

print("using list comprehension",uncommonA + uncommonB)

# Using Fitler
uA = list(filter(lambda val: val not in b,a))
uB = list(filter(lambda val: val not in a,b))

print("Using filter lambda",uA + uB)