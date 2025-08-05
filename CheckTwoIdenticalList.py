a = [1, 2, 3]
b = [1, 2, 4]

print("Result",a == b)

a = [1, 2, 3]
b = [1, 2, 3]

flag = True

if(len(a) != len(b)):
    flag = False
else:
    for i in range(len(a)):
        if a[i] != b[i]:
            flag = False
            break

print(flag)

# Using all() with zip()
flag1 = all(x == y for x,y in zip(a,b))
print(flag1)