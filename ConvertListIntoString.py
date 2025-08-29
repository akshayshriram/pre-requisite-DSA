from functools import reduce

a = ['P', 'y', 't', 'h', 'o', 'n']

print("".join(a))

print(reduce(lambda x,y: x + y, a))

res = ""

for item in a:
    res += item

print(res)