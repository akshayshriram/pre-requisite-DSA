n = int(input())

for currentRow in range(n):
    for currentNumber in range(n):
        if(currentNumber < n-(currentRow+1)):
            print(" ", end=" ")
        else:
            print("*", end=" ")
    print("")