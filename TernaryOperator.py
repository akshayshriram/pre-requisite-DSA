a = 5
b = 3
res = a if a > b else b

# If a > b then a will be res
print(res)

num = 5
print("Even" if num % 2 == 0 else "Odd")

integar = -3

print("Positive" if integar > 0 else "Negative")


# Using dictionary
n1 = 20
n2 = 10
max = {True: n1, False: n2}[n1 > n2]

print(max)

# Lambda func using IIFL

max1 = (lambda x,y: y if y > x else x)(n1,n2)

print(max1)
