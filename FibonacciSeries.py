num = 7

n1,n2 = 0,1
count = 0
if(num <= 0):
    print("Please enter a positive integer")
elif(num == 1):
    print("Fibonacci series for num:", num, "is", n1)

else:
    while count < num:
        print(n1)
        count += 1
        if(count < num):
            nth = n1 + n2   
            n1 = n2
            n2 = nth

