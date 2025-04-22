num = int(input())
# Print all prime numbers till the num
if (num < 0):
    print("Prime number cannot be negative numbers")
elif (num == 0 or num == 1):
    print("0 and 1 cannot be prime numbers")
else:
    for i in range(2,num + 1):
        start = 2
        flag = 0
        while start < i:
            if(i % start) == 0:
                flag = 1
                break
            else:
                start += 1
        if(flag == 0):
            print(i) 
            