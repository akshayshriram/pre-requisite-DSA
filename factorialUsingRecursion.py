def factorial(x):
    if x==1 or x==0:
        return 1
    else:
        return (x * factorial(x-1))

num = 5

result = factorial(num)

print("Factorial for:", num, "is", result)