num = 12
factorial = 1
if num < 0:
    print("Factorial does not exits for negative numbers")
elif num == 0:
    print("Factorial of 0 is 1")
else:
    for i in range (1,num + 1):
        factorial = factorial*i
    print("Factorial for num:",num,"is", factorial)
    