n = int(input())

for i in range(1, n+1):

    temp = i
    while(temp%2 == 0):
        temp /= 2
    if temp == 1:
        break
    print(i)