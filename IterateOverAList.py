myLsit = [1, 3, 5, 7, 9]

print("Using val")
for val in myLsit:
    print(val)

print("Using range")
for i in range(len(myLsit)):
    print(myLsit[i])

i = 0
print("Using While")
while i < len(myLsit):
    print(myLsit[i])
    i+=1

print("Enumerate")

for i, val in enumerate(myLsit):
    print(i, val)

print("Using list comprehension")

[print(val) for val in myLsit]
