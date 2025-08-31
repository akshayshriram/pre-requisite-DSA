myStr = "Moon"

print(type(myStr))
setStr = set(myStr)
print(setStr)
print(type(setStr))

myStr2 = "moon is moon"
print(type(myStr2))
setStr2 = set(myStr2.split())
print(setStr2)
print(type(setStr2))

set1 = {1,2,3}

res1 = str(set1)

print(type(res1), res1)

res2 = ", ".join(map(str,set1))
print(type(res2), res2)