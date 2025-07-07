# def toSum(num1,num2):
#     print(num1 + num2)

# a = int(input())
# b = int(input())

# toSum(a,b)

#Dynamic params

def dynamiSum(*numbers):
    sum = 0
    for i in numbers:
        sum += i
    return sum

num1 = int(input())
num2 = int(input())

result = dynamiSum(num1,num2)

print("result:",result)

