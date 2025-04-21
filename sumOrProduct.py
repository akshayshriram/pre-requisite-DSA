num = int(input())

calcType = input()
sum = 0
product = 1

if(calcType.lower() == 'sum'):
    for i in range(1, num + 1):
        sum = sum + i
    print("sum:",sum)
elif(calcType.lower() == 'product'):
    for i in range(1, num + 1):
        product = product * i
    print("product:", product)