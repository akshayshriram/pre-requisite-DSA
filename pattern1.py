# Print 0 for even number and * for odd number
n =int(input())
for i in range(n):
    if(i%2 == 0):
        print("0", end="")
    else:
        print("*", end="")

print("")
# using while loop
i=0
while i<n:
    if(i%2 == 0):
        print("0", end="")
    else:
        print("*", end="")
    i+=1